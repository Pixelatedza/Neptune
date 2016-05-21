app.controller('ListController', function($scope, $http) {
	$scope.pageObj = {} // The page object
	$scope.paginator = {} // paginator
	$scope.objectList = [] // data
	$scope.pageObj.next = 0;
	$scope.pageObj.prev = 0;
	$scope.pageObj.number = 1;
	$scope.pageObj.hasPrev = false;
	$scope.pageObj.hasNext = false;
	$scope.pageObj.end = 0;
	$scope.pageObj.start = 0;
	$scope.paginator.count = 0;
	$scope.paginator.perPage = 0;
	$scope.paginator.numPages = 0;
	$scope.selectedItems = {}

	$scope.prevPage = function(){
		$scope.getPage($scope.pageObj.prev)
	}

	$scope.nextPage = function(){
		$scope.getPage($scope.pageObj.next)
	}

	$scope.getPage = function(page_number){
		// Posting data as json
		$http({
			method: 'POST',
			url: "/nepcore/auth/users/",
			data: {
				page: page_number,
				paginateBy: $scope.paginator.perPage
			},
			}).then(function successCallback(response) {
				$scope.paginator = response.data.paginator;
				$scope.pageObj = response.data.page_obj;
				$scope.objectList = response.data.object_list;
			}, function errorCallback(response) {
			});
		};

	$scope.select = function(itemPK){
		if(!(itemPK in $scope.selectedItems)){
			$scope.selectedItems[itemPK] = true;
		}else{
			delete $scope.selectedItems[itemPK]
		};
		console.log($scope.selectedItems)
	};
});
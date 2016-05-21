app.controller('ListController', function($scope, $http, AjaxService) {
	$scope.url = ""
	$scope.loading = true;
	$scope.pageObj = {}; // The page object
	$scope.paginator = {}; // paginator
	$scope.objectList = []; // data
	$scope.indexPKMap = {};
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
	$scope.selectedItems = {};
	$scope.ajax = AjaxService;

	$scope.prevPage = function(){
		$scope.getPage($scope.pageObj.prev);
	}

	$scope.nextPage = function(){
		$scope.getPage($scope.pageObj.next);
	}

	$scope.getPage = function(page_number){
		// Posting data as json
		$scope.loading = true;
		$http({
			method: 'POST',
			url: $scope.url,
			data: {
				page: page_number,
				paginateBy: $scope.paginator.perPage
			},
			}).then(function successCallback(response) {
				$scope.paginator = response.data.paginator;
				$scope.pageObj = response.data.page_obj;
				$scope.objectList = response.data.object_list;
				$scope.itemPKMap = {}
				for (obj in $scope.objectList){
					$scope.itemPKMap[$scope.objectList[obj].pk] = obj;
				};
			}, function errorCallback(response) {
			}).finally(function(){
				$scope.loading = false;
			});
		};

	$scope.select = function($event, itemPK){
		if(!(itemPK in $scope.selectedItems) && $event.target.localName == "td"){
			$scope.selectedItems[itemPK] = true;
		}else if($event.target.localName == "td"){
			delete $scope.selectedItems[itemPK];
		};
	};

	$scope.create = function(itemPK){
		console.log("NOT IMPLEMETED!")
	};

	$scope.edit = function(itemPK){
		console.log("NOT IMPLEMETED!")
	};

	$scope.delete = function(itemPK){
		console.log("NOT IMPLEMETED!")
	};
});

app.controller('UserListController', function($scope, $controller) {
	$controller('ListController', {$scope: $scope});
	$scope.url = "/nepcore/auth/users/";

	$scope.edit = function(){
		console.log("NOT IMPLEMETED!")
	};

	$scope.delete = function(){
		console.log("NOT IMPLEMETED!")
	};
});

app.controller('ItemListController', function($scope, $controller, $state) {
	$controller('ListController', {$scope: $scope});
	$scope.url = "/nepcore/item/get/items/";
	$scope.create_state = "create_edit_item_state";
	$scope.edit_state = "create_edit_item_state";
	$scope.delete_state = "create_item_state";

	$scope.create = function(itemTypeName){
		state = $state.get($scope.create_state);
		$state.go($scope.create_state, {url: state.data.my_link + itemTypeName});
	};

	$scope.edit = function(itemPk){
		state = $state.get($scope.edit_state);
		itemTypeName = $scope.objectList[$scope.itemPKMap[itemPk]].fields.itemType.name
		$state.go($scope.create_state, {url: state.data.my_link + itemTypeName + "/" + itemPk});
	};

	$scope.delete = function(){
		console.log("NOT IMPLEMETED!")
	};
});
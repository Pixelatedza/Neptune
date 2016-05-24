app.controller('ListController', function($scope, $http, AjaxService) {
	$scope.url = "";
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
	$scope.selectedItemsCount = 0;
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
				$scope.indexPKMap = {}
				for (obj in $scope.objectList){
					$scope.indexPKMap[$scope.objectList[obj].pk] = obj;
				};
			}, function errorCallback(response) {
			}).finally(function(){
				$scope.loading = false;
			});
		};

	$scope.select = function($event, itemPK){
		if(!(itemPK in $scope.selectedItems) && $event.target.localName == "td"){
			$scope.selectedItems[itemPK] = true;
			$scope.selectedItemsCount += 1;
		}else if($event.target.localName == "td"){
			delete $scope.selectedItems[itemPK];
			$scope.selectedItemsCount -= 1;
		};
	};

	$scope.create = function(itemPK){
		console.log("NOT IMPLEMENTED!")
	};

	$scope.edit = function(itemPK){
		console.log("NOT IMPLEMENTED!")
	};

	$scope.delete = function(itemPK){
		console.log("NOT IMPLEMENTED!")
	};
});

app.controller('UserListController', function($scope, $controller) {
	$controller('ListController', {$scope: $scope});
	$scope.url = "/nepcore/auth/users/";
	$scope.editing = false;
	$scope.editError = null;

	$scope.edit_group = function(userPK){
		for (group in $scope.groups){
			g = $scope.groups[group]
			if (g.groupName == $scope.objectList[$scope.indexPKMap[userPK]].fields.groups[0]){
				$scope.group = g.groupPK;
			};
		};
		console.log($scope.group);
		$scope.user = userPK;
	};

	$scope.set_groups = function(){
		$scope.ajax.get('/nepcore/auth/groups/', function(success, data){
			$scope.groups = data
		});
	}

	$scope.save_edit = function(){
		$scope.editing = true;
		data = {
			group: $scope.group,
			user: $scope.user
		};
		$scope.ajax.post('/nepcore/auth/users/edit/group/', data, function(success, data){
			if (success){
				$('#editModal').modal('hide');
				for (group in $scope.groups){
					g = $scope.groups[group]
					if (g.groupPK == $scope.group){
						$scope.groupName = g.groupName;
					};
				};
				$scope.objectList[$scope.indexPKMap[$scope.user]].fields.groups[0] = $scope.groupName;
				$scope.groupName = "";
				$scope.editError = null;
			}
			else{
				$scope.editError = data.msg;
			}
			$scope.editing = false;
		});
	};

	$scope.delete = function(){
		console.log("NOT IMPLEMENTED!")
	};

	$scope.close_modal = function(){
		$('#editModal').modal('hide');
		$scope.editError = null;
	};
});

app.controller('ItemListController', function($scope, $controller, $state) {
	$controller('ListController', {$scope: $scope});
	$scope.url = "/nepcore/item/list/items/";
	$scope.create_state = "create_edit_item_state";
	$scope.edit_state = "create_edit_item_state";
	$scope.delete_state = "create_item_state";
	$scope.emailError = null;
	$scope.toEmail = "";
	$scope.emailing = false;
	$scope.item = {};

	$scope.create = function(itemTypeName){
		state = $state.get($scope.create_state);
		$state.go($scope.create_state, {url: state.data.my_link + itemTypeName});
	};

	$scope.view = function(itemPK){
		$scope.ajax.get('/nepcore/item/get/item/'+ itemPK, function(success, data){
			$scope.item = data;
		});
	};

	$scope.edit = function(itemPK){
		state = $state.get($scope.edit_state);
		itemTypeName = $scope.objectList[$scope.indexPKMap[itemPK]].fields.itemType.name;
		$state.go($scope.create_state, {url: state.data.my_link + itemTypeName + "/" + itemPK});
	};

	$scope.delete = function(){
		console.log("NOT IMPLEMETED!")
	};

	$scope.export = function(){
		$scope.ajax.postDownload('/nepcore/item/export/items/', $scope.selectedItems);
	};

	$scope.email = function(){
		$scope.emailing = true;
		data = {
			items: $scope.selectedItems,
			toEmail: $scope.toEmail
		};
		$scope.ajax.post('/nepcore/item/email/items/', data, function(success, data){
			if (success){
				$('#emailModal').modal('hide');
				$scope.emailError = null;
				$scope.toEmail = "";
			}
			else{
				$scope.emailError = data.msg;
			}
			$scope.emailing = false;
		});
	};

	$scope.close_mail = function(){
		$('#emailModal').modal('hide');
		$scope.toEmail = "";
		$scope.emailError = null;
	};
});
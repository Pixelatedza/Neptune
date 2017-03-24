//
// Handles the copying of item type fields.
//
app.controller('copyItemType', function($scope, $http) {
	// create a blank object to handle form data.
	$scope.fields = {};
	// calling our submit function.
	$scope.getItemTypeFields = function(url) {
		// Posting data as json
		$http({
			method: 'POST',
			url: "/item/get/item-type-fields/",
			data: $scope.formData
			}).then(function successCallback(response) {
				$scope.fields = response.data;
			}, function errorCallback(response) {
			});
	};
});

//
// Deals with the posting of data over ajax, coincidentally does forms for
// the time being as well.
//
app.controller('postController', function($scope, $http) {
	// create a blank object to handle form data.
	$scope.formData = {};
	$scope.formErrors = {};
	// calling our submit function.
	$scope.submitForm = function(url) {
		// Posting data as json
		console.log($scope.formData)
		$http({
			method: 'POST',
			url: url,
			data: $scope.formData
			}).then(function successCallback(response) {
				$scope.formData = {};
				$scope.formErrors = {};
			}, function errorCallback(response) {
				$scope.formErrors = response.data;
			});
	};
});
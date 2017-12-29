app.controller('dynamicForms', function($scope, $http, DynamicForm) {
	// create a blank object to handle form data.
	// calling our submit function.
	$scope.getItemTypeFields = function(itemName) {
		// Posting data as json
		$http({
			method: 'POST',
			url: "/item/get/item-type-fields/",
			data: {itemName: itemName}
			}).then(function successCallback(response) {
				// Potential bug if no fields are returned, forms will be cleared.
				// Minor issue though.
				fields = response.data;
				$scope.forms = [];
				$scope.count = 0
				console.log(fields);
				for (field in fields){
					$scope.addForm(fields[field]);
				};
			}, function errorCallback(response) {
			});
	};

	// This handles the forms html when adding and removing forms.
	$scope.forms = [DynamicForm.createNew(0)];
	$scope.count = 1

	$scope.removeForm = function(i){
		$scope.forms.splice(i, 1);
		forms = $scope.forms.slice(i)
		for (index in forms){
			forms[index].lowerIndex();
		};
		$scope.count = $scope.count - 1;
	};

	$scope.addForm = function(formData){
		$scope.forms.push(DynamicForm.createNew($scope.count, formData));
		$scope.count = $scope.count + 1;
	};

	// Submission of dynamic forms is a bit different to normal forms.
	// create a blank object to handle form data.
	$scope.formData = {};
	$scope.formErrors = {};

	// calling our submit function.
	$scope.submitForm = function(url) {
		// add the dynamic forms data to the global form data.
		$scope.formData.attributes = []
		for (index in $scope.forms){
			form = $scope.forms[index];
			form.formData.index = form.index;
			$scope.formData.attributes.push(form.formData);
		};
		// Posting data to django as json
		$http({
			method: 'POST',
			url: url,
			data: $scope.formData
			}).then(function successCallback(response) {
				$scope.formData = {};
				$scope.forms = [DynamicForm.createNew(0)];
				$scope.count = 1;
				$scope.formErrors = {};
			}, function errorCallback(response) {
				$scope.formErrors = response.data;
			});
	};
});
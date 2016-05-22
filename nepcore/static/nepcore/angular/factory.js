app.factory('DynamicForm', function(){
	function DynamicFormInstance(index, formData={}){
		this.index = index;
		this.formData = formData;
		this.errors = {};
		this.lowerIndex = function(){
			this.index = this.index - 1;
		}
	};

	return {
		createNew: function(index, formData){
			return new DynamicFormInstance(index, formData);
		}
	};
});

app.factory('AjaxService', function($http, FileSaver, Blob){
	function nepGet(url) {
		// Posting data as json
		$http({
			method: 'GET',
			url: url,
			}).then(function successCallback(response) {
				console.log(response.data);
			}, function errorCallback(response) {
			});
	};

	function nepPost(url, data) {
		// Posting data as json
		$http({
			method: 'POST',
			url: url,
			data: data,
			}).then(function successCallback(response) {
				console.log(response.data);
			}, function errorCallback(response) {
			});
	};

	function nepPostDownload(url, data){
		// Posting data as json
		$http({
			method: 'POST',
			url: url,
			data: data,
			}).then(function successCallback(response) {
				data = new Blob([response.data], {type: 'text/csv'});
				FileSaver.saveAs(data, 'exported_items.csv')
			}, function errorCallback(response) {
			});
	}

	return {
		get: function(url){
			nepGet(url);
		},
		post: function(url, data){
			nepPost(url, data);
		},
		postDownload: function(url, data){
			nepPostDownload(url, data);
		}
	};
});

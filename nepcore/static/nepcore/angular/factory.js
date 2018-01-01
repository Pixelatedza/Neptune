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
	function nepGet(url, callBack) {
		// Posting data as json
		$http({
			method: 'GET',
			url: url,
			}).then(function successCallback(response) {
				if (callBack){
					callBack(true, response.data);
				}
			}, function errorCallback(response) {
				if (callBack){
					callBack(false, response.data);
				}
			});
	};

	function nepPost(url, data, callBack) {
		// Posting data as json
		$http({
			method: 'POST',
			url: url,
			data: data,
			}).then(function successCallback(response) {
				if (callBack){
					callBack(true, response.data);
				}
			}, function errorCallback(response) {
				if (callBack){
					callBack(false, response.data);
				}
			});
	};

	function nepPostDownload(url, data, callBack){
		// Posting data as json
		$http({
			method: 'POST',
			url: url,
			data: data,
			}).then(function successCallback(response) {
				data = new Blob([response.data], {type: 'text/csv'});
				FileSaver.saveAs(data, 'exported_items.csv')
				if (callBack){
					callBack(true, response.data);
				}
			}, function errorCallback(response) {
				if (callBack){
					callBack(false, response.data);
				}
			});
	}

	return {
		get: function(url, callBack){
			nepGet(url, callBack);
		},
		post: function(url, data, callBack){
			nepPost(url, data, callBack);
		},
		postDownload: function(url, data, callBack){
			nepPostDownload(url, data, callBack);
		}
	};
});


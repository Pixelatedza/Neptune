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

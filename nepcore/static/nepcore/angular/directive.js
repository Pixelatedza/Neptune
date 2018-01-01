app.directive("scroll", function ($window) {
	return function(scope, element, attrs) {
		angular.element($window).bind("scroll", function() {
			if (this.pageYOffset >= 50) {
				scope.navOffset = {'padding-top': "0px"}
				scope.$digest()
			} else {
				scope.navOffset = {'padding-top': (50 - this.pageYOffset).toString() + "px"}
				scope.$digest()
			}
		});
	};
});

app.directive("realTime", function($http, $compile){
	return {
		scope: {},
		link: function(scope, element, attrs, controller){
			scope.attrs = attrs;
			scope.element = element;
			
			scope.reload = function() {
				$http.get('menus/').success(function(tplContent){
	                scope.element.children().eq(0).replaceWith($compile(tplContent)(scope));                
	            }); 
			};
			
			scope.$on("reload." + scope.attrs.realTime, function(event, data){
				scope.reload();
			})
		},
		templateUrl: function(elem, attrs){
			return  attrs.realTime || "Specify template url. real-time='template'";
		}
	};
});
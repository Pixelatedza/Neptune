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
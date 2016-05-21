var app = angular.module('NeptuneApp', ['ui.router']).config(function($interpolateProvider,$httpProvider) {
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.run(['$rootScope','$state', '$http', function ($rootScope, $state, $http) {
	$http({
			method: 'GET',
			url: "/nepcore/states/",
			}).then(function successCallback(response) {
				loadStates(response.data);
				$state.transitionTo('index');
			}, function errorCallback(response) {
			});

}]);

app.config(function($stateProvider, $urlRouterProvider, $interpolateProvider){
	loadStates = function(states){
		for (state in states){
			s = states[state];
			$stateProvider.state(s.name, {
					url: s.url,
					controller: function($templateCache){
						$templateCache.remove(s.link);
					},
					templateUrl: s.link
			})
		};
	}
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

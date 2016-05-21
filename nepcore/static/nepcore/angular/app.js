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
				console.log($state)
				$state.go('index', {state: $state});
				console.log($state.get())
			}, function errorCallback(response) {
			});

}]);

app.config(function($stateProvider, $urlRouterProvider, $interpolateProvider){
	loadStates = function(states){
		stateNameLinks = {}
		for (state in states){
			s = states[state];
			if (s.params){
				$stateProvider.state(s.name, {
					url: s.url,
					data: {
						my_link: s.link
					},
					controller: function($templateCache, $state, $stateParams){
						$templateCache.remove($stateParams.url);
					},
					templateUrl: function($stateParams){
						return $stateParams.url;
					}
				});		

			}else{
				$stateProvider.state(s.name, {
					url: s.url,
					data: {
						my_link: s.link
					},
					controller: function($templateCache, $state){
						$templateCache.remove($state.current.data.my_link);
					},
					templateUrl: s.link
				});				
			};
		};
	};
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

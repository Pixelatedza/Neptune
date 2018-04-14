var app = angular.module('NeptuneApp', ['ui.router','ngFileSaver']).config(function($interpolateProvider,$httpProvider) {
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.run(['$rootScope','$state', '$http', function ($rootScope, $state, $http) {
	$http({
		method: 'GET',
		url: "/nepcore/states/",
		}).then(function successCallback(response) {
			loadStates(response.data.states);
			$state.go(response.data.default_state);
		}, function errorCallback(response) {
	});
	
	// Create websocket and setup listeners for specifics streams.
	// This code needs to be put somewhere cleaner, I'm not a fan of having demultiplex defined
	// over and over in the app.run.
	const webSocketBridge = new channels.WebSocketBridge();
	webSocketBridge.connect('/real_time_updates/');
	webSocketBridge.listen();

	webSocketBridge.demultiplex('menu', function(action, stream) {
		console.log(action, stream);
		$rootScope.$broadcast('reload.menus');
	});
	webSocketBridge.demultiplex('state', function(action, stream) {
		console.info(action, stream);
	});
	
	webSocketBridge.socket.addEventListener('open', function() { console.log("Connected to notification socket"); });
	webSocketBridge.socket.addEventListener('close', function() { console.log("Disconnected to notification socket"); });
}]);

app.config(function($stateProvider, $urlRouterProvider, $interpolateProvider){
	loadStates = function(states){
		stateNameLinks = {};
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
						console.log($state.current.data.my_link)
						$templateCache.remove($state.current.data.my_link);
					},
					templateUrl: s.link
				});				
			};
		};
	};
	$interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

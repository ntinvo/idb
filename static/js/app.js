var mainApp = angular.module('ngGGMate', ['ngRoute']);

// Routes
mainApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider
    .when('/test', {
        templateUrl: '/templates/test.html',
        controller: 'testCtrl'
    })
    .otherwise({
        templateUrl: '/templates/test.html',
        controller: 'testCtrl'
    })

}]);


mainApp.controller('testCtrl', function($scope, $http) {
    $http.get('/run_unittests').then(function(result){
        console.log(result.data.output);
        $scope.output = '\n' + result.data.output;
    });
});
var app = angular.module("VigeFront", ['ngRoute'])

app.config(function($routeProvider) {

  $routeProvider.when('/main', {
    templateUrl: '/static/partials/main.html',
    controller: 'mainCtrl'
  });

  $routeProvider.when('/home', {
    templateUrl: '/static/partials/home.html',
    controller: 'HomeController'
  });

  $routeProvider.otherwise({ redirectTo: '/main' });

});

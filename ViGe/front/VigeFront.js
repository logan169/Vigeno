var app = angular.module("VigeFront", ['ngRoute','ViGeFront.main.controllers','flow'])

app.config(function($routeProvider) {

  $routeProvider.when('/', {
    templateUrl: '/front/modules/main/html/main.html',
    controller: 'mainCtrl'
  });

  $routeProvider.otherwise({ redirectTo: '/' });

});

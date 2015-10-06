(function(){
'use strict';

var mainCtrl = function(mainService){
	this.data = {};
};

angular
  .module('modules.main', [])
  
  .config(['$stateProvider', function($stateProvider) {
    $stateProvider
      .state('main', {
        url: '/main',
        templateUrl: 'modules/main/main.html',
        controllerAs: 'mainCtrl',
        controller: 'mainCtrl'
      });
  }])

  .controller('mainCtrl', [
    'mainService',
    mainCtrl
  ]);

})();

(function(){
'use strict';

// Declare app level module which depends on filters, and services
angular.module('VigeFront', [
  'ui.router',
  'modules.main'
])
.config([
  '$urlRouterProvider', 
  //use this line for Providers
  // 'ActivityProvider',
  function($urlRouterProvider
    //use this line for Providers
    //, ActivityProvider
    ) {
    
    //use this line for Providers
    // ActivityProvider.setAPI('../test/api/posts.json');

    $urlRouterProvider.otherwise('/main');
}]);

})();

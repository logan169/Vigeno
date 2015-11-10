var app = angular.module('ViGeFront.main.controllers','flow');

app.controller('uploadController', function($modalInstance, $scope,$http,$rootScope) {


  /*envoie au serveur les inputs via l'URL*/
   $scope.sendData=function(data){
        $http({
        method: 'GET',
        url: 'api/v0/uploadURL/'+data+'/'
        }).then(function successCallback(response) {
	        // this callback will be called asynchronously
	        // when the response is available
	        console.log(response.data);
	        $rootScope.results=response;
  	    },
   		function errorCallback(response) {
   	        // called asynchronously if an error occurs
   	        // or server returns response with an error status.
  	        console.log("Erreur lors de l'envoie des données");
  	        console.log(response);
  	    })
   };


  $scope.ok = function () {
        $modalInstance.close();
  };

  $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
  };
});



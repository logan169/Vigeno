var app = angular.module('ViGeFront.main.controllers');

app.controller('uploadController', function($modalInstance, $scope,$http,$rootScope,$window) {

    $scope.fileStatus=false,
    $scope.dataStatus=false,

    $scope.changeFileStatus=function(file){
        console.log(file)
        /* si le fichier est different de undefined, le statut devient true*/
        $scope.fileStatus=(angular.isUndefined(file))

    }

    $scope.changeDataStatus=function(inputText){
        console.log(inputText)
        /* si la longueur du texte dans la boite est >0, le statut devient true*/
        $scope.dataStatus=((angular.isUndefined(inputText) != true) && (inputText.length>0))
    }

    $scope.evaluateInputType=function(data,file){
        console.log(data,file)

        if (($scope.dataStatus==true) && ($scope.fileStatus=false)){

            /*envoie au serveur les inputs via l'URL*/
            $scope.sendData=function(data){
            $http({
            method: 'GET',
            url: 'api/v0/uploadURL/'+data+'/'
            }).then(function successCallback(response) {
	            // this callback will be called asynchronously
	            // when the response is available
	            console.log(response);
	            $rootScope.results=response;
	            $scope.ok
  	        },
   		    function errorCallback(response) {
   	            // called asynchronously if an error occurs
   	            // or server returns response with an error status.
  	            console.log("Erreur lors de l'envoie des données");
  	            console.log(response);
  	            })
            };
        }
        else if (($scope.dataStatus==false) && ($scope.fileStatus=true)){
            /*envoie au serveur un fichier*/
            $scope.sendFile=function(file,$scope){

            $http({
            method: 'POST',
            url: 'api/v0/uploadFile/'+file+'/'
            }).then(function successCallback(response) {
	            // this callback will be called asynchronously
	            // when the response is available
	            console.log(response.data);
	            $rootScope.results=response;
                $scope.ok
  	        },
   		    function errorCallback(response) {
   	            // called asynchronously if an error occurs
   	            // or server returns response with an error status.
  	            console.log("Erreur lors de l'envoie du fichier");
  	            console.log(response);
  	            })
            };
        }
        else if (($scope.dataStatus==true) && ($scope.fileStatus=true)){
            /* send error message, enter only one input! */
            alert('Error!! enter multiple input detected!')
        }
        else if (($scope.dataStatus==false) && ($scope.fileStatus=false)){
            /* send error message, enter only one input! */
            alert('upload canceled!')
        }
    }









  $scope.ok = function () {
        $modalInstance.close();
  };

  $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
  };
});



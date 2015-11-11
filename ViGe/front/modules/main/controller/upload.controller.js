var app = angular.module('ViGeFront.main.controllers');

app.controller('uploadController', function($modalInstance, $scope,$http,$rootScope,$window) {

    $scope.fileStatus=false,
    $scope.dataStatus=false,
    $scope.inputText='Enter a querie directly in this box or upload a file!\n\nformat:\nchromosome<SPACE>startPosition<SPACE>',

    $scope.resetUploadBox=function(){
        $scope.inputText='';
    }

    $scope.file_changed = function(element) {
    $scope.$apply(function(scope) {$scope.fileStatus=angular.isDefined(element.files[0]) && element.files[0].name.length>0});
    $scope.resetUploadBox()
    }

    /* si la longueur du texte dans la boite est >0, le statut devient true*/
    $scope.changeDataStatus=function(inputText){$scope.dataStatus= (angular.isDefined(inputText)) && inputText.length>0}

    $scope.evaluateInputType=function(data,file){
        /*console.log($scope.dataStatus,$scope.fileStatus)*/

        if (($scope.dataStatus) && (!$scope.fileStatus)){

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
	            $scope.ok()
  	        },
   		    function errorCallback(response) {
   	            // called asynchronously if an error occurs
   	            // or server returns response with an error status.
  	            console.log("Erreur lors de l'envoie des données");
  	            console.log(response);
  	            })
            };
        }
        
        else if (($scope.dataStatus==false) && ($scope.fileStatus==true)){
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
                $scope.ok()
  	        },
   		    function errorCallback(response) {
   	            // called asynchronously if an error occurs
   	            // or server returns response with an error status.
  	            console.log("Erreur lors de l'envoie du fichier");
  	            console.log(response);
  	            })
            };
        }

         else if (($scope.dataStatus==true) && ($scope.fileStatus==true)) {
        /* send error message, enter only one input! */
            alert('Error!! enter only one input! ')
        }

        else if (($scope.fileStatus==false) && ($scope.inputText =='Enter a querie directly in this box or upload a file!\n\nformat:\nchromosome<SPACE>startPosition<SPACE>')){
            alert('Error! enter an input')
        }

        else if (($scope.dataStatus==false) && ($scope.fileStatus==false)){
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



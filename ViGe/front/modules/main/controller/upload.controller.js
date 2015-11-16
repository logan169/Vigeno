var app = angular.module('ViGeFront.main.controllers');

app.controller('uploadController', function($modalInstance, $scope,$http,$rootScope,$window) {
    $scope.fileStatus=false,
    $scope.dataStatus=false,
    defaultInputText='Enter a querie directly in this box or upload a file!\n\nformat:\nchromosome<SPACE>startPosition<SPACE>',
    $scope.inputText=defaultInputText,
    $scope.Validation='',
    $scope.fileName=''

    /*envoie au serveur un fichier*/
    $scope.sendFile=function(file){
    $http({
    method: 'POST',
    url: '/import'
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
  	    $scope.Validation="Erreur lors de l'envoie des données, veuillez verifier le format soumis"
  	    })
    };


    $scope.resetUploadBox=function(){
        if ($scope.inputText == defaultInputText){
            $scope.inputText='';
    }}

    $scope.file_changed = function(element) {
    $scope.$apply(function(scope) {$scope.fileStatus=angular.isDefined(element.files[0]) && element.files[0].name.length>0});
    $scope.resetUploadBox()
    $scope.fileName=element.files[0].name
    }

    /*######################################################################*/

    /* si la longueur du texte dans la boite est >0, le statut devient true*/
    $scope.changeDataStatus=function(inputText){
    if (inputText==defaultInputText){$scope.dataStatus = false}
    else {$scope.dataStatus = (angular.isDefined(inputText)) && inputText.length>0
    }}

    $scope.evaluateInputType=function(data,file){
        console.log('data: ' + $scope.dataStatus, 'file:' +$scope.fileStatus)
        $scope.Validation=''

        if (($scope.dataStatus==false) && ($scope.fileStatus==true)){
            $scope.sendFile(file),
            $scope.Validation='Analyse en cours, veuillez patienter. '
        }

        else if (($scope.dataStatus==true) && ($scope.fileStatus==false)){
            console.log(data),
            $scope.sendData(data),
            $scope.Validation='Analyse en cours, veuillez patienter. '

        }

         else if (($scope.dataStatus==true) && ($scope.fileStatus==true)) {
        /* send error message, enter only one input! */
            $scope.Validation='Error!! enter only one input! '
        }

        else if ((($scope.fileStatus==false) && ($scope.inputText ==defaultInputText))||(($scope.dataStatus==false) && ($scope.fileStatus==false)))
        {

            $scope.Validation='Error! enter an input or click cancel!'
        }

        else if (($scope.dataStatus==false) && ($scope.fileStatus==false)){
            /* send error message, enter only one input! */
            $scope.Validation='upload canceled!'
        }
    }

  $scope.ok = function () {
        $modalInstance.close();
  };

  $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
  };
});



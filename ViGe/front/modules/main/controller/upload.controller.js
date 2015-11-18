var app = angular.module('ViGeFront.main.controllers');

app.controller('uploadController', function($modalInstance, $scope,$http,$rootScope,$window) {
    $scope.fileStatus=false,
    $scope.dataStatus=false,
    defaultInputText='Enter a querie directly in this box or upload a file!\n\nformat:\nchromosome<SPACE>startPosition<SPACE>',
    $scope.inputText=defaultInputText,
    $scope.ValidationMessage='',
    $scope.Validation=false,
    $scope.fileName='',
    $scope.submit=false,

    /*envoie au serveur un fichier*/
    $scope.sendFile=function(fileName){
    $http({
    method: 'POST',
    url: '/api/v0/processFile/'+fileName+'/'
    }).then(function successCallback(response) {
	    // this callback will be called asynchronously
	    // when the response is available
	    console.log(response.data);
	    console.log(response);
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
    url: '/api/v0/uploadURL/'+data+'/'
    }).then(function successCallback(response) {
	    // this callback will be called asynchronously
	    // when the response is available
	    console.log(response.data);
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
    $scope.$apply(function(scope) {console.log(angular.isDefined(element.files[0]) && element.files[0].name.length>0);$scope.fileStatus=angular.isDefined(element.files[0]) && element.files[0].name.length>0});
    $scope.resetUploadBox()
    $scope.fileName=element.files[0].name
    $scope.fileName=$scope.fileName.replace(/ /g, "_")
    }

    /*######################################################################*/

    /* si la longueur du texte dans la boite est >0, le statut devient true*/
    $scope.changeDataStatus=function(inputText){
    if (inputText==defaultInputText){$scope.dataStatus = false}
    else {$scope.dataStatus = (angular.isDefined(inputText)) && inputText.length>0
    }}

    $scope.evaluateInputType=function(data,file){
        console.log('data: ' + $scope.dataStatus, 'file:' +$scope.fileStatus)
        $scope.Validation=false

        if (($scope.dataStatus==false) && ($scope.fileStatus==true) && ($scope.submit==true)){
            $scope.Validation=true,
            $scope.ValidationMessage='Analyse en cours, veuillez patienter!',
            $scope.sendFile(file)
        }

        else if (($scope.dataStatus==false) && ($scope.fileStatus==true) && ($scope.submit==false)){
            $scope.Validation=false,
            $scope.ValidationMessage='Fichier non uploadé, veuillez cliquer sur upload svp.'
        }

        else if (($scope.dataStatus==true) && ($scope.fileStatus==false)){
            $scope.Validation=true,
            $scope.ValidationMessage='Analyse en cours, veuillez patienter!',
            $scope.sendData(data)
        }

         else if (($scope.dataStatus==true) && ($scope.fileStatus==true)) {
        /* send error message, enter only one input! */
            $scope.Validation=false,
            $scope.ValidationMessage="Veuillez n'entrez qu'un seul input!"
        }

        else if ((($scope.fileStatus==false) && ($scope.inputText ==defaultInputText))||(($scope.dataStatus==false) && ($scope.fileStatus==false)))
        {
            $scope.Validation=false,
            $scope.ValidationMessage='Error!! enter an input or click cancel!'
        }

        else if (($scope.dataStatus==false) && ($scope.fileStatus==false)){
            /* send error message, enter only one input! */
            $scope.Validation=false,
            $scope.ValidationMessage='Error!! enter an input or click cancel!'
        }
    }

  $scope.ok = function () {
        $modalInstance.close();
  };

  $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
  };
});



var app = angular.module('ViGeFront.main.controllers');

app.controller('uploadController', function( $modalInstance, fileUpload, $scope,$http,$rootScope,$window) {

    $scope.fileStatus=false,
    $rootScope.ValidationMessage='',


   $scope.file_changed = function(element) {
        $scope.$apply(function(scope) {console.log(angular.isDefined(element.files[0]) && element.files[0].name.length>0);$scope.fileStatus=angular.isDefined(element.files[0]) && element.files[0].name.length>0});
   };

  $scope.uploadFile = function(){
        var file = $scope.myFile;
        console.log('file is '+ file.name );
        console.dir(file);
        var uploadUrl = "/api/v0/uploadFile/";
        if ((file.name).length>0){
            fileUpload.uploadFileToUrl(file, uploadUrl);
            $rootScope.ValidationMessage='Analyse en cours, veuillez patienter!';
        }
        else{
        $rootScope.ValidationMessage='Veuillez selectionner un fichier!';
        }
    };

  $rootScope.FileSentCloseModal= function () {
        $modalInstance.close();
  };

  $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
  };
});

app.directive('fileModel', ['$parse', function ($parse) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;

            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
    };
}]);

app.service('fileUpload', ['$http','$rootScope', function ($http,$rootScope) {
    this.uploadFileToUrl = function(file, uploadUrl){
        var fd = new FormData();
        fd.append('file', file);
        $http.post(uploadUrl, fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        })
        .then(function successCallback() {
            $http({
            method: 'POST',
            url: '/api/v0/processFile/'+file.name.replace(/ /g,'_')+'/'
            }).then(function successCallback(response) {
	            // this callback will be called asynchronously
	            // when the response is available
	            console.log(response.data);
	            console.log(response);
	            $rootScope.FileSentCloseModal();
	            $rootScope.results=response;
	            console.log(response)

  	            },
            function errorCallback(response) {
   	            // called asynchronously if an error occurs
   	            // or server returns response with an error status.
   	            $rootScope.ValidationMessage="Erreur lors du traitement du fichier, verifiez le format!";
  	            console.log("Erreur lors du traitement du fichier "+ response.message);
  	            console.log(response);
  	            })
            })

        function errorCallback(response) {
   	            // called asynchronously if an error occurs
   	            // or server returns response with an error status.
   	            $rootScope.ValidationMessage="Erreur lors de l'envoie du fichier veuillez réessayer!";
  	            console.log("Erreur lors de l'envoie du fichier "+ response.message);
  	            console.log(response);
  	            }
        }
    }]);




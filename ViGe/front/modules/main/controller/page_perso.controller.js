var app = angular.module('ViGeFront.main.controllers', ['ui.bootstrap']);

app.controller('page_perso', page_persoCtrl);

var page_persoCtrl = function($scope,$http,$rootScope) {


    /*demande au serveur les fileReadable pour l'user*/

    $scope.fileReadable=function(){

		/*envoie au serveur une annotation et le dict*/
    	$http({
    	method: 'GET',
    	url: '/api/v0/getfileReadpermited/'
    	}).then(function successCallback(response) {
		    // this callback will be called asynchronously
		    // when the response is available
		    console.log(response.data);
		    $scope.tree=response.data;
  		},
    	function errorCallback(response) {
   		    // called asynchronously if an error occurs
   		    // or server returns response with an error status.
  		    console.log("Erreur lors de la tentative de mise à jour de l'arbre");
  		    console.log(response);
  		    })

    };

    /*demande au serveur les fileOwned par l'user*/

    $scope.fileReadable=function(file){
    /*remplace rootScope.data par le dictionnaire du fichier*/
    $rootScope.data=data

    console.log(userChoice)

		/*envoie au serveur une annotation et le dict*/
    	$http({
    	method: 'GET',
    	url: '/api/v0/getfileReadpermited/'
    	}).then(function successCallback(response) {
		    // this callback will be called asynchronously
		    // when the response is available
		    console.log(response.data);
		    $scope.tree=response.data;
  		},
    	function errorCallback(response) {
   		    // called asynchronously if an error occurs
   		    // or server returns response with an error status.
  		    console.log("Erreur lors de la tentative de mise à jour de l'arbre");
  		    console.log(response);
  		    })

    };


}
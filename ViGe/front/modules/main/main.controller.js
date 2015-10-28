var app = angular.module('ViGeFront.main.controllers', []);

var mainCtrl = function($scope,$http) {

	/*(re)initialise les variables au chargement de la vue et lors d'une nouvelle recherche*/
	$scope.reset=function(){
		$scope.index = ' Veuillez cliquer sur un element # du tableau';
		$scope.sequenceRef = '';
		$scope.sequencePat = '';
		$scope.sequenceDbSNP='';
		$scope.chromosome = '';
		$scope.rangeSeqPol='';
		$scope.strand='';
		$scope.annotation='';
		$scope.results=""
		};


	/*envoie au serveur les inputs via l'URL*/
	$scope.sendData=function(data){
	    $http({
  		method: 'GET',
  		url: 'api/v0/uploadURL/'+data+'/'
		}).then(function successCallback(response) {
			// this callback will be called asynchronously
			// when the response is available
			console.log(response.data);
			$scope.results=response;
  			},

  			function errorCallback(response) {
    		// called asynchronously if an error occurs
    		// or server returns response with an error status.
  			console.log("Erreur lors de l'envoie des données");
  			console.log(response);
  			})
  		};

	/*modifie la fenetre polymorphisme*/
	$scope.modifyPolWin=function(index, item){
		$scope.index =index;
		$scope.sequenceRef=item.sequence;
		$scope.sequencePat=item.sequence.substring(0,9)+'─'+item.sequence.substring(10,21)
		$scope.sequenceDbSNP=item.sequenceDbSNP;
		$scope.rangeSeqPol= item.start-9+'-'+(10+item.start);
		$scope.chromosome = item.chromosome;
		$scope.annotation = item.annotation;
		$scope.strand=item.strand;
	};

};


app.controller('mainCtrl', mainCtrl);

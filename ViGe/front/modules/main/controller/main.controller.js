var app = angular.module('ViGeFront.main.controllers', ['ui.bootstrap']);



var mainCtrl = function($scope,$http,$modal,$rootScope) {

	/*(re)initialise les variables au chargement de la vue et lors d'une nouvelle recherche*/
	$scope.reset=function(){
		$scope.index = ' Veuillez cliquer sur un element # du tableau';
		$scope.sequenceRef = '';
		$scope.sequencePat = '';
		$scope.sequenceDbSNP='';
		$scope.sequenceProtein='';
		$scope.chromosome = '';
		$scope.rangeSeqPol='';
		$scope.strand='';
		$scope.annotation='';
		$scope.results= '';
	};

	$scope.results=$rootScope.results


	/*modifie la fenetre polymorphisme*/
	$scope.modifyPolWin=function(index, item){
		$scope.index =index;
		$scope.sequenceRef=item.sequence;
		$scope.sequencePat=item.sequence.substring(0,9)+'─'+item.sequence.substring(10,22)
		$scope.sequenceDbSNP=item.sequenceDbSNP;
		//$scope.sequenceProtein=item.seqProt;
		$scope.rangeSeqPol= item.start-9+'-'+(9+item.start); // verifier infos
		$scope.chromosome = item.chromosome;
		$scope.annotation = item.annotation;
		$scope.strand=item.strand;
	};

	$scope.open = function () {
		console.log('yes');
    	var modalUpload = $modal.open(
    		{
    		templateUrl: '/front/modules/main/html/upload.html',
    		controller:'uploadController',
    		}
    	);
  	};
};





app.controller('mainCtrl', mainCtrl);





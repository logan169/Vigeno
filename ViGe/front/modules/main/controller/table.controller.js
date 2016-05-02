var app = angular.module('ViGeFront.main.controllers');

app.controller('tableController', function( $modal, $modalInstance, $scope,$rootScope,$window) {

  $scope.strand_mutation = $rootScope.column.strand_mutation;
  $scope.start_mutation = $rootScope.column.start_mutation;
  $scope.end_mutation = $rootScope.column.end_mutation;
  $scope.chromosome = $rootScope.column.chromosome;
  $scope.strand = $rootScope.column.strand;
  $scope.start = $rootScope.column.start;
  $scope.end = $rootScope.column.end;
  $scope.length = $rootScope.column.length;
  $scope.frame = $rootScope.column.frame;
  $scope.CDS_start = $rootScope.column.CDS_start;
  $scope.CDS_end = $rootScope.column.CDS_end;
  $scope.CDS_length = $rootScope.column.CDS_length;
  $scope.gene_name = $rootScope.column.gene_name;
  $scope.gene_id = $rootScope.column.gene_id;
  $scope.transcript_name = $rootScope.column.transcript_name;
  $scope.transcript_id = $rootScope.column.transcript_id;
  $scope.id = $rootScope.column.id;
  $scope.number = $rootScope.column.number;
  $scope.protein_name = $rootScope.column.protein_name;
  $scope.protein_id = $rootScope.column.protein_id;
  $scope.peptide = $rootScope.column.peptide;
  $scope.group = $rootScope.column.group; 
$scope.sex = $rootScope.column.sex;


  $scope.checkall_checkbox = false;
  $scope.uncheckall_checkbox = false;

  $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
  };

  $scope.checkAll = function(){
    console.log("yee");
    $scope.checkall_checkbox = true;
  };

    $scope.uncheckAll = function(){
    console.log("iii");
    $scope.uncheckall_checkbox = true;
  };

});



'use strict'

var app = angular.module('ViGeFront.main.controllers', ['ui.bootstrap']);

app.controller('mainCtrl',function($scope,$http,$modal,$rootScope,$location,Tree, $anchorScroll){

	/*function that get the width size of the screen to adjust the offset of the id to look for in the function tabscroll in order to center on the position specified*/
	var viewport=function (){
		console.log('viewport');
    	var e = window, a = 'inner';
    	if ( !( 'innerWidth' in window ) ){
    	    a = 'client';
    	    e = document.documentElement || document.body;
    	    }
    	var dict= { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
    	//console.log('width :'+dict.width);
    	//console.log('height :'+dict.heigth);
    	return dict.width
    	};

    var getIdToScrollTo=function(){
    	console.log('getIdToScrollTo');
		// mutation length/2 + start
		var demiLength=Math.round($scope.currentPoly.mutated.normalized.demilength);

		//offset based on screen width
		var offset=Math.round(viewport()/11); // need to measure the right up offset
		console.log('offset :'+offset)


		//output Position is the closest position who %3==0 from (defPos+offset)-2 (starting position)
		//var output=demiLength+offset;
		var output=demiLength;
		while ((output-2)%3!=0){
		    output+=1;
		    console.log(output);
		}
		if (output>$scope.currentPoly.mutated.normalized.end){return $scope.currentPoly.mutated.normalized.end;}

		return ('position_mutation-'+(output));
    }

	/*autoScroll jusqu'a la position == 1/2 de la sequence mutée*/
	var tabScroll = function() {
		console.log('getIdToScrollTo');
		var id=getIdToScrollTo()
		console.log('IdToScrollTo :'+id);


	  		if (document.getElementById(id).scrollIntoView() != null){
	  			document.getElementById(id).scrollIntoView()
	  			}
	  		else{console.log(null)}


    };


    /*ouvre le modal de l'upload*/
    $scope.open = function () {
    var modalUpload = $modal.open({
    	templateUrl: '/front/modules/main/html/upload.html',
    	controller:'uploadController',
    	});
  	};

    /*set result = $rootScope.results*/
    $scope.results=$rootScope.results;

    $scope.currentPoly = {
    	selectedFrame:null,
    	vrai:true,
    	selectedRow:null,
    	layerValue : false,
    	TreeValue : null,
    };

    $scope.changeLayerValue = function(){
    	$scope.currentPoly.layerValue = !$scope.currentPoly.layerValue
    };

    $scope.changeSelectedRow=function(idNumber){
    	console.log($scope.currentPoly.selectedRow);
    	$scope.currentPoly.selectedRow =  idNumber+'-table-row';
    	console.log(idNumber);
    	console.log($scope.currentPoly.selectedRow);
    };

	$scope.splitDna=function(str){
		var codons = [];
		if (str==undefined){return}
		for (var i = 0, charsLength = str.length; i < charsLength; i += 3) {
			codons.push(str.substring(i, i + 3 ));
		};
		//console.log(codons)
		return codons;
	};

	$scope.changeFrameButtonColor = function(value) {
		$scope.currentPoly.selectedFrame=value;
    };

    var getdbSnipSeq=function(chromosome,start,end,ref_strand){
    	$http({
			method: 'GET',
			url: '/api/v0/getDNA&AADBSNIP/'+chromosome+'/'+start+'/'+end+'/'+ref_strand+'/'
			}).then(function successCallback(response) {
				// this callback will be called asynchronously
				// when the response is available

				$scope.currentPoly.allFramesDbSnps=response.data.data
				tabScroll();
				console.log('yes');
				}, function errorCallback(response) {
				// called asynchronously if an error occurs
				// or server returns response with an error status.
				console.log('Noooooo!!!!');
				console.log(response);
				});
		};


	var get6frames=function(seq,ref_strand){
		 console.log(seq,ref_strand)
		 $http({
			method: 'GET',
			url: '/api/v0/getDNA&AA/'+seq+'/'+ref_strand+'/'
			}).then(function successCallback(response) {
				// this callback will be called asynchronously
				// when the response is available
				$scope.currentPoly.allFrames=response.data.data
				//console.log('yes');
				}, function errorCallback(response) {
				// called asynchronously if an error occurs
				// or server returns response with an error status.
				//console.log('Noooooo!!!!');
				console.log(response);
				});
		 };

	var startingStrandAndFrame=function(strand,frame){
		var outputFrame='';
		if (strand=='+'){
			outputFrame+='f';
			outputFrame+=parseInt(frame)+1
		}
		else{
		outputFrame+='r';
			outputFrame+=parseInt(frame)+1
		}
		return outputFrame;
	}

	$scope.Array=function(start,stop){
    	var output=Array(0);
    	for (var i=2;i<(stop+1-start);i+=3){
    	        output.push(i);
    	};
    	$scope.currentPoly.Array= output;
    	return output;
	};

	$scope.range=function(item,start,end){
		if (item>=start) {
			if (item>=end){
			//console.log(item,start,end,true)
			return false}
			return true;
			}
		else{
			//console.log(item,start,end,false)
			return false;
		}
	};

	/*modifie la fenetre polymorphisme*/
	$scope.modifyPolWin=function(index, item){
		$scope.currentPoly = {

			vrai:true,
			index :index,
			strand : item.strand,
			start : item.start,
			chromosome:item.chromosome,
			end : item.end,
			frame : item.frame,
			peptide : item.peptide,
			seq : item.sequence,
			length:item.length,
			gene:{
				id:item.gene_id,
				name:item.gene_name,
			},
			transcript:{
				name:item.transcript_name,
				id:item.transcript_id
			},
			exon_id:item.id,
			protein:{
				name:item.protein_name,
				id:item.protein_id
			},
			mutated:{
				start:item.start_mutation,
				end:item.end_mutation,
				length:item.end_mutation-item.start_mutation,
				normalized:{
					start:item.start_mutation-item.start,
					end:(item.start_mutation-item.start)+(item.end_mutation-item.start_mutation),
					demilength:(item.end_mutation-item.start_mutation)/2+(item.start_mutation-item.start),
				}
			}
		}

		console.log($scope.currentPoly.mutated.normalized.start,$scope.currentPoly.mutated.normalized.end,$scope.currentPoly.mutated.length,$scope.currentPoly.mutated.normalized.demilength)
		get6frames($scope.currentPoly.seq,$scope.currentPoly.strand);
		getdbSnipSeq(item.chromosome,item.start,item.end,$scope.currentPoly.strand);//modifier code pour obtenir dbsnp filter
		$scope.currentPoly.selectedFrame=startingStrandAndFrame(item.strand, item.frame);
	};

    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////////////////////////

	/*reset table*/
	var rstTab=function(){
		document.getElementById('visRow').innerHTML='';
		}

    /*modifie la fenetre de l'arbre*/
	$scope.modifyTree=function(userChoice){
		$scope.tree ='';
		console.log(userChoice)
		console.log(!$scope.currentPoly.layer,$scope.currentPoly.TreeValue)

		if (!$scope.currentPoly.layerValue || !$scope.currentPoly.TreeValue){
			console.log('yeayea')
			/*envoie au serveur une annotation et le dict*/
    		$http({
    		method: 'GET',
    		url: '/api/v0/modifyTree/'+userChoice+'/'
    		}).then(function successCallback(response) {
			    // this callback will be called asynchronously
			    // when the response is available
			    console.log(response.data.data);
			    $scope.tree=response.data.data;
			    $scope.currentPoly.TreeValue = userChoice
			    rstTab();
			    Tree.makeNewTree(response.data.data);
  				},

    		function errorCallback(response) {
   			    // called asynchronously if an error occurs
   			    // or server returns response with an error status.
  			    //console.log("Erreur lors de la tentative de mise à jour de l'arbre");
  			    console.log(response);
  			    })
    		}

    	else if($scope.currentPoly.layerValue){
    		/*Ajoute un calque à l'arbre*/

			console.log('yoyoya')
			$scope.tree ='';
			console.log(userChoice, $scope.currentPoly.TreeValue)

			/*envoie au serveur une annotation et le dict*/
    		$http({
    		method: 'GET',
    		url: '/api/v0/addTreeLayer/'+$scope.currentPoly.TreeValue+'/'+userChoice+'/'
    		}).then(function successCallback(response) {
			    // this callback will be called asynchronously
			    // when the response is available
			    console.log(response.data.data);
			    $scope.tree = response.data.data;
			    rstTab();
			    Tree.makeNewTree(response.data.data);
  			},

    		function errorCallback(response) {
   			    // called asynchronously if an error occurs
   			    // or server returns response with an error status.
  			    //console.log("Erreur lors de la tentative de mise à jour de l'arbre");
  			    console.log(response);
  			    })
    		}
    	else{}
    	}
});




app.service('Tree', function(){

this.makeNewTree=function(input){


//************************************************************functions************************************************
function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
	  links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) {d.y = d.depth * 100;});

  // Update the nodes…
  var node = svg.selectAll("g.node")
	  .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
	  .attr("class", "node")
	  .attr("transform", function(d) { return "translate(" + source.x + "," + source.y + ")"; })
	  .on("click", click);

  nodeEnter.append("circle")
	  .attr("r", 1e-6)
	  .style("fill", function(d) {return d._children ? "lightsteelblue" : "#fff"; });

  nodeEnter.append("text")
	  .attr("y",  function(d) {return d.children || d._children ?  -15: 25;})
	  .attr("x", function(d) { return d.children || d._children ? 10 : 0;})
	  .attr("text-anchor", 'middle')
	  .style("font-size",15)
	  .text(function(d) {if (d.parent == 'null'){return 'Tree : '+d.name+' / '+'Layer : '+d.layer; } else{return d.name;}})
	  .style("fill", function(d) {return d._children ? "black":"blue"; })
	  .style("fill-opacity", 1);

  nodeEnter.append("text")
	  .attr("y", 25)
	  .attr("x", 0)
	  .attr("text-anchor", 'middle')
	  .text(function(d) {if (d.children_length ){return d.children_length}})
	  .style("font-weight", 'bold')
	  .style("fill", 'black')
	  .style("fill-opacity", 1);


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });


  nodeUpdate.select("circle")
	  .attr("r" , 10)                   // modifie le rayon des noeuds lorsque les noeud ss jacents sont absorbés
	  .style("fill" , function(d) { return d.color} )           // change la couleur des noeuds


  nodeUpdate.select("text")
	  .style("fill-opacity", 1);

  nodeUpdate.select("text")
	  .style("fill-opacity", 1);

  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
	  .remove();

  nodeExit.select("circle")
	  .attr("r", 1e-6);

  nodeExit.select("text")
      .style("fill-opacity", 1e-6);

  nodeExit.select("text.s")
      .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
	  .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
	  .attr("class", "link")
	  .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	  });


  // Transition links to their new position.
  link.transition()
	  .duration(duration)
	  .attr("d", diagonal);


  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
	  .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	    })
	  .remove();


	  // Stash the old positions for transition.
  nodes.forEach(function(d) {
	d.x0 = d.x;
	d.y0 = d.y;
  });

}

// Toggle children on click.
function click(d) {
  if (d.children) {
	d._children = d.children;
	d.children = null;
  } else {
	d.children = d._children;
	d._children = null;
  }
  update(d);
}

// ************** Generate the tree diagram	 *****************
var margin = {top: 30, right: 10, bottom: 30, left: 10},
	width = 1500 - margin.right - margin.left,
	height = 1500 - margin.top - margin.bottom;

var i = 0,
	duration = 300,
	root;

var tree = d3.layout.tree()
	.size([height, width]);

var diagonal = d3.svg.diagonal()
 .projection(function(d) { return [d.x, d.y]; });

var svg = d3.select("#visRow").append("svg")
	.attr("width", width + margin.right + margin.left)
	.attr("height", height + margin.top + margin.bottom)
    .append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

root = input[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);
	}
});



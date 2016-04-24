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


	var get6frames=function(seq,ref_strand,frame){
		 console.log(seq,ref_strand)
		 $http({
			method: 'GET',
			url: '/api/v0/getDNA&AA/'+seq+'/'+ref_strand+'/'+frame
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

	$rootScope.column={
		strand_mutation : true,
		start_mutation : true,
		end_mutation : false,
		chromosome : true,
		strand : true,
		start : false,
		end : false,
		length : false,
		frame : true,
		CDS_start : false,
		CDS_end : false,
		CDS_length : false,
		gene_name : true,
		gene_id : false,
		transcript_name : true,
		transcript_id : false,
		id : false,
		number : false,
		protein_name : true,
		protein_id : false,
		peptide : true,
		group : false
	}

	/*modifie les colonnes du tableau*/
	$scope.modifyTableColumn = function (){
    var modalUpload2 = $modal.open({
    	templateUrl: '/front/modules/main/html/tableColumn.html',
    	controller:'tableController',
    	});
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
		get6frames($scope.currentPoly.seq,$scope.currentPoly.strand,$scope.currentPoly.frame);
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

			//console.log('yoyoya')
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


//*********************************************************************************************************************
//pie

function drawPie(d) {
  d3.select(this)
    .selectAll('path')
    .data(pie(d.pie))
    .enter()
    .append('path')
    .attr('d', arc)
    .attr('fill', function(d){return d.data.color;})
    .attr('stroke','black')
    .attr('stroke-width', function(d) { return d.data.value == 0 ? 0: 0.5;})
    }

    var w = 100;
    var h = 60;
    var i = 0;


    var tree = d3.layout.tree()
      .nodeSize([w + 10, h + 20])
      .separation(function(a, b) {
        return (a.parent == b.parent ? 1 : 1.5);
      });

    var diagonal = d3.svg.diagonal()
      .projection(function(d) {
        return [d.x, d.y];
      });

    var vis = d3.select("body").append("svg:svg")
      .attr("width", 500)
      .attr("height", 500)
      .append("svg:g")
      .attr("transform", "translate(" + 250 + "," + 30 + ")");

    function toggleAll(d) {
      if (d.children) {
        d.children.forEach(toggleAll);
        toggle(d);
      }
    }

    var arc = d3.svg.arc()
      .outerRadius(10)
      .innerRadius(0);

    var pie = d3.layout.pie()
      .value(function(d) {
        return d.value;
      })
      .sort(null);


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


var div = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

  nodeEnter
     .each(drawPie)
     .on("mouseover", function(d) {

             div.transition()
                 .duration(200)
                 .style("opacity", 1);
             div.html(d.name)
                 .style("left", (d3.event.pageX) + "px")
                 .style("top", (d3.event.pageY - 28) + "px");
             })
     .on("mouseout", function(d) {
             div.transition()
                 .duration(500)
                 .style("opacity", 0);
                 })
     .append('circle')
     .attr('r',function(d){return d.children_length==0? 0:11})
     .style('fill',function(d){return d.pie.length==0 ? '#3182bd':'none'})
     .style('stroke',function(d){return d.children_length==0? 'none':'black'})
     .style('stroke-width',0.9) // la width du cercle peut etre modifiee au besoin pour refleter
     .on("mouseover", function(d) {

             div.transition()
                 .duration(200)
                 .style("opacity", 1);
             div.html(d.name)
                 .style("left", (d3.event.pageX) + "px")
                 .style("top", (d3.event.pageY - 28) + "px");
             })
     .on("mouseout", function(d) {
             div.transition()
                 .duration(500)
                 .style("opacity", 0);
                 })

  nodeEnter
     .append('rect')
     .attr("x", -10)
     .attr("y", -10)
     .attr("width", 20)
     .attr("height", 20)
     .style('fill', function(d){if (root.layer == 'null'){return d.children_length==0 ? '#fee0d2':'none'}else{return d.children_length==0 ? d.color:'none'}})
     .style('stroke',function(d){return d.children_length==0 ? 'black':'none'})
     .on("mouseover", function(d) {

             div.transition()
                 .duration(200)
                 .style("opacity", 1);
             div.html(d.name)
                 .style("left", (d3.event.pageX) + "px")
                 .style("top", (d3.event.pageY - 28) + "px");
             })
     .on("mouseout", function(d) {
             div.transition()
                 .duration(500)
                 .style("opacity", 0);
                 });


  nodeEnter.append("text")
	  .attr("y",  function(d) {return d.children_length != 0 ?  -15: 5;})
	  .attr("x", function(d) { return d.children_length !=0 ? 2 : 0;})
	  .attr("text-anchor", 'middle')
	  .style("font-size",15)
	  .text(function(d) {if (d.parent == 'null'){return d.name.charAt(0).toUpperCase() + d.name.slice(1) } else{if (String(d.name).length<9 && String(d.name).length !=8 ){return d.name;}}})
	  .style('font-weight','bold')
	  .style("fill-opacity", 1);

  nodeEnter.append("text")
	  .attr("y", 25)
	  .attr("x", 0)
	  .attr("text-anchor", 'middle')
	  .text(function(d) {if (d.children_length ){return d.children_length}})
	  .style("font-weight", 'bold')
	  .style("fill", 'black')
	  .style("fill-opacity", 1);

  nodeEnter.on("dblclick",function(d){
    	console.log(d.name+'-table-row');
    	if (document.getElementById(d.name+'-table-row').scrollIntoView() != null){
 		  document.getElementById(d.name+'-table-row').scrollIntoView()
 		  changeSelectedRow( 1+d.name)
 		  }
 		else{
 		  changeSelectedRow( 1+d.name)
 		  };


 		    });

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

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


  //add title box

  box.append('rect')
     .attr("x", 50)
     .attr('y',-25)
     .attr("width", 300)
     .attr("height", function(d){return root.layer == 'null'? 40:65})
     .style('fill', '#fee0d2')
     .style('stroke','black')

  box.append("text")
     .attr("x", 75)
     .attr('y',0)
	 .text(function (){ return 'Tree : '+root.name.toUpperCase();})
	 .style("font-weight", 'bold')
	 .style("fill-opacity", 1);

  box.append("text")
     .attr("x", 75)
     .attr('y',25)
	 .text(function (){ if (root.layer != 'null'){return 'Layer : '+root.layer.toUpperCase();}})
	 .style("font-weight", 'bold')
	 .style("fill-opacity", 1);

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
    .attr("width", '100%')
    .attr("height", '100%')
    .attr('viewBox','0 0 '+Math.min(width,height)+' '+Math.min(width,height))
    .attr('preserveAspectRatio','xMinYMin')
    .append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  var box = svg.append("g")

root = input[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);
	}
});



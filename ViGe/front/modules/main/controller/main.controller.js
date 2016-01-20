var app = angular.module('ViGeFront.main.controllers', ['ui.bootstrap']);

app.controller('mainCtrl',function($scope,$http,$modal,$rootScope,$sce){
    /*ouvre le modal de l'upload*/
    $scope.open = function () {
    var modalUpload = $modal.open({
    	templateUrl: '/front/modules/main/html/upload.html',
    	controller:'uploadController',
    	});
  	};

    /*set result = $rootScope.results*/
    $scope.results=$rootScope.results

    /*(re)initialise les variables au chargement de la vue et lors d'une nouvelle recherche*/
    $scope.reset=function(){
        $scope.strand_mutation='';
        $scope.start_mutation='';
        $scope.end_mutation='';
        $scope.chromosome='';
        $scope.strand='';
        $scope.start='';
        $scope.end='';
        $scope.length='';
        $scope.frame='';
        $scope.CDS_start='';
        $scope.CDS_end='';
        $scope.CDS_length='';
        $scope.gene_name='';
        $scope.gene_id='';
        $scope.transcript_name='';
        $scope.transcript_id='';
        $scope.id='';
        $scope.number='';
        $scope.protein_name='';
        $scope.protein_id='';
        $scope.peptide='';
        $scope.sequence='';
        };

  	    //colorie une sequence d'ADN en fonction de ses codons
  	    $scope.changeColorADN=function(str,readingFrame){
  	        var codons = [];
    		outputStr='';
    		outputStr+='<font style="background-color:yellow;">'+str.substring(0,readingFrame)+'</font>';

			for (var i = 0, charsLength = str.length; i < charsLength; i += 3) {
    			codons.push(str.substring(i+readingFrame, i + 3 +readingFrame));
				};

    		for (var element=0, listeLength=codons.length; element<listeLength; element++){
        	    if (element%2==0){
        		outputStr+='<font style="background-color:red;"><span>';
        		outputStr+= (codons[element]);
        	    outputStr+= '</span></font>';
        	    }
        	else{
        	    outputStr+='<font style="background-color:yellow;">';
        		outputStr+= (codons[element]);
        	    outputStr+= '</font>' ;
        		}
    		};
    		return(outputStr);
    	};

    	//colorie une sequence d'ADN en fonction de ses codons
  	    $scope.changeColorAA=function(str,readingFrame){
  	    	dictAA={'F':'lime','L':'cyan','M':'cornflowerblue','*':'red','V':'yellow','I':'green','S':'coral','P':'burlywood','T':'mediumpurple','A':'lightpink','Y':'brown','H':'orange','Q':'mediumturquoise','N':'olive','K':'palegreen','D':'palegoldenrod','E':'royalblue','W':'seashell','C':'slategrey','R':'tomato','G':'salmon'};
    		outputStr='';
    		outputStr+='<font style="background-color:white;"><span1></span1></font>'.repeat(readingFrame)
    		for (var element=0, listeLength=str.length; element<listeLength; element++){
        		outputStr+='<font style="background-color:'+dictAA[str[element]]+'";><span>';
        		outputStr+= (str[element]);
        	    outputStr+= '</span></font>';
        	    };
    		return(outputStr);
    	};

    	$scope.get6frameslist=function(seq){
			 $http({
			 	method: 'GET',
			 	url: '/api/v0/getDNA&AA/'+seq+'/'
				}).then(function successCallback(response) {
					// this callback will be called asynchronously
					// when the response is available
					$scope.seqTrad=response.data.data
					$scope.trustedHtml00=$sce.trustAsHtml($scope.changeColorADN($scope.seqTrad[0][0],0));
            		$scope.trustedHtml10=$sce.trustAsHtml($scope.changeColorADN($scope.seqTrad[1][0],1));
            		$scope.trustedHtml20=$sce.trustAsHtml($scope.changeColorADN($scope.seqTrad[2][0],2));
            		$scope.trustedHtml30=$sce.trustAsHtml($scope.changeColorADN($scope.seqTrad[3][0],0));
            		$scope.trustedHtml40=$sce.trustAsHtml($scope.changeColorADN($scope.seqTrad[4][0],1));
            		$scope.trustedHtml50=$sce.trustAsHtml($scope.changeColorADN($scope.seqTrad[5][0],2));

            		$scope.trustedHtml01=$sce.trustAsHtml($scope.changeColorAA($scope.seqTrad[0][1],0));
            		$scope.trustedHtml11=$sce.trustAsHtml($scope.changeColorAA($scope.seqTrad[1][1],1));
            		$scope.trustedHtml21=$sce.trustAsHtml($scope.changeColorAA($scope.seqTrad[2][1],2));
            		$scope.trustedHtml31=$sce.trustAsHtml($scope.changeColorAA($scope.seqTrad[3][1],0));
            		$scope.trustedHtml41=$sce.trustAsHtml($scope.changeColorAA($scope.seqTrad[4][1],1));
            		$scope.trustedHtml51=$sce.trustAsHtml($scope.changeColorAA($scope.seqTrad[5][1],2));
					//console.log('yes');
					}, function errorCallback(response) {
					// called asynchronously if an error occurs
					// or server returns response with an error status.
					//console.log('Noooooo!!!!');
					console.log(response);
					});
			 };

		$scope.startingStrandAndFrame=function(strand,frame){
			outputFrame='';
			if (strand=='+'){
				outputFrame+='f'
			}
			else{
				outputFrame+='r'
			}
			outputFrame+=parseInt(frame)+1
			console.log(outputFrame)
			document.getElementById(outputFrame).click();
		}

        /*modifie la fenetre polymorphisme*/
        $scope.modifyPolWin=function(index, item){
            $scope.index =index;
            $scope.strand_mutation=item.strand_mutation;
            $scope.start_mutation=item.start_mutation;
            $scope.end_mutation=item.end_mutation;
            $scope.chromosome=item.chromosome;
            $scope.strand=item.strand;
            $scope.start=item.start;
            $scope.end=item.end;
            $scope.length=item.length;
            $scope.frame=item.frame;
            $scope.CDS_start=item.CDS_start;
            $scope.CDS_end=item.CDS_end;
            $scope.CDS_length=item.CDS_length;
            $scope.gene_name=item.gene_name;
            $scope.gene_id=item.gene_id;
            $scope.transcript_name=item.transcript_name;
            $scope.transcript_id=item.transcript_id;
            $scope.id=item.id;
            $scope.number=item.number;
            $scope.protein_name=item.protein_name;
            $scope.protein_id=item.protein_id;
            $scope.peptide=item.peptide;
            $scope.seq=item.sequence;
            $scope.list6frames=$scope.get6frameslist($scope.seq);
            $scope.startingStrandAndFrame($scope.strand,$scope.frame);
            };

    /////////////////////////////////////////////////////////////////////////////////////////////////

    /*modifie la fenetre de l'arbre*/
	$scope.modifyTree=function(userChoice, Tree){
		$scope.tree ='';
		console.log(userChoice)

		/*envoie au serveur une annotation et le dict*/
    	$http({
    	method: 'GET',
    	url: '/api/v0/modifyTree/'+userChoice+'/'
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
});




app.factory('Tree', function(){

function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
	  links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 180; });

  // Update the nodes…
  var node = svg.selectAll("g.node")
	  .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
	  .attr("class", "node")
	  .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
	  .on("click", click);

  nodeEnter.append("circle")
	  .attr("r", 1e-6)
	  .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeEnter.append("text")
	  .attr("x", function(d) { return d.children || d._children ? -13 : 13; })
	  .attr("dy", ".35em")
	  .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
	  .text(function(d) { return d.name; })
	  .style("fill-opacity", 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  nodeUpdate.select("circle")
	  .attr("r", 10)
	  .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeUpdate.select("text")
	  .style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
	  .remove();

  nodeExit.select("circle")
	  .attr("r", 1e-6);

  nodeExit.select("text")
	  .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
	  .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
	  .attr("class", "link")
	  .attr("d", function(d) {
		var o = {x: source.x0, y: source.y0};
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
var margin = {top: 20, right: 120, bottom: 20, left: 120},
	width = window.innerWidth - margin.right - margin.left,
	height = window.innerHeight - margin.top - margin.bottom


var i = 0,
	duration = 750,
	root;

var tree = d3.layout.tree()
	.size([height, width]);

var diagonal = d3.svg.diagonal()
	.projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("#visRow").append("svg")
	.attr("width", width + margin.right + margin.left)
	.attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("viewBox", "0 0 " + width + " " + height )
    .attr("preserveAspectRatio", "xMidYMid meet")
    .attr("pointer-events", "all")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


root = $scope.results[0];
console.log(root)
root.x0 = height / 2;
root.y0 = 0;

update(root);



});

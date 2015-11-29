var app = angular.module('ViGeFront.main.controllers', ['ui.bootstrap']);



var mainCtrl = function($scope,$http,$modal,$rootScope,rapido) {

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
    	var modalUpload = $modal.open(
    		{
    		templateUrl: '/front/modules/main/html/upload.html',
    		controller:'uploadController',
    		}
    	);
  	};

};

app.factory('rapido',function(){

	return{
  	'message': 'ok',
  	'error': false,
  	'data':{
  		'1': {
  		'message': 'ok',
  		 'data': {
  		 	'CDS_start': null,
  		 	 'chromosome': '6',
  		 	  'sequence': 'TTCCCCACGCATCTGAGGG',
  		 	  'frame': null, 'number': 4,
  		 	   'sequenceDbSNP': 'TTCCCCACGCATCTGAGGG',
  		 	    'CDS_length': null, 'seqProt': 'N/A',
  		 	     'protein': null,
  		 	      'transcript': 'FLOT1-011',
  		 	      'CDS_end': null,
  		 	       'strand': '-',
  		 	       'end': 30698342, 'id': 'ENSE00003564703',
  		 	        'start': 30698204, 'length': 138,
  		 	         'genome': 'GRCh37.75',
  		 	          'annotation': 'Exon',
  		 	           'gene': 'FLOT1'},
  		 	            'error': false},
 		 '0': {
 		 	'message': 'ok',
 		 	 'data': {
 		 	 	'CDS_start': 3405547,
 		 	 	 'chromosome': '2',
 		 	 	  'sequence': 'GGTGAAAAAGCTGCAGCAA',
 		 	 	   'frame': 0,
 		 	 	    'number': 2,
 		 	 	     'sequenceDbSNP': 'GGTGAAAAAGCTGCAGCAA',
 		 	 	      'CDS_length': 117,
 		 	 	       'seqProt': 'MEDAGGGEETPAPEAP/LHPPQ/K/*/ELA/TPPEEQGLLFQEETIDLGGDEFGSEENK/ETASEGSSPLADKLNEHMMESVLISDSPNSEGDAGDLGRVRDEAEPGGEGDPGPEPAGTPSPSGEADGDCAPK/EDAAPSSGGAPRQDAAREVPGSEAAH/RPEQEPPVAEPVPVCTIFSQRAPPASGDGFEPQMVKSPSFGGASEASARTPPQVVQPSPSLSTFFGDTAASHSLASDFFDSL/FTTSAFISVSNPGAGSPAP/SASPPPLAVPGTEGRPEPVAMRGPQAAAPPASPEPFAHIQAVFAGSDDPFATALSMS/GEMDRRNDAWLPGEATRGVLRAVATQQRGAVFVDKENLTMPGLRFDNIQGDAVKDLMLRFLGEKAAAKRQVLNADSVEQSFVGLKQLISCRNWRAAVDLCGRLLTAHGQGYS/GKSE/GLLTSHTTDSLQLWFVRLALLVKLGLFQNAEMEFEPFGNLDQPDLYYEYYPHVYPGRRGSMVPFSMRILHAELQQYLGNPQESLDRLHKVKTVCSKILANLEQGLAEDGGMSSVTQEGRQASIRLWRSRLGRVMYSMANCLLLMKDYVLAVEAYHSVIKYYPEQEPQLLSGIGRISLQIGDIKTAEKYFQDVEKVTQKLDGLQGK/EIMVLMNSAFLHLGQNNFAEAHRFFTEILRMDPRNAVANNNAAVCLLYLGKLKDSLRQLEAMVQQDPRHYLHESVLFNLTTMYELESSRSMQKKQALLEAVAGKEGDSFNTQCLKLA',
 		 	 	        'protein': null,
 		 	 	         'transcript': 'TRAPPC12-001',
 		 	 	          'CDS_end': 3405664,
 		 	 	           'strand': '+',
 		 	 	            'end': 3405664,
 		 	 	            'id': 'ENSE00001145941',
 		 	 	             'start': 3405547,
 		 	 	              'length': 117,
 		 	 	               'genome': 'GRCh37.75',
 		 	 	                'annotation': 'Exon',
 		 	 	                 'gene': 'TRAPPC12'},
 		 	 	                  'error': false},
		 '3': {
		 'message': 'ok',
		  'data': {
		  	'CDS_start': 36142145,
		  	 'chromosome': '19',
		  	  'sequence': 'AGCACCATGGCGGAAGACA',
		  	   'frame': 0,
		  	    'number': 1,
		  	     'sequenceDbSNP': 'AGCACCATGGCGGAAGACA',
		  	      'CDS_length': 106,
		  	       'seqProt': 'MAEDMETKIKNYKTAPFDSRFPNQNQTRNCWQNYLDFHRCQKAMTAKGGDISVCEWYQRVYQSLCPTSWVTDWDEQRAEGTFPGKI',
		  	        'protein': null,
		  	         'transcript': 'COX6B1-003',
		  	          'CDS_end': 36142251,
		  	           'strand': '+',
		  	            'end': 36142251,
		  	             'id': 'ENSE00003125961',
		  	              'start': 36142134,
		  	               'length': 117,
		  	                'genome': 'GRCh37.75',
		  	                 'annotation': 'Exon',
		  	                  'gene': 'COX6B1'},
		  	                   'error': false},
		  '2': {
		  'message': 'ok',
		   'data': {
		   	 'CDS_start': 48887293,
		   	  'chromosome': '8',
		   	   'sequence': 'ATCCGCTTAGCAGAAGCCC',
		   	    'frame': 0,
		   	     'number': 14,
		   	      'sequenceDbSNP': 'ATCCGCTTAGCAGAAGCCC',
		   	       'CDS_length': 229,
		   	        'seqProt': 'MSSPASTPSRRGSRRGRATPAQTPRSEDARSSPSQRRRGEDSTSTGELQPMPTSPGVDLQSPAAQDVLFSSPPQMHSSAIPLDFDVSSPLTYGTPSSRVEGTPRSGVRGTPVRQRPDLGSA/SQKGLQVDLQSDGAAAEDIVASEQSLGQKLVIWGTDVNVAACKENFQRFLQRFIDPLAKEEENVGIDITEPLYMQRLGEINVIGEPFLNVNCEHIKSFDKNLYRQLISYPQEVIPTFDMAVNEIFFDH/RYPDSILEHQIQVRPL/FNALKTKNMRNLNPEDIDQLITISGI/MVIRTSQLIPEMQEAFFQCQVCAHTTRVEMDRGC/RIAEPSVCGRCHTTHSMALIHNRSLFSDKQMIKLQESPEDMPAGQTPHTVILFAHNDLVDKVQPGDRVNVTGIYRAVPIRVNPRVSNVKSVYKTHIDVIHYRKTDAKRLHGLDEEAEQKLFSEKRVELLKELSRKPDIYERLASALAPS/TIYEHEDIKKGILLQLFGGTRKDFSHTGRGKFRAEINILLCGDPGTSKSQLLQYVYNLVPRGQYTSGKGSSAVGLTAYVMKDPETRQLVLQTGALVLSDNGICCIDEFDKMNESTRSVLHEVMEQQTLSIAKAGIICQLNARTSVLAAANPIESQWNPKKTTIENIQLPHTLLSRFDLIFLM/LLDPQDEAYDRRLAHHLVALYYQSEEQAEEELLDMAVLKDYIAYAHSTIMPRLSEEASQALIEAYVDMRKIGSSRGMVSAYPRQLESLIRLAEAHAKVRLSNKVEAIDVEEAKRLHREALKQSATDPRTGIVDISILTTGMSATSRKRKEELAEALKKLILSKGKTPALKYQQLFEDIRGQSDIAITKDMFEEALH/RALADDDFLTVTGKTVRLL',
		   	         'protein': null,
		   	          'transcript': 'MCM4-004',
		   	           'CDS_end': 48887522,
		   	            'strand': '+',
		   	             'end': 48887522,
		   	              'id': 'ENSE00003323524',
		   	               'start': 48887293,
		   	                'length': 229,
		   	                 'genome': 'GRCh37.75',
		   	                  'annotation': 'Exon',
		   	                   'gene': 'MCM4'},
		   	                    'error': false}
		   }
  		};
  	});



app.controller('mainCtrl', mainCtrl);


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

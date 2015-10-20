var app = angular.module('ViGeFront.main.controllers', []);

var mainCtrl = function($scope,$http) {
	$scope.items = 'toto';
	$scope.index = ' Veuillez cliquer sur une element # du tableau';
	$scope.sequenceRef = '';
	$scope.sequencePat = '';
	$scope.chromosome = '';
	$scope.rangeSeqPol='';
	$scope.strand='';
	$scope.annotation='';
	$scope.results = {
	   	  'data':
	   	      	[{'CDS_start': 2655029,'chromosome': 'Y','frame': 0,'number': 0,'CDS_length': 615,'protein': null,'transcript': 'SRY-001','CDS_end': 2655644,'strand': '-','id': 'ENSE00001494622','start': 2654895,'length': 845,'genome': 'GRCh37.75','sequence':'GCATGACTAGCACGCAGCAAA','gene': 'SRY','annotation': 'Exon',
	   	      	},{'CDS_start': 2655029,'chromosome': 'Y','frame': 0,'number': 0,'CDS_length': 615,'protein': null,'transcript': 'SRY-001','CDS_end': 2655644,'strand': '-','sequence':'AGCATGACCGCAGCAGCATAA','id': 'ENSE00001494622','start': 2654895,'length': 845,'genome': 'GRCh37.75','annotation': 'Exon','gene': 'SRY',
	   	      	},{'CDS_start': 2655029,'chromosome': 'Y','frame': 0,'number': 0,'CDS_length': 615,'protein': null,'transcript': 'SRY-001','CDS_end': 2655644,'strand': '-','id': 'ENSE00001494622','start': 2654895,'length': 845,'genome': 'GRCh37.75','gene': 'SRY','annotation': 'Exon','sequence':'ATGAAGAGCCTAACGCCAAGC',
	   	      	},{'CDS_start': 3405547, 'sequence':'GCATGACTAGCACGCAGCAAA','chromosome': '2', 'frame': 0, 'number': 2, 'CDS_length': 117, 'protein': null, 'transcript': 'TRAPPC12-001', 'CDS_end': 3405664, 'strand': '+', 'id': 'ENSE00001145941', 'start': 3405547, 'length': 117, 'genome': 'GRCh37.75', 'annotation': 'Exon', 'gene': 'TRAPPC12'
	   	      	},{'CDS_start': 126667390, 'sequence':'GCATGTACTGGCCGCAGCAAA','chromosome': '6', 'frame': 0, 'number': 1, 'CDS_length': 74, 'protein': null, 'transcript': 'CENPW-002', 'CDS_end': 126667464, 'strand': '+',  'id': 'ENSE00001446879', 'start': 126667390, 'length': 74, 'genome': 'GRCh37.75', 'annotation': 'Exon', 'gene': 'CENPW'},
	   	      	],
	   	      	'message': 'ok',
	   	      	'error': false,
	   	      	};

	$scope.modifyPolWin=function(index, item){
		$scope.index =index;
		$scope.sequenceRef=item.sequence;
		$scope.sequencePat=item.sequence.substring(0,10)+'-'+item.sequence.substring(11,22)
		$scope.rangeSeqPol= item.start-10+'-'+(11+item.start);
		$scope.chromosome = item.chromosome;
		$scope.annotation = item.annotation;
		$scope.strand=item.strand;
	};

};

app.controller('mainCtrl', mainCtrl);

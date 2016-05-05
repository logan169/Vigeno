
<script>
/*
Ce script permet d'afficher une nouvelle sous string d'une string mere

output type: ["***end of sequence***atcgtagcg", 0, 9] string fille, new start, new end
*/



var moveSeqRigth=function(str,oldStart,oldEnd){

    newStart=oldStart+37;
    newEnd=oldEnd+37;
    message="***";

    if (newEnd<str.length){
    	newStr= str.substr(newStart,newEnd);
    }
    else{
        newStart=parseInt(str.length)-37;
        newEnd=str.length;
        newStr= str.substr(newStart,newEnd)+message;
    }
    outputlist=[newStr,newStart,newEnd];
    document.getElementById('seq').innerHTML=newStr;
    document.getElementById('seqLength').innerHTML=newStr.length;
    document.getElementById('start').innerHTML=newStart;
    document.getElementById('end').innerHTML=newEnd;
    return (outputlist);

};

//////////////////////////////////////////////////////////////////////


var moveSeqLeft=function(str,oldStart,oldEnd){

    newStart=parseInt(oldStart)-37;
    newEnd=parseInt(oldEnd)-37;
    message="***";

    if (newStart>=0){
    	newStr= str.substr(newStart,newEnd);
    }

    else{
        newStart=0;
        newEnd=37;
        newStr=message+str.substr(newStart,newEnd);
    }

    outputlist=[newStr,newStart,newEnd];
    document.getElementById('seq').innerHTML=newStr;
    document.getElementById('seqLength').innerHTML=newStr.length;
    document.getElementById('start').innerHTML=newStart;
    document.getElementById('end').innerHTML=newEnd;
    return (outputlist);
};

//moveSeqLeft(str,start,end);
//moveSeqRigth(str,start,end);

</script>
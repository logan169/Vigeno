__author__ = 'schwartzl'

import flask
from pyGeno.tools.parsers import CSVTools as C
import common.kernel as K
import common.format as F
import common.Position as Pos
from common.db import printQuerieResults as qc



def parseFile(filename):
    file=C.CSVFile()
    file.parse(filename)
    dict={}
    print str(file)

    x=0
    for line in file :
        print line
        #print line['peptide'],line['start'],line['end'],line['chromosome'],line['strand'],line['ensg'],line['enst']
        dict[x]=[line['peptide'],line['start'],line['end'],line['chromosome'],line['strand'],line['ensg'],line['enst']]
        x+=1
    print dict

    data={}
    y=0 #correspond a l'iterateur d'index du dictionnaire data qui accumule les dictinnaire
    for key in dict:
        #utilise la fonction startPos dans le dossier common, cette fonction prends 3 parametre en entree:
        # startPos(genome,chromosome,position) et renvoie un dict contenant toutes les infos necessaires au client
        #pour cette sequence


        temp=Pos.startPos('GRCh37.75',str(dict[key][3]),int(dict[key][1]))

        """
        temp=qc(int(dict[key][1]),str(dict[key][3]))

        print temp

        exonID=''
        exon={}
        sameExon=True
        for element in temp:

            if exonID=='':
                exonID=element['id']
                for key in element:
                    exon[str(key)]=element[key]
            '''
            print element

            if exonID!=element['id']:
                sameExon=False
                return 'Error position fall in 2 separate regions!'
            '''
        print exon

        if sameExon == True:
            t=K.JSONResponse(exon,False,'ok')

            if t['error']==False:
                data[str(y)]=t
            else:
                data= K.JSONResponse(None,True,'error at line '+str(y)+' in the input file')
        y+=1


        """
        temp= K.JSONResponse(temp,False, 'ok')

        if temp['error']==False:
            data[str(y)]=temp
        else:
            data= K.JSONResponse(None,True,'error at line '+str(y)+' in the input file')
        y+=1

    return data

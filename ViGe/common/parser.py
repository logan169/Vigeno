__author__ = 'schwartzl'

import flask
from pyGeno.tools.parsers import CSVTools as C
import common.kernel as K
import common.format as F
import common.Position as Pos
from common.db import getExons


def parseFile(filename):
    #print filename
    f = C.CSVFile()
    f.parse(filename, separator=",")
    liste=[]

    for line in f :
        liste.append([line['peptide'],line['start'],line['end'],line['chromosome'],line['strand'],line['ensg'],line['enst']])

    data={}
    y=0 #correspond a l'iterateur d'index du dictionnaire data qui accumule les dictinnaire

    retour={}
    for element in liste:
        exons=getExons(int(element[1]),str(element[3]))

        for e in exons:
            eid = e["id"]
            trans = (e["transcript"], e["number"])
            if eid in retour :
                retour[eid]["transcripts"].append(trans)
            else :
                retour[eid] = e
                retour[eid]["transcripts"] = [trans]
                del(retour[eid]["number"])
                del(retour[eid]["transcript"])


    #print retour
    return retour

"""
        exonID=''
        dictexon={}
        sameExon=True
        for element in exons:

            #verifie que les resultats sont redondant (il y a plusieurs numero pour le meme exon)
            if exonID=='':
                exonID=element['id']
                for cle in element:
                    exons[str(cle)]=element[cle]

            '''
            print element

            if exonID!=element['id']:
                sameExon=False
                return 'Error position fall in 2 separate regions!'
            '''
        #print exon

        if sameExon == True:
            t=K.JSONResponse(exon,False,'ok')

            if t['error']==False:
                data[str(y)]=t
            else:
                data= K.JSONResponse(None,True,'error at line '+str(y)+' in the input file')
        y+=1


    return data
"""

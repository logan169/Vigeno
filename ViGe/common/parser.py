__author__ = 'schwartzl'

import flask
from pyGeno.tools.parsers import CSVTools as C
import common.kernel as K
import common.Position as Pos

def parseURL( input_data, separator = '%20'):
    #l'input est une chaine de caracteres sortis de l'URL
    # format: chr1%20pos1%20chr2%20pos2...



    #split l'input en fonction des espaces
    if ' ' in input_data:
        lines=input_data.split(" ")
    #sinon split l'input en fonction du "separator"
    elif separator in input_data:
        lines=input_data.split(separator)
    data={}

    #formate chaque lignes de sorte a faire ressortir le chr et la position
    #format : [chr1,pos1,chr2,pos2,...]

    x=0
    while x < len(lines):
        if lines[x]!='':
            #on regarde si c'est une cle=chr ou une value=pos
            #on utilise le modulo pour associer chaque position a son chromosome
            if x%2==0:
                #verifie si le chromosome (lines[x]) est une cle de data, si oui on append sa liste sinon on cree cette cle
                if lines[x] not in data.keys():
                    data[str(lines[x])]=[]

                #puis on append la liste de ce chromosome pour ajouter la nouvelle position
                try:
                    data[lines[x]].append(int(lines[x+1]))
                except:
                    print ('erreur format')
            x+=1

        #ex format data renvoye
        # {'Y': [2655643,656435],'13':[2556463,365645,564564]}

        #maintenant on utilise le dictionaire file pour iterer sur toutes les values pour chacune des keys en appellant
        # la fonction Position a chaque fois. Au final, le dict data a la forme suivante, chaques sequences de l'input est
        # associees a un index correspondant a un dictionnaire contenant toutes l'info pour cette sequence.
        # IL y a donc une key error et message et une key pour chaque sequence soumise

        #ex d'output
        #{'0': {'message': 'ok', 'data': {'CDS_start': 2655074, 'chromosome': u'Y', 'sequence': 'ATGATTGCATTGTCAAAAA',
        #  'frame': 0, 'number': 0, 'sequenceDbSNP': 'ATGATTGCADTGTCAAAAA', 'CDS_length': 570, 'protein': None,
        #  'transcript': u'SRY-201', 'CDS_end': 2655644, 'strand': u'-', 'end': 2655644, 'id': u'ENSE00002201849',
        #  'start': 2655074, 'length': 570, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'SRY'}, 'error': False}}

        file={}
        x=1 #correspond a l'iterateur d'index du dictionnaire data
        for key in data:
            for value in data[key]:

                #utilise la fonction startPos dans le dossier common, cette fonction prends 3 parametre en entree:
                # startPos(genome,chromosome,position) et renvoie un dict contenant toutes les infos necessaires au client
                #pour cette sequence
                file[str(x)]=Pos.startPos('GRCh37.75',str(key),int(value))
                x+=1

        print file

        return file

def parseFile(filename):

    file=C.CSVFile()
    file.parse(filename)
    dict={}

    x=1
    for line in file :
        #print line['peptide'],line['start'],line['end'],line['chromosome'],line['strand'],line['ensg'],line['enst']
        dict[x]=[line['peptide'],line['start'],line['end'],line['chromosome'],line['strand'],line['ensg'],line['enst']]
        x+=1



    data=K.JSONResponse({},False,None)
    y=1 #correspond a l'iterateur d'index du dictionnaire data qui accumule les dictinnaire
    for key in dict:
        #utilise la fonction startPos dans le dossier common, cette fonction prends 3 parametre en entree:
        # startPos(genome,chromosome,position) et renvoie un dict contenant toutes les infos necessaires au client
        #pour cette sequence
        temp=Pos.startPos('GRCh37.75',str(dict[key][3]),int(dict[key][1]))

        if temp['error']==False:
            data["data"][str(y)]=temp['data']
        else:
            data= K.JSONResponse(None,True,'error at line '+str(y)+' in the input file')
        y+=1

    return data

__author__ = 'schwartzl'

import flask
from pyGeno.tools.parsers import CSVTools as C
import common.kernel as K
import common.format as F
import common.Position as Pos
from common.db import getExons
from db import *
folder_path='/u/schwartzl/py/projetIric/20151223/vige/ViGe/uploads/'

filename='pep_pep_pep.csv'

path=folder_path+filename
print path
#filename='/u/schwartzl/Bureau/fichier_celine_input.tsv'
username='log'

def parseFile(path,filename,username):
    csv = C.CSVFile()
    csv.parse(path,separator=',')

    typs={'chromosome':'string'}
    docLignes=[]

    print csv.legend

    numeroLigne=1
    for ligne in csv[1:len(csv)]:
        docLigne={}
        #print ligne
        for colonne in csv.legend:
            typ=None

            #validation type de la colonne
            try:
                float(ligne[colonne])
                typ = "numeric"
            except:
                typ = "string"

            #validation si type est similaire a cet meme colonne dans les lignes precedentes
            if colonne not in typs:
                typs[colonne]=typ

            else:
                if typs[colonne] != typ and colonne != 'chromosome':
                    message='Type error in ligne '+str(numeroLigne)+' and column '+str(colonne)+':\n'+'ligne '+str(numeroLigne)+':'+str(ligne)
                    print  message
                    return message

            #ajoute l'element de la colonne au dict qui vient de passer la validation de typage dans le docLigne

            docLigne[colonne]=ligne[colonne]

        #ajoute le dict docligne a liste doclignes
        docLignes.append(docLigne)

    #une fois que toutes les lignes ont ete validees, on integre les infos dans les bd:

    # on process chaque ligne et on ajoute le dict de resultat dans File_Content
    for x in range (len(docLignes)):
        augmentedContent=getExons(startPosition=int(docLignes[x]['start']),endPosition=int(docLignes[x]['end']),transcript_id=docLignes[x]['enst'])

        if len(augmentedContent) >0:
            if len(augmentedContent) == 1:
                docLignes[x].update(augmentedContent[0])

                try:
                    addFileContent(filename=filename,line=x,username=username,content=docLignes[x])

                except:
                    message= 'You already own a file with this name, please change the name of the file you are uploading'
                    print message
                    return message
        else:
            print '##########################\n###########Exon not found############# infos :'+str(docLignes[x])+'\n#############################'





    #l'overview dans file_Overview
    addFileOverview(filename=filename,username=username,colonnes=typs)

    #la permission de lire,ecrire,'overview et le file owned dans file_Overview
    modifyPermissionDoc(username=username,fileReadPermission=filename,fileWritePermission=filename,fileOwned=filename)



parseFile(path,filename,username)




from pyGeno.tools.parsers import CSVTools as C
import kernel as K


def parseFile(path,filename,username):

    #parserpyGeno
    csv = C.CSVFile()
    csv.parse(path+filename,separator=',')

    #ici on verifie le type de chaque colonne pour chaque ligne et on accumule l'info dans un \
    # dict , si le test passe le dict est copie dans la bd file_content
    typs={'chromosome':'string'}
    docLignes={}

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
                    return K.JSONResponse(None,True,message)

            #ajoute l'element de la colonne au dict qui vient de passer la validation de typage dans le docLigne
            docLigne[colonne]=ligne[colonne]

        #ajoute le dict docligne a liste doclignes
        docLignes[numeroLigne]=docLigne
        numeroLigne+=1

        outputDoc={'docLignes':docLignes,'filename':filename,'username':username,'typs':typs}
        return K.JSONResponse(outputDoc,False,'file uploaded')

#######################################################################################################################
#une fois que toutes les lignes ont ete validees, on integre les infos dans les bd avec la fonction du fichier
#addDictInDb.py
#######################################################################################################################



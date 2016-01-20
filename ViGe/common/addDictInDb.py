#######################################################################################################################
#une fois que toutes les lignes ont ete validees, on integre les infos dans les bd avec la fonction du fichier
#addDictInDb.py
#######################################################################################################################
#################Ce script recupere le dict produit par le fichier parser et integre ses elements a la bd
######################################################################################################################


from db import getExons,addFileOverview,modifyPermissionDoc,addFileContent
import kernel as K




def addDictInDb(docLignes,filename,username,typs):

    #cree un fichier pour noter tout les exons n'ayant pas ete trouves dans la bd
    ExonsNotFound=open('ExonsNotFound.txt','a')

    # on process chaque lignes et on ajoute le dict de resultat dans File_Content
    for x in range (1,len(docLignes)):

        augmentedContent=getExons(startPosition=int(docLignes[x]['start']),endPosition=int(docLignes[x]['end']),transcript_id=docLignes[x]['enst'])
        if len(augmentedContent)>0:
            if len(augmentedContent)==1:
                docLignes[x]['start_mutation']=docLignes[x]['start']
                docLignes[x]['end_mutation']=docLignes[x]['end']
                docLignes[x]['strand_mutation']=docLignes[x]['strand']
                docLignes[x].update(augmentedContent[0])


                try:
                    addFileContent(filename=filename,line=x,username=username,content=docLignes[x])
                except:
                    message= 'You already own a file with this name, please change the name of the file you are uploading'
                    return K.JSONResponse(None,True,message)
        else:
            ExonsNotFound.write(str(docLignes[x])+'\n')

    ExonsNotFound.close()

    #l'overview dans file_Overview
    addFileOverview(filename=filename,username=username,colonnes=typs)
    #la permission de lire,ecrire,'overview et le file owned dans file_Overview
    modifyPermissionDoc(username=username,fileReadPermission=filename,fileWritePermission=filename,fileOwned=filename)



    return K.JSONResponse(docLignes,False,'augmented content for this file is now in db')










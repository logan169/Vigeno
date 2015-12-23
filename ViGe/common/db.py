# -*- coding: utf-8 -*-

import hashlib, uuid
from pyArango.connection import *
import time


###############################################################"
##mdp
###############################################################

#create a salt
def newSalt():
    return uuid.uuid4().hex

#hash mdp avec le salt
def mdp_hash(mdp,salt):
    return hashlib.sha512(mdp + salt).hexdigest()

###############################################################"
##db
###############################################################
conn = Connection()

#Creation/initialisation des collections
try :
    l
except:
    db=conn["ViGe"]

try:
    usersCollection= db.createCollection(name = "Users")
except:
    usersCollection=db["Users"]

try:
    annotationCollection=db.createCollection(name="Exon")
except:
    annotationCollection=db["Exon"]

try:
    fileCollection=db.createCollection(name='File')
except:
    fileCollection=db["File"]

try:
    permissionCollection=db.createCollection(name='Permissions')
except:
    permissionCollection=db['Permissions']


#######################################################################################################################
##fonction pour manipuler toutes les  bd
#######################################################################################################################





#print querie results:
def getExons(startPosition,chromosome):


    bindVars={
        'startPosition':startPosition,
        'chromosome':chromosome,
        }

    aql = """
    FOR c IN Exon
        FILTER  c.start <= @startPosition && c.end >= @startPosition && c.chromosome==@chromosome
        RETURN c
    """



    # by setting rawResults to True you'll get dictionaries instead of Document objects, useful if you want to result to set of fields for example
    queryResult = db.AQLQuery(aql, rawResults = True, batchSize = 100, bindVars = bindVars)

    return queryResult

#########################################################################
# pour bd User
#########################################################################
#add a new user infos to the data bank
def addUser(username,mdp,mail):

    try:
        doc=usersCollection.createDocument()
        doc._key=str(username)
        doc['username'] = str(username)
        doc['salt'] = str(newSalt())
        doc['mdp'] = str(mdp_hash(str(mdp),doc['salt']))
        doc['mail'] = str(mail)
        doc['fileOwned']={}
        doc['fileReadPermission']={}
        doc.save()
        return True

    except:#renvois un message d'erreur si utilisateur déjà dans bd
        print ("Erreur, nom d'utilisateur non disponible, veuillez changer.")
        return (False)



#modifie les dictionnaires filereadpermission et/ou fileownpermission d'un utilisateur
def modUserFilePerm(username,fileowned=None,fileread=None):

    #open document
    temp=usersCollection[str(username)]

    if fileowned != None:
        #change fileowned
        tempFileOwned=temp['fileOwned']
        tempFileOwned.update({str(len(tempFileOwned)+1):str(fileowned)})

    if fileread != None:
        #change fileread
        tempFileReadPerm=temp['fileReadPermission']
        tempFileReadPerm.update({str(len(tempFileReadPerm)+1):str(fileread)})

    temp.save()
#########################################################################
# pour bd Annotation
#########################################################################
def addExon(dict):
    doc = annotationCollection.createDocument()


    doc['id']=               dict['id']
    doc['CDS_start'] =       dict['CDS_start']
    doc['frame'] =           dict['frame']
    doc['CDS_length'] =      dict['CDS_length']
    doc['CDS_end']=          dict['CDS_end']
    doc['strand']=           dict['strand']
    doc['end']=              dict['end']
    doc['start']=            dict['start']
    doc['length'] =          dict['length']
    doc['sequence']=         dict['sequence']
    doc['number']=           dict['number']
    doc['transcript']=       dict['transcript']
    doc['chromosome']=       dict['chromosome']
    doc['gene']=             dict['gene']
    doc['protein']=          dict['protein']

    doc.save()


#########################################################################
# pour bd file
#########################################################################

#fonction permettant de copier une ligne de l'input dans la bd
def addFile(name,userID):
    doc = fileCollection.createDocument()
    doc['fileName']= name
    doc['uploadDate']= time.time()
    doc['owner']=userID

    addPermission(userID,name,1,1,1)
    modifyPerm(userId,name,name)


#########################################################################
# pour bd permission
#########################################################################

#fonction permettant de copier une ligne de l'input dans la bd
def addPermission(userID,filename,fileReadPermission,fileWritePermission,fileSharePermission):
    try:
        doc = permissionCollection.createDocument()
        doc._key=userId+filename
        doc['user']=str(userID)
        doc['file']=str(filename)
        doc['fileReadPermission']=fileReadPermission
        doc['fileWritePermission']=fileWritePermission
        doc['fileSharePermission']=fileSharePermission

    except:#l'user dispose déjà d'un accès à ce fichier

        print ("Erreur, cet utilisateur disponible déjà, veuillez changer.")
        return (False)





#########################################################################

#print addUser('ll','pp','log@hotmail.com')


"""
print usersCollection['logan']['fileOwned']
print usersCollection['logan']['fileReadPermission']


modUserFilePerm('logan',fileread='logan.tsv')

print usersCollection['logan']['fileOwned']
print usersCollection['logan']['fileReadPermission']
"""
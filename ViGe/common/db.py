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
#conn = Connection(arangoURL='http://132.204.81.223:1375')

#conn = Connection(arangoURL='http://132.204.81.150:8082')

conn = Connection(arangoURL = 'http://132.204.81.150:8082')
#conn = Connection(arangoURL='http://127.0.0.1:8529')



#Creation/initialisation des collections
try :
    db = conn.createDatabase(name = 'ViGeno')
except:
    db=conn["ViGeno"]

try:
    usersCollection= db.createCollection(name = "Users")
except:
    usersCollection=db["Users"]

try:
    annotationCollection=db.createCollection(name="Exon")
except:
    annotationCollection=db["Exon"]

try:
    fileOverviewCollection=db.createCollection(name='File_Overview')
except:
    fileOverviewCollection=db["File_Overview"]

try:
    fileContentCollection=db.createCollection(name='File_Content')
except:
    fileContentCollection=db["File_Content"]

try:
    permissionCollection=db.createCollection(name='Permissions')
except:
    permissionCollection=db['Permissions']

#######################################################################################################################
##fonction pour manipuler toutes les  bd
#######################################################################################################################

#print querie results:
#requete pour brin forward
def getExons(startPosition,endPosition,transcript_id):

    bindVars={
        'startPosition':startPosition,
        'endPosition':endPosition,
        'transcript_id':transcript_id,
        }

    aql = """
    FOR c IN Exon
        FILTER  c.start <= @startPosition && c.end >= @endPosition && c.transcript_id==@transcript_id
        RETURN c
    """

    # by setting rawResults to True you'll get dictionaries instead of Document objects, useful if you want to result to set of fields for example
    queryResult = db.AQLQuery(aql, rawResults = True, batchSize = 100, bindVars = bindVars)

    return queryResult


#requete pour brin reverse
def getExonsReverse(startPosition,endPosition,transcript_id):

    bindVars={
        'startPosition':startPosition,
        'endPosition':endPosition,
        'transcript_id':transcript_id,
        }

    aql = """
    FOR c IN Exon
        FILTER  c.start <= @endPosition  && c.end >= @startPosition && c.transcript_id==@transcript_id
        RETURN c
    """

    # by setting rawResults to True you'll get dictionaries instead of Document objects, useful if you want to result to set of fields for example
    queryResult = db.AQLQuery(aql, rawResults = True, batchSize = 100, bindVars = bindVars)

    return queryResult



#########################################################################
# pour bd User
#########################################################################

#validate if an username exist and return doc for an user in collection user
def FindUsername(username,mail):
    bindVars={
        'username':username,
        'mail':mail,
        }
    aql = """

    For c IN Users
    FILTER  c.username==@username OR c.mail==@mail
    RETURN c

    """
    queryResult = db.AQLQuery(aql, rawResults = True, batchSize = 100, bindVars = bindVars)
    return queryResult

#add a new user infos to the data bank
def addUser(username,mdp,mail):

    if len(FindUsername(str(username),str(mail)))==0:
        docUser=usersCollection.createDocument()
        docUser._key=str(username)
        docUser['username'] = str(username)
        docUser['salt'] = str(newSalt())
        docUser['mdp'] = str(mdp_hash(str(mdp),docUser['salt']))
        docUser['mail'] = str(mail)
        docUser.save()
        createPermissionDoc(str(username))
        return True

    else:#renvois un message d'erreur si utilisateur déjà dans bd
        print ("Erreur, nom d'utilisateur ou mail déjà présent dans la banque de donnée, veuillez tenter de recuperer votre compte ou changer l'username")
        return (False)

#########################################################################
# pour bd permission
#########################################################################

#initialise un document dans la collection permission pour un nouvel user
def createPermissionDoc(username):
        doc = permissionCollection.createDocument()
        doc._key=username
        doc['username']=username
        doc['fileReadPermission']=[]
        doc['fileWritePermission']=[]
        doc['fileOwned']=[]
        doc.save()

#########################################################################
#########################################################################
#fonction permettant de copier une ligne de l'input dans la bd
def modifyPermissionDoc(username,fileReadPermission=None,fileWritePermission=None,fileOwned=None):

    doc = permissionCollection[str(username)]
    if fileReadPermission is not None:
        doc['fileReadPermission'].append(fileReadPermission)
    if fileWritePermission is not None:
        doc['fileWritePermission'].append(fileWritePermission)
    if fileOwned is not None:
        doc['fileOwned'].append(fileOwned)
    doc.save()

#########################################################################
#########################################################################

#########################################################################
# pour bd Annotation
#########################################################################
def addExon(dict):
    doc = annotationCollection.createDocument()
    for k in dict :
        doc[k] = dict[k]
        doc.save()


#########################################################################
# pour bd fileOverview
#########################################################################

#fonction permettant de creer un doc dans la collection file overview qui sera utilisé pour la page utilisateur
def addFileOverview(filename,username,colonnes):
    docFileOverview = fileOverviewCollection.createDocument()
    docFileOverview._key=str(username)+','+str(filename)
    docFileOverview['fileName']= filename
    docFileOverview['uploadDate']= time.time()
    docFileOverview['originalOwner']=username
    docFileOverview['column']=colonnes
    docFileOverview.save()


#########################################################################
# pour bd fileContent
#########################################################################

#fonction permettant de creer un doc dans la collection file Content qui sera utilisé pour la page main  resultat
def addFileContent(filename,line, username, content=None):
    docFileContent = fileContentCollection.createDocument()
    docFileContent._key=str(username)+','+str(filename)+','+str(line)
    docFileContent['filename']=filename
    docFileContent['line']= line
    docFileContent['content']=content
    docFileContent.save()

#########################################################################

#collection possible : File_Content, File_Overview
def findfiles(collection, filename):
    bindVars={
        'filename':filename,
        }
    aql = """
    For c IN """+collection+"""
    FILTER  c.filename==@filename
    SORT c.line
    RETURN c
    """
    queryResult = db.AQLQuery(aql, rawResults = True, batchSize = 100, bindVars = bindVars)
    return queryResult



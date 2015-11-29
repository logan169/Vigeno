# -*- coding: utf-8 -*-

import hashlib, uuid
from pyArango.connection import *


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
    db = conn.createDatabase(name = "ViGe")
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


#######################################################################################################################
##fonction pour manipuler toutes les  bd
#######################################################################################################################


#print all elements in usercollection:
def printAllElements():
    for doc in usersCollection.fetchAll():
        print doc

#print an element of usercollection:
def printOneElement(email):
    print usersCollection[str(email)]


#########################################################################
# pour bd User
#########################################################################
#add a new user infos to the data bank
#Attention verifier que la clef de cette adresse email n'existe pas avant d'ajouter à la banque de donnée
def addUser(username,mdp,mail):

    try:
        printOneElement(mail)
        print ("Erreur, cette email dispose déjà d'un compte dans notre banque de donnée.")
        return (False)

    except:
        doc=usersCollection.createDocument()
        doc['username'] = str(username)
        doc['ID'] = len(usersCollection.fetchAll())
        doc['salt'] = str(newSalt())
        doc['mdp'] = str(mdp_hash(str(mdp),doc['salt']))
        doc['mail'] = str(mail)
        doc._key = str(mail)
        doc.save()
        return True



#########################################################################
# pour bd Annotation
#########################################################################
def addExon(dict):
    doc=annotationCollection.createDocument()
    doc['CDS_start'] =       dict['CDS_start']
    doc['chromosome'] =      dict['chromosome']
    doc['sequence'] =        dict['sequence']
    doc['frame'] =           dict['frame']
    doc['sequenceDbSNP'] =   dict['sequenceDbSNP']
    doc['CDS_length'] =      dict['CDS_length']
    doc['protein']=          dict['protein']
    doc['transcript']=       dict['transcript']
    doc['CDS_end']=          dict['CDS_end']
    doc['strand']=           dict['strand']
    doc['end']=              dict['end']
    doc['start']=            dict['start']
    doc['gene']=             dict['gene']
    doc['id']=               dict['id']
    doc['length'] =          dict['length']
    #doc._key =
    doc.save()

#########################################################################
# pour bd file
#########################################################################

def addFile(File)

print addUser('ll','pp','log@hotmail.com')

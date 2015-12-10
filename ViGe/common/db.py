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
def printAllElements(collection):
    for doc in collection.fetchAll():
        print doc

#print an element of usercollection:
def printOneElement(collection,element):
    print collection[str(element)]

#erase all collection
def EraseAll(collection):
    for doc in collection.fetchAll():
        doc.delete()

#print querie results:
def printQuerieResults(startPosition,chromosome):


    bindVars={
        'startPosition':startPosition,
        'chromosome':chromosome,
        }

    aql = "FOR c IN Exon FILTER c.chromosome==@chromosome && c.start <= @startPosition && c.end >= @startPosition RETURN c"

    """
    #modifier la requête dépendamment du strand
    if strand == '+':
        aql = "FOR c IN Exon FILTER c.chromosome==@chromosome && c.start <= @startPosition && c.end >= @startPosition RETURN c"

    elif strand == '-':
        aql = "FOR c IN Exon FILTER c.chromosome==@chromosome && c.start >= @startPosition && c.end <= @startPosition RETURN c"

    else:
        return 'error in strand submitted!\n supported strand : "+", "-"'
    """

    print aql
    # by setting rawResults to True you'll get dictionaries instead of Document objects, useful if you want to result to set of fields for example
    queryResult = db.AQLQuery(aql, rawResults = True, batchSize = 1, bindVars = bindVars)

    return queryResult

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
#def addFile(Fileline):



#print addUser('ll','pp','log@hotmail.com')

#printOneElement(annotationCollection,'Exon/296553284292')
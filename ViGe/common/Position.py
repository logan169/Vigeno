__author__ = 'schwartzl'

import format as F
import kernel as K


def startPos111(chromosomeId, startPosition,genomeId='Grch37.5'):

    from common.db import printQuerieResults

    resp=printQuerieResults(startPosition)

    try:
        doc=resp[0]
        print doc
        print doc['CDS_start']
        return doc
    except:
        print resp
        return resp



#startPos est une fonction prenant 3 arguments (str,str,int) en entree et donne en output
#un dictionnaire contenant des informations associees a la position soumise ex: geneID,sequence,annotation....
def startPos (genomeId,chromosomeId, startPosition):

    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    from pyGeno.Genome import Exon
    from pyGeno.Genome import Transcript
    from pyGeno.Genome import Chromosome
    from pyGeno.Genome import Protein
    from pyGeno.configuration import db

    print Exon.getIndexes()
    #Exon.dropGlobalIndex('chromosome')
    #Gene.dropGlobalIndex('chromosome')
    #Exon.dropGlobalIndex('start')
    #Exon.dropGlobalIndex('end')
    Exon.dropGlobalIndex(['chromosome','start', 'end'])
    Exon.dropGlobalIndex(['start', 'end'])
    Exon.dropGlobalIndex('chromosome')
    Exon.ensureGlobalIndex('start')
    Exon.ensureGlobalIndex('end')

    #Exon.ensureGlobalIndex('start')
    #Exon.ensureGlobalIndex('end')


    Gene.dropGlobalIndex('start')
    Gene.dropGlobalIndex('end')
    Gene.ensureGlobalIndex(['start', 'end'])

    #Exon.ensureGlobalIndex('start')
    #Exon.ensureGlobalIndex('end')
    #Gene.ensureGlobalIndex('start')
    #Gene.ensureGlobalIndex('end')
    print Exon.getIndexes()


    #on initialise nos variables de pyGeno en les associant au genome et chromosome de l'input
    genomeReferent = Genome (name = str(genomeId))
    chro = genomeReferent.get(Chromosome, number=str(chromosomeId))[0]


    #1ere verification:verifie si la position soumise est bien dans la sequence du chromosome
    if startPosition<=len(chro.sequence[0:]) and startPosition>=0:

        #2eme verification:verifie si la position soumise est dans l'index des exons de ce chromosome => exon
        try :
            db.enableDebug(True)
            exonReferent = genomeReferent.get(Exon, {'start <=': startPosition, 'end >': startPosition, "chromosome.number" : str(chromosomeId)})
            print Exon.getIndexes()

            resp = K.JSONResponse(F.formatExon(exonReferent[0]), False, 'ok')
            resp['data']['annotation']='Exon'
            db.enableDebug(False)

        #sinon 3eme verification:verifie si la position soumise est dans l'index des Genes de ce chromosome => intron
        except IndexError:
            try:
                geneReferent = genomeReferent.get(Gene, {'start >=': startPosition, 'end <': startPosition, "chromosome.number" : str(chromosomeId)})
                print Gene.getIndexes()
                if len(geneReferent) == 0:
                    print 'b'
                    geneReferent = genomeReferent.get(Gene, {'start <': startPosition, 'end >=': startPosition, "chromosome.number" : str(chromosomeId)})

                resp = K.JSONResponse(F.formatGene(geneReferent[0]), False, 'ok')
                resp['data']['annotation']='Intron'

            #sinon 4eme verification: la position soumise est donc forcement un intergene
            #on complete manuellement le reste du dict pour le completer
            except :
                resp = K.JSONResponse({}, False, '')
                resp['data']['annotation']='Intergene'
                resp['data']['chromosome']= chromosomeId
                resp['data']['start']= startPosition
                resp['data']['gene']= 'N/A'
                resp['data']['strand']= 'Inconnue'
                resp['data']['id']= 'N/A'


        start=startPosition-9 #peut etre modifie pour allonger/raccourcir la longueur des sequences affichees par le client
        end=startPosition+10 #peut etre modifie pour allonger/raccourcir la longueur des sequences affichees par le client


        #Si la recherche precedente n'a pas rencontree de probleme, on va tenter d'aller chercher une sequence
        #To Do: verification sequence start/end < max len(Chr) et > 0
        if resp['error']==False:

            #on ajoute la sequence de reference au dict
            resp['data']['sequence']=chro.sequence[start:end]

        #on modifie les variables genomeReferent et chro pour ajouter le masque de SNPs
        genomeReferent = Genome (name = str(genomeId), SNPs='human_dbSNP144_common_all') #masque de SNPs a modifier
        chro =  genomeReferent.get(Chromosome, number=str(chromosomeId))[0]
        #on ajoute la sequence de DBSNP au dict
        resp['data']['sequenceDbSNP']=chro.sequence[start:end]

        """
        #print frame
        try:
            print resp['data']['frame']
        except:
            print('no frame?')
        """
        
        try:
            proteinReferent = genomeReferent.get(Protein,{'name like':resp['data']['transcript']})[0]
            resp ['data']['seqProt']=proteinReferent.sequence
        except:
            print ('no prot?')
            resp ['data']['seqProt']='N/A'

    else:
        #si la position soumise n'est pas dans la sequence du chromosome, on retourne un dict contenant un message d'erreur,
        # une erreur et une liste de donnee vide
        resp = K.JSONResponse(None, True, 'La position %s est soit a l.txt\'exterieur de la sequence du chromosome %s soit a moins de 10 nucleotides d\'une extermite de la sequence' %startPosition,chromosomeId) #==> Region intergenique

    return resp



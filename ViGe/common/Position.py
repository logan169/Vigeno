__author__ = 'schwartzl'

import format as F
import kernel as K


def startPos (genomeId,chromosomeId, startPosition):

    #faire le menage dans le code

    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    from pyGeno.Genome import Exon
    from pyGeno.Genome import Transcript
    from pyGeno.Genome import Chromosome
    from pyGeno.SNP import getSNPSetsList

    from pyGeno.Chromosome import ChrosomeSequence

    Exon.ensureGlobalIndex('start')
    Exon.ensureGlobalIndex('end')
    #Exon.dropGlobalIndex('genome')
    #Gene.dropGlobalIndex('genome')
    #Gene.ensureGlobalIndex('start')
    #Gene.ensureGlobalIndex('end')


    #print getSNPSetsList()


    genomeReferent = Genome (name = str(genomeId))
    chro =  genomeReferent.get(Chromosome, number=str(chromosomeId))[0]




    if startPosition<=len(chro.sequence[0:]) and startPosition>=0:

        try :
            exonReferent = genomeReferent.get(Exon, {'start <=': startPosition, 'end >': startPosition, "chromosome.number" : str(chromosomeId)})
            resp = K.JSONResponse(F.formatExon(exonReferent[0]), False, 'ok') #==> Exon
            resp['data']['annotation']='Exon'

        except IndexError:
            try:
                geneReferent = genomeReferent.get(Gene, {'start >=': startPosition, 'end <': startPosition, "chromosome.number" : str(chromosomeId)})
                if len(geneReferent) == 0:
                    print 'b'
                    geneReferent = genomeReferent.get(Gene, {'start <': startPosition, 'end >=': startPosition, "chromosome.number" : str(chromosomeId)})

                resp = K.JSONResponse(F.formatGene(geneReferent[0]), False, 'ok') #==> Intron
                resp['data']['annotation']='Intron'
            except :
                resp = K.JSONResponse({}, False, '') #==> Region intergenique
                resp['data']['annotation']='Intergene'


        start=startPosition-9
        end=startPosition+10
        if resp['error']==False:


            resp['data']['sequence']=chro.sequence[start:end]

        #print resp['data']['sequence']

        genomeReferent = Genome (name = str(genomeId), SNPs='dummySRY_AGN')
        chro =  genomeReferent.get(Chromosome, number=str(chromosomeId))[0]

        resp['data']['sequenceDbSNP']=chro.sequence[start:end]
        #print resp['data']['sequenceDbSNP']


    else:

        resp = K.JSONResponse(None, True, 'La position %s est soit a l.txt\'exterieur de la sequence du chromosome %s soit a moins de 10 nucleotides d\'une extermite de la sequence' %startPosition,chromosomeId) #==> Region intergenique

    return resp



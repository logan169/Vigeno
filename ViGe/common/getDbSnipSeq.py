from pyGeno.Genome import Genome
from pyGeno.Genome import Chromosome
from pyGeno.tools.UsefulFunctions import *



def getdbSnipSeq(chromosome,start,end):

    #print 'ref_strand',ref_strand

    #modifier le code pour incorporer le snp
    genomeReferent = Genome (name = "GRCh37.75")# SNPs='human_dbSNP142_common_all') #masque de SNPs a modifier

    chro =  genomeReferent.get(Chromosome, number=chromosome)[0]
    #on ajoute la sequence de DBSNP au dict

    return chro.sequence[start:end]

"""
    if ref_strand == '+':
        return chro.sequence[start:end]

    elif ref_strand == '-':
        seq=chro.sequence[start:end]
        return seq[::-1]
"""

'''
print getdbSnipSeq('6',124351557,124351584,'-')

print getdbSnipSeq('6',124351557,124351584,'+')
'''
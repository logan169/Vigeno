from pyGeno.Genome import Genome
from pyGeno.Genome import Chromosome




def getdbSnipSeq(chromosome,start,end):

    #modifier le code pour incorporer le snp
    genomeReferent = Genome (name = "GRCh37.75")# SNPs='human_dbSNP142_common_all') #masque de SNPs a modifier

    chro =  genomeReferent.get(Chromosome, number=chromosome)[0]
    #on ajoute la sequence de DBSNP au dict
    return chro.sequence[start:end]


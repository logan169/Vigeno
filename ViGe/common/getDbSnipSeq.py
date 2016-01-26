from pyGeno.Genome import  Genome,Chromosome


def getdbSnipSeq(chromosome,start,end):
    genomeReferent = Genome (name = "Grch37.5", SNPs='human_dbSNP144_common_all') #masque de SNPs a modifier
    chro =  genomeReferent.get(Chromosome, number=chromosome)[0]
    #on ajoute la sequence de DBSNP au dict
    resp['data']['sequenceDbSNP']=chro.sequence[start:end]

from pyGeno.Genome import *
from pyGeno.Chromosome import *
from pyGeno.Exon import *
from pyGeno.Protein import *
from pyGeno.Transcript import *


genomeReferent = Genome (name = 'GRCh37.75')
geneReferent = genomeReferent.get(Gene, name = 'SRY')[0]

print
"""
#imprime les informations sur le genome de reference
print geneReferent.genome
print '\n'
"""
#imprime les informations sur le gene de reference
print geneReferent
print '\n'


#imprime la liste des sequences d'exons existants pour ce gene dans le genome de ref et le transcript associe
x=0
for seq in geneReferent.get(Exon):
    print seq.transcript
    print "sequence => " + seq.sequence + '\n'
    x+=1

print '%d exons trouves' %x

print "------------------------------------------------------------------------------\n-------------------------------------------------------------------------"

#imprime la liste des sequences de proteines differentes existantes pour ce gene dans le genome de ref et le transcript associe
x=0
for prot in geneReferent.get(Protein):
    print prot.transcript
    print prot.sequence


    x+=1
print '%d proteines trouvees' % x

print "------------------------------------------------------------------------------\n-------------------------------------------------------------------------"






"""






print getGenomeList()#imprime la liste des genomes telecharges
print getSNPSetsList()#imprime la liste des snp telecharges



g = Genome(name = "GRCh37.75")





#print the protein sequence
print prot.sequence
#print the protein's gene biotype
print prot.gene.biotype
#print protein's transcript sequence
print prot.transcript.sequence

#fancy queries
for exons in g.get(Exon, {"CDS_start >": 1, "CDS_end <=" : 3, "chromosome.number" : "22"}) :
        #print the exon's coding sequence
        print exon.CDS
        #print the exon's transcript sequence
        print exon.transcript.sequence


#You can do the same for your subject specific genomes
#by combining a reference genome with polymorphisms
g = Genome(name = "GRCh37.75", SNPs = ["STY21_RNA"], SNPFilter = MyFilter())
"""
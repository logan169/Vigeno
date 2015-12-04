__author__ = 'schwartzl'

from pyGeno.Genome import Genome
from pyGeno.Genome import Chromosome
from pyGeno.Genome import Exon
from common import db as db

genomeId='GRCh37.75'
chromosomeId='Y'

genomeReferent = Genome ( name = str(genomeId))

exons=genomeReferent.iterGet(Exon)


x=0
for exon in exons:

  dict={}
  dict['key']=x
  dict['id']= exon.id
  dict['number']= exon.number
  dict['start']= exon.start
  dict['end']= exon.end
  dict['length']= exon.length
  dict['CDS_length']= exon.CDS_length
  dict['CDS_start']= exon.CDS_start
  dict['CDS_end']= exon.CDS_end
  dict['frame']= exon.frame
  dict['strand']= exon.strand
  dict['sequence']= exon.sequence

  db.addExon(dict)
  x+=1








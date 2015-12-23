__author__ = 'schwartzl'

from pyGeno.Genome import Genome
from pyGeno.Genome import Exon
from common import db as db


genomeId='GRCh37.75'
chromosomeId='Y'

genomeReferent = Genome ( name = str(genomeId))

exons=genomeReferent.iterGet(Exon)


for exon in exons:

  dict={
        'id': exon.id,
        'number': exon.number,
        'start': exon.start,
        'end': exon.end,
        'length': exon.length,
        'CDS_length': exon.CDS_length,
        'CDS_start': exon.CDS_start,
        'CDS_end': exon.CDS_end,
        'frame': exon.frame,
        'strand': exon.strand,
        'chromosome': exon.chromosome.number,
        'gene_name': exon.gene.name,
        'transcript_name': exon.transcript.name,
        'protein_name': exon.protein,
        'sequence':exon.sequence,
        'gene_id': exon.gene.id,
        'transcript_id': exon.transcript.id,

        if exon.protein != None:
                'protein_id': exon.protein.id,

    }


  db.addExon(dict)








from pyGeno.Genome import *
from pyGeno.tools.ProgressBar import ProgressBar

try:
      from common import db as db
except:
      import db as db

genomeId='GRCh37.75'
genomeReferent = Genome(name = str(genomeId))

exons = genomeReferent.iterGet(Exon)
count = genomeReferent.count(Exon)
pg = ProgressBar(nbEpochs=count)
for exon in exons:
  pg.update(label=exon.id)
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
        'sequence':exon.sequence,
        'gene_id': exon.gene.id,
        'transcript_id': exon.transcript.id,
  }

  # exon.protein revient None tout le temps
  #donc on utilise exon.transcript.protein.name
  try:
    dict['protein_name'] = exon.transcript.protein.name
    dict['protein_id'] = exon.transcript.protein.id
  except:
    dict['protein_name'] = None
    dict['protein_id'] = None

  db.addExon(dict)

pg.close()

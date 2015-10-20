__author__ = 'schwartzl'

def formatGene(gene) :
    return {
        'id': gene.id,
        'name': gene.name,
        'strand': gene.strand,
        'start': gene.start,
        'end': gene.end,
        'biotype': gene.biotype,
        'chromosome': gene.chromosome.number,
        'genome': gene.genome.name,
    }

def formatExon(exon) :
    return {
        'id': exon.id,
        'number': exon.number,
        'start' : exon.start,
        'end' : exon.end,
        'length' : exon.length,
        'CDS_length' : exon.CDS_length,
        'CDS_start' : exon.CDS_start,
        'CDS_end' : exon.CDS_end,
        'frame' : exon.frame,
        'strand' : exon.strand,

        'genome': exon.genome.name,
        'chromosome': exon.chromosome.number,
        'gene': exon.gene.name,
        'transcript': exon.transcript.name,
        'protein': exon.protein,
    }

def formatTranscript(transcript) :
    return {
        'id': transcript.id,
        'name': transcript.name,
        'start' : transcript.start,
        'end' : transcript.end,
        'length' : transcript.length,
        'coding' : transcript.coding,
        'genome': transcript.genome.name,
        'chromosome': transcript.chromosome.number,
        'gene': transcript.gene.name,
        'protein': transcript.protein.name,
        'exons':transcript.exon.id
    }

def formatProtein(protein) :
    return {
        'id': protein.id,
        'name': protein.name,
        'genome': protein.genome.name,
        'chromosome': protein.chromosome.name,
        'gene': protein.gene.name,
        'transcript': protein.transcript.name,
    }
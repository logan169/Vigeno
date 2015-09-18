__author__ = 'schwartzl'

def formatGene(gene) :
    return {
        'id': gene.id,
        'name': gene.name,

        'strand': gene.strand,
        'start': gene.start,
        'chromosome': gene.chromosome.number,
        'genome': gene.genome.name,
    }

def formatExon(exon) :
    return {
        'id': exon.id,
        'name': exon.name,
        'start' : exon.start,
        'end' : exon.end,
        'length' : exon.length,
        'CDS_length' : exon.CDS_length,
        'CDS_start' : exon.CDS_start,
        'CDS_end' : exon.CDS_end,
        'frame' : exon.frame,
        'strand' : exon.strand,

        'genome': str(exon.genome),
        'chromosome': str(exon.chromosome),
        'gene': exon.gene.name,
        'transcript': str(exon.transcript),
        'protein': str(exon.protein),
    }

def formatTranscript(transcript) :
    return {
        'id': transcript.id,
        'name': transcript.name,
        'start' : transcript.start,
        'end' : transcript.end,
        'length' : transcript.length,
        'coding' : transcript.coding,

        'genome': str(transcript.genome),
        'chromosome': str(transcript.chromosome),
        'gene': str(transcript.gene),
        'protein': str(transcript.protein),
    }

def formatProtein(protein) :
    return {
        'id': protein.id,
        'name': protein.name,

        'genome': str(protein.genome),
        'chromosome': str(protein.chromosome),
        'gene': str(protein.gene),
        'transcript': str(protein.transcript),
    }
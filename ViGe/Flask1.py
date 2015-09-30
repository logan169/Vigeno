__author__ = 'schwartzl'

import flask
from flask import Flask, url_for, redirect

import ViGe.format as F
import ViGe.kernel as K

app = Flask(__name__)

########################################################################################################################
#######################################      programme flask        ####################################################
########################################################################################################################
########################################################################################################################

# Home sweet home!!!
@app.route('/')
def home():
    return '<br/>Welcome to pyGeno visual interface! <br/> Please enter a command in the URL <br> <br> i.e: /genomeId/... ' \
           '<br> &nbsp &nbsp &nbsp &nbsp gene/geneId/ <br> &nbsp &nbsp &nbsp &nbsp exon/exonId/ <br> &nbsp &nbsp &nbsp &nbsp ' \
           'transcript/transcriptId/ <br> &nbsp &nbsp &nbsp &nbsp protein/proteinId/'

# ask to write a complete path as /<genomeId>/...
@app.route('/<genomeId>/')
def genomeId(genomeId):
    from pyGeno.Genome import Genome

    try:
        genomeReferent = str(Genome (name = str(genomeId)))
        return '<br/><br/> %s <br/> <br> Please enter  a command as followed in the URL to continue <br> <br> i.e: /genomeId/... <br> ' \
           '&nbsp &nbsp &nbsp &nbsp gene/geneId/ <br> &nbsp &nbsp &nbsp &nbsp exon/exonId/ <br> &nbsp &nbsp &nbsp &nbsp transcript/transcriptId/' \
           ' <br> &nbsp &nbsp &nbsp &nbsp protein/proteinId/ <br> &nbsp &nbsp &nbsp &nbsp position/startPosition' % genomeReferent
    except:
        return redirect(url_for('home'))

#redirige vers la page de genomeId si le path est incomplet
@app.route('/<genomeId>/<l>/')
def incompletPath(genomeId,l):
    return redirect(url_for('genomeId', genomeId=str(genomeId)))



#print to screen complet information for position
@app.route('/<genomeId>/<chromosomeId>/<int:startPosition>/')
def startPos (genomeId,chromosomeId, startPosition):

    #faire le menage dans le code

    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    from pyGeno.Genome import Exon
    from pyGeno.Genome import Transcript
    from pyGeno.Genome import Chromosome
    import pyGeno.configuration as conf

    Exon.ensureGlobalIndex('start')
    Exon.ensureGlobalIndex('end')
    Exon.dropGlobalIndex('genome')
    Gene.dropGlobalIndex('genome')
    #Gene.ensureGlobalIndex('start')
    #Gene.ensureGlobalIndex('end')

    genomeReferent = Genome (name = str(genomeId))



"""
    ####################################################################################################################################
    #1ere facon de faire la position basee sur les index
    ####################################################################################################################################
    try :
        exonReferent = genomeReferent.get(Exon, {'start <=': startPosition, 'end >': startPosition, "chromosome.number" : str(chromosomeId)})
        resp = K.JSONResponse(F.formatExon(exonReferent[0]), False, 'ok') #==> Exon

    except IndexError:
        try:
            geneReferent = genomeReferent.get(Gene, {'start >=': startPosition, 'end <': startPosition, "chromosome.number" : str(chromosomeId)})
            if len(geneReferent) == 0:
                print 'b'
                geneReferent = genomeReferent.get(Gene, {'start <': startPosition, 'end >=': startPosition, "chromosome.number" : str(chromosomeId)})

            resp = K.JSONResponse(F.formatGene(geneReferent[0]), False, 'ok') #==> Intron
        except :
            resp = K.JSONResponse(None, True, 'position not found') #==> Region intergenique

    return flask.jsonify(**resp)

"""
#########################################################################
#2eme facon d'avoir la position basee sur des iterget /iterative
#########################################################################
"""

    Exon.dropGlobalIndex('genome')
    Gene.dropGlobalIndex('genome')
    Exon.ensureGlobalIndex('start')
    Exon.ensureGlobalIndex('end')
    Exon.dropGlobalIndex('start')
    Exon.dropGlobalIndex('end')

    Exon.ensureGlobalIndex(['start','end'])
    genomeReferent = Genome (name = str(genomeId))



    #version iterative fonctionnelle...mais longue comme l'hiver
    try :
        for exon in genomeReferent.iterGet(Exon, { "chromosome.number" : str(chromosomeId) }):
            if exon.start <= startPosition and exon.end > startPosition:
                print 'position est dans l\'exon : '+ str(exon)
                return str(exon.id)

    except ValueError:
        for gene in genomeReferent.iterGet(Gene, { "chromosome.number" : str(chromosomeId) }):
            if gene.start <= startPosition and gene.end > startPosition:
                print 'position est dans un intron du gene : '+ str(gene)
                return str(gene.name)

    # A faire, verifier que la position est comprise entre 0 et chromosome length
    return 'position est dans une region intergenique du chromosome '+ str(chromosomeId)
"""

#############################################################################################
##range
##########################################################################
@app.route('/<genomeId>/<chromosomeId>/<int:startPosition>/<int:endPosition>/')
def range (genomeId,chromosomeId, startPosition, endPosition):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    from pyGeno.Genome import Exon
    from pyGeno.Genome import Transcript
    from pyGeno.Genome import Chromosome

    genomeReferent = Genome (name = str(genomeId))

    chro =  genomeReferent.get(Chromosome, number = str(chromosomeId))[0]
    return chro.sequence[startPosition:endPosition]


    #print genomeReferent.get(ChromosomeSequence_getSequence, {'start =': startPosition, 'end =': endPosition, "chromosome.number =" str(chromosomeId)})
    #return Chromosome.ChromosomeSequence_getSequence(startPosition, endPosition)









#print to screen complet information for gene
@app.route('/<genomeId>/gene/<geneId>/')
def geneId (genomeId,geneId):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    Gene.ensureGlobalIndex('name')
    Gene.ensureGlobalIndex('id')
    genomeReferent = Genome (name = str(genomeId))

    try :
        geneReferent = genomeReferent.get(Gene, id = str(geneId.upper()))[0]

    except IndexError:
        try:
            geneReferent = genomeReferent.get(Gene, name = str(geneId.upper()))[0]
        except :
            resp = K.JSONResponse(None, True, 'Gene not found')
            return flask.jsonify(**resp)

    resp = K.JSONResponse(F.formatGene(geneReferent), False, 'ok')
    return flask.jsonify(**resp)

#print to screen complet information for exon
@app.route('/<genomeId>/exon/<exonId>/')
def exon (genomeId,exonId):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Exon
    Exon.ensureGlobalIndex('id')
    genomeReferent = Genome (name = str(genomeId))

    try :
        exonReferent = genomeReferent.get(Exon, id = str(exonId.upper())) [0]
        resp = K.JSONResponse(F.formatExon(exonReferent), False, 'ok')
    except :
        resp = K.JSONResponse(None, True, 'Exon not found')

    return flask.jsonify(**resp)

#print to screen complet information for transcript
@app.route('/<genomeId>/transcript/<transcriptId>/')
def transcriptId (genomeId,transcriptId):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Transcript
    Transcript.ensureGlobalIndex('name')
    Transcript.ensureGlobalIndex('id')
    genomeReferent = Genome (name = str(genomeId))

    try :
        transcriptReferent = genomeReferent.get(Transcript, id = str(transcriptId.upper())) [0]

    except IndexError:
        try:
            transcriptReferent = genomeReferent.get(Transcript, name = str(transcriptId.upper()))[0]
        except :
            resp = K.JSONResponse(None, True, 'Transcript not found')
            return flask.jsonify(**resp)

    resp = K.JSONResponse(F.formatTranscript(transcriptReferent), False, 'ok')
    return flask.jsonify(**resp)


#print to screen complet information for protein
@app.route('/<genomeId>/protein/<proteinId>/')
def proteinId (genomeId,proteinId):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Protein
    Protein.ensureGlobalIndex('name')
    Protein.ensureGlobalIndex('id')
    genomeReferent = Genome (name = str(genomeId))

    try :
        proteinReferent = genomeReferent.get(Protein, name = str(proteinId)) [0]


    except IndexError:
        try:
            proteinReferent = genomeReferent.get(Protein, id = str(proteintId))[0]
        except :
            resp = K.JSONResponse(None, True, 'Protein not found')
            return flask.jsonify(**resp)

    resp = K.JSONResponse(F.formatProtein(proteinReferent), False, 'ok')
    return flask.jsonify(**resp)


if __name__ == '__main__':
    app.debug=True
    app.run()

"""
########################################################################################################################
#brouillon
########################################################################################################################

string = ''
#imprime les informations sur le genome de reference
string += genomeReferent.genome + '<br>'

#imprime les informations sur le gene de reference
string += geneReferent.genome + '<br>'

#imprime la liste des sequences d'exons existants pour ce gene dans le genome de ref et le transcript associe
x=0
for seq in geneReferent.get(Exon):
    string += seq.transcript + "<br>"+ "sequence => " + seq.sequence + "<br>"
    x+=1

string += '%d exons trouves' %x

return string

"""
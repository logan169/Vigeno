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

########################################################################################################################
#modificaton a ajouter:
########################################################################################################################
#
#modifier les str dans le fichier format
#
#//implementer de partout return dictionnaire dans dictionnaires##########################verifier si fonctionne bien
#
#
#
#
#
#
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
    genomeReferent = str(Genome (name = str(genomeId)))
    return '<br/><br/> %s <br/> <br> Please enter  a command as followed in the URL to continue <br> <br> i.e: /genomeId/... <br> ' \
           '&nbsp &nbsp &nbsp &nbsp gene/geneId/ <br> &nbsp &nbsp &nbsp &nbsp exon/exonId/ <br> &nbsp &nbsp &nbsp &nbsp transcript/transcriptId/' \
           ' <br> &nbsp &nbsp &nbsp &nbsp protein/proteinId/ <br> &nbsp &nbsp &nbsp &nbsp position/startPosition' % genomeReferent

#redirige vers la page de genomeId si le path est incomplet
@app.route('/<genomeId>/<l>/')
def incompletPath(genomeId,l):
    return redirect(url_for('genomeId', genomeId=str(genomeId)))



#print to screen complet information for position
@app.route('/<genomeId>/<chrosome>/<int:startPosition>/')
def startPos (genomeId,chromosome, startPosition):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    from pyGeno.Genome import Exon
    from pyGeno.Genome import Transcript
    from pyGeno.Genome import Chromosome
    Exon.ensureGlobalIndex('start')			#est ce que on peut faire ca?
    Gene.ensureGlobalIndex('start')			#est ce que on peut faire ca?
    Transcript.ensureGlobalIndex('start')	#est ce que on peut faire ca?

    genomeReferent = Genome (name = str(genomeId))

    try :
        ExonReferent = genomeReferent.get(Exon, start = str(startPosition))[0]
        resp = K.JSONResponse(F.formatExon(ExonReferent), False, 'ok') #==> Exon

    except:
        try:
            geneReferent = genomeReferent.get(Gene, start = str(startPosition))[0]
            resp = K.JSONResponse(F.formatGene(geneReferent), False, 'ok') #==> Intron
        except IndexError:
            resp = K.JSONResponse(None, True, 'Gene not found') #==> Region intergenique

    return flask.jsonify(**resp)

    #for exons in g.get(Exons, {"CDS_start >": x1, "CDS_end <=" : x2, "chromosome.number" : "22"}) :


#print to screen complet information for gene
@app.route('/<genomeId>/gene/<geneId>/')
def geneId (genomeId,geneId):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Gene
    Gene.ensureGlobalIndex('name')
    Gene.ensureGlobalIndex('id')
    genomeReferent = Genome (name = str(genomeId))

    try :
        geneReferent = genomeReferent.get(Gene, name = str(geneId))[0]
        resp = K.JSONResponse(F.formatGene(geneReferent), False, 'ok')

    except:
        try:
            geneReferent = genomeReferent.get(Gene, id = str(geneId))[0]
            resp = K.JSONResponse(F.formatGene(geneReferent), False, 'ok')
        except IndexError:
            resp = K.JSONResponse(None, True, 'Gene not found')

    return flask.jsonify(**resp)

#print to screen complet information for exon
@app.route('/<genomeId>/exon/<exonId>/')
def exon (genomeId,exonId):
    from pyGeno.Genome import Genome
    from pyGeno.Genome import Exon
    Exon.ensureGlobalIndex('name')
    Exon.ensureGlobalIndex('id')
    genomeReferent = Genome (name = str(genomeId))

    try :
        exonReferent = genomeReferent.get(Exon, name = str(exonId)) [0]
        resp = K.JSONResponse(F.formatExon(exonReferent), False, 'ok')

    except:
        try:
            exonReferent = genomeReferent.get(Exon, id = str(exonId))[0]
            resp = K.JSONResponse(F.formatExon(exonReferent), False, 'ok')
        except IndexError:
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
        transcriptReferent = genomeReferent.get(Transcript, name = str(transcriptId)) [0]
        resp = K.JSONResponse(F.formatTranscript(transcriptReferent), False, 'ok')

    except:
        try:
            transcriptReferent = genomeReferent.get(Transcript, id = str(transcriptId))[0]
            resp = K.JSONResponse(F.formatTranscript(transcriptReferent), False, 'ok')
        except IndexError:
            resp = K.JSONResponse(None, True, 'Transcript not found')

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
        resp = K.JSONResponse(F.formatProtein(proteinReferent), False, 'ok')

    except:
        try:
            proteinReferent = genomeReferent.get(Protein, id = str(proteintId))[0]
            resp = K.JSONResponse(F.formatProtein(proteinReferent), False, 'ok')
        except IndexError:
            resp = K.JSONResponse(None, True, 'Protein not found')

    return flask.jsonify(**resp)


if __name__ == '__main__':
    app.debug=True
    app.run()

########################################################################################################################
#brouillon
########################################################################################################################
"""
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



#the name of the genome is defined inside the package's manifest.ini file
#get returns a list of elements
from pyGeno.Genome import Genome
from pyGeno.Genome import Gene
from pyGeno.Genome import Protein

GenomeReferent = Genome(name = str(genomeId))
return str(GenomeReferent.get(Gene, name = str(geneId))[0]) + '\n'+ str(GenomeReferent.get(Protein, name = str(geneId)))
"""




'''
g = Genome(name = "GRCh37.75")
prot = g.get(Protein, id = 'ENSP00000438917')[0]
#print the protein sequence
print prot.sequence
#print the protein's gene biotype
print prot.gene.biotype
#print protein's transcript sequence
print prot.transcript.sequence

GRCh37.75
SRY
'''
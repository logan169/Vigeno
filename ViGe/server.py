


from flask import Flask, url_for, redirect, send_from_directory,request,render_template
import sys
sys.path.append('/u/schwartzl/py/ViGe/ViGe/common/')
import format as F
import kernel as K


app = Flask(__name__)

# Home sweet home!!!
@app.route('/')
def home():
    return render_template('index.html')



    """
	resp = K.JSONResponse({}, False, 'Welcome to pyGeno visual interface! <br/> Please enter a command in the URL \n\n'
                                   +'i.e: /genomeId/\n \ngene/geneId/\n \nexon/exonId/\n \ntranscript/transcriptId/\n\n'
                                    +'protein/proteinId/ \n \n position/startPosition')
	return resp"""

# ask to write a complete path as /<genomeId>/...
@app.route('/<genomeId>/')
def genomeId(genomeId):
    from pyGeno.Genome import Genome

    try:
        genomeReferent = str(Genome (name = str(genomeId)))
        resp = K.JSONResponse({}, False, '%s \n\n Welcome to pyGeno visual interface! <br/> Please enter a command in the URL \n\n'
                                   +'i.e: /genomeId/\n \ngene/geneId/\n \nexon/exonId/\n \ntranscript/transcriptId/\n\n'
                                    +'protein/proteinId/ \n \n position/startPosition' % genomeReferent)
	return resp

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

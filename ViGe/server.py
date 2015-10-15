


from flask import Flask, url_for, redirect, send_from_directory,request,render_template
import sys

import common.format as F
import common.kernel as K


app = Flask(__name__, static_folder='front')

@app.route('/')
def send_file():
  return send_from_directory(app.static_folder,"index.html")


"""


# ask to write a complete path as /<genomeId>/...
@app.route('/api/<genomeId>/')
def genomeId(genomeId):
    from pyGeno.Genome import Genome

    try:
        genomeReferent = str(Genome (name = str(genomeId)))
        resp = K.JSONResponse({}, False, '%s \n\n Welcome to pyGeno visual interface! <br/> Please enter a command in the URL \n\n'
                                   +'i.e: /genomeId/\n \ngene/geneId/\n \nexon/exonId/\n \ntranscript/transcriptId/\n\n'
                                    +'protein/proteinId/ \n \n position/startPosition' % genomeReferent)
	return resp

    except:
        return redirect(url_for('/'))


#redirige vers la page de genomeId si le path est incomplet
@app.route('/api/<genomeId>/<l>/')
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
    chro =  genomeReferent.get(Chromosome, number = str(chromosomeId))[0]

    #voir pkoi le serveur renvoit directement un 404 sur starposition<0

    if startPosition<=len(chro.sequence[0:]) and startPosition>=0:

        try :
            exonReferent = genomeReferent.get(Exon, {'start <=': startPosition, 'end >': startPosition, "chromosome.number" : str(chromosomeId)})
            resp = K.JSONResponse(F.formatExon(exonReferent[0]), False, 'ok') #==> Exon
            resp['data']['annotation']='Exon'

        except IndexError:
            try:
                geneReferent = genomeReferent.get(Gene, {'start >=': startPosition, 'end <': startPosition, "chromosome.number" : str(chromosomeId)})
                if len(geneReferent) == 0:
                    print 'b'
                    geneReferent = genomeReferent.get(Gene, {'start <': startPosition, 'end >=': startPosition, "chromosome.number" : str(chromosomeId)})

                resp = K.JSONResponse(F.formatGene(geneReferent[0]), False, 'ok') #==> Intron
                resp['data']['annotation']='Intron'
            except :
                resp = K.JSONResponse({}, False, '') #==> Region intergenique
                resp['data']['annotation']='Intergene'



        if resp['error']==False:
            start=startPosition-10
            end=startPosition+11

            resp['data']['sequence']=chro.sequence[start:end]

        print resp['data']['sequence']





    else:

        resp = K.JSONResponse(None, True, 'La position %s est soit a l\'exterieur de la sequence du chromosome %s soit a moins de 10 nucleotides d\'une extermite de la sequence' %startPosition,chromosomeId) #==> Region intergenique

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
    print resp
    return flask.jsonify(**resp)

#print to screen complet information for exon
@app.route('/api/<genomeId>/exon/<exonId>/')
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
@app.route('/api/<genomeId>/protein/<proteinId>/')
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
"""

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8091)

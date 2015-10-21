

import flask


import common.format as F
import common.kernel as K


app = flask.Flask(__name__, static_folder='front')


@app.route('/')
def send_file():
  return flask.send_from_directory(app.static_folder,"index.html")




#upload a file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    print (send_from_directory(app.config['UPLOAD_FOLDER'],filename))
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)






#print to screen complet information for position
@app.route('/api/v0/<genomeId>/<chromosomeId>/<int:startPosition>/')
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
            start=startPosition-9
            end=startPosition+10

            resp['data']['sequence']=chro.sequence[start:end]

        print resp['data']['sequence']


    else:

        resp = K.JSONResponse(None, True, 'La position %s est soit a l.txt\'exterieur de la sequence du chromosome %s soit a moins de 10 nucleotides d\'une extermite de la sequence' %startPosition,chromosomeId) #==> Region intergenique

    return flask.jsonify(**resp)

#print to screen complet information for protein
@app.route('/api/v0/<genomeId>/protein/<proteinId>/')
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
    app.run(host='0.0.0.0',port=8091)

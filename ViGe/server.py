

import flask


import common.format as F
import common.kernel as K
import common.parser as P
import common.Position as Pos


app = flask.Flask(__name__, static_folder='front')

#premier call envoie vers index.html
#ensuite c'est Angular qui gere les vues
@app.route('/')
def send_file():
  return flask.send_from_directory(app.static_folder,"index.html")




#route pour uploader des data du client a partir de l'URL et construire le tableau
@app.route('/api/v0/uploadURL/<input>/')
def uploaded_file(input):


    #on stock l'information a renvoyer au client dans data
    data={}

    #l'input est parse par parseURL puis manipule de sorte a construire data par la suite
    #la variable file est un dict sous la forme file={Chromosome1=[pos1,pos2,pos3,....],Chromosome2=[....],....}
    file=P.parseURL(input)
    print file


    #maintenant on utilise le dictionaire file pour iterer sur toutes les values pour chacune des keys en appellant
    # la fonction Position a chaque fois. Au final, le dict data a la forme suivante, chaques sequences de l'input est
    # associees a un index correspondant a un dictionnaire contenant toutes l'info pour cette sequence.
    # IL y a donc une key error et message et une key pour chaque sequence soumise

    #ex d'output
    #{'0': {'message': 'ok', 'data': {'CDS_start': 2655074, 'chromosome': u'Y', 'sequence': 'ATGATTGCATTGTCAAAAA',
    #  'frame': 0, 'number': 0, 'sequenceDbSNP': 'ATGATTGCADTGTCAAAAA', 'CDS_length': 570, 'protein': None,
    #  'transcript': u'SRY-201', 'CDS_end': 2655644, 'strand': u'-', 'end': 2655644, 'id': u'ENSE00002201849',
    #  'start': 2655074, 'length': 570, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'SRY'}, 'error': False}}


    x=0 #correspond a l'iterateur d'index du dictionnaire data
    for key in file:
        for value in file[key]:

            #utilise la fonction startPos dans le dossier common, cette fonction prends 3 parametre en entree:
            # startPos(genome,chromosome,position) et renvoie un dict contenant toutes les infos necessaires au client
            #pour cette sequence
            data[str(x)]=Pos.startPos('GRCh37.75',str(key),int(value))
            x+=1

    return flask.jsonify(**data)









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

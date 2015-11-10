

import flask
import common.parser as P
import common.Position as Pos

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = flask.Flask(__name__, static_folder='front')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/api/v0/sendFile/<input>/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return


#premier call envoie vers index.html
#ensuite c'est Angular qui gere les vues
@app.route('/')
def send_file():
  return flask.send_from_directory(app.static_folder,"index.html")



########################################################################################################################

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


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8091)

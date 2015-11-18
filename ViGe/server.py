

import flask
import common.parser as P
import common.kernel as K

import common.Position as Pos

import os

# Initialize the Flask application
app = flask.Flask(__name__, static_folder='front')



# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename



#premier call envoie vers index.html
#ensuite c'est Angular qui gere les vues
@app.route('/')
def send_file():
  return flask.send_from_directory(app.static_folder,"index.html")


# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# Route that will process the file upload
@app.route('/api/v0/uploadFile/', methods=['POST'])
def upload_File():


    if request.files['file'].filename == '':
        return flask.jsonify(**K.JSONResponse(None,True,'No file selected! please select a file!'))
    else:
        # Get the name of the uploaded file
        file = request.files['file']
        #print file
        # Check if the file is one of the allowed types/extensions
        #print file and allowed_file(file.filename)
        if file and allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = secure_filename(file.filename)
            filename=filename.replace(' ','_')
            # Move the file form the temporal folder to
            # the upload folder we setup
            #print os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return flask.jsonify(**K.JSONResponse(None,False,'file uploaded'))

@app.route('/api/v0/processFile/<filename>/', methods=['POST'])
def process_File(filename):

    dictFile= P.parseFile('/u/schwartzl/py/projetIric/17nov/ViGe/uploads/'+filename)
    return flask.jsonify(**dictFile)



#route pour uploader des data du client a partir de l'URL et construire le tableau
@app.route('/api/v0/uploadURL/<input>/')
def uploaded_URL(input):

    #on stock l'information a renvoyer au client dans data
    data={}

    #l'input est parse par parseURL puis manipule de sorte a construire data par la suite
    #la variable file est un dict sous la forme file={Chromosome1=[pos1,pos2,pos3,....],Chromosome2=[....],....}
    file=P.parseURL(input)
    return flask.jsonify(**file)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8091)

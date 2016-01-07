
import flask
import common.parser as P
import common.kernel as K
import common.tree as T
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


###########################################################################################################
def authentification(username=None):
    user= 'log'
    if username is not None:
        user=str(username)
    return user

dictFile={}
dictTab={}
###########################################################################################################

#premier call envoie vers index.html
#ensuite c'est Angular qui gere les vues
@app.route('/')
def index():
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
            #path=os.path.join(app.config['UPLOAD_FOLDER'])
            # Move the file form the temporal folder to
            # the upload folder we setup
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            global dictTab
            dictTab=P.parseFile(os.path.join(app.config['UPLOAD_FOLDER']),filename,authentification())
            return flask.jsonify(**dictTab)








@app.route('/api/v0/modifyTree/<userChoice>/', methods=['GET'])
def modifyTree(userChoice):
    #print 'userChoice : '+userChoice

    global dictTab  #j'improte mon nouveau dict du tableau a partir de  ma variable global dictTab

    temp= K.JSONResponse(T.TreeJsInput(userChoice,dictTab),False,'yeas')
    #print temp
    return flask.jsonify(**temp)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8091)

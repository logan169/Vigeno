
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


username='log'

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
            # Move the file form the temporal folder to
            # the upload folder we setup
            #print os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #print str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return flask.jsonify(**K.JSONResponse(None,False,'file uploaded'))



dictTab={}
@app.route('/api/v0/processFile/<filename>/', methods=['POST'])
def process_File(filename):
    from common import time_processing
    fileuploadedPath= (str(os.path.join(app.config['UPLOAD_FOLDER'])+filename))
    #print fileuploadedPath
    #dictFile= P.parseFile(fileuploadedPath)
    global username
    path=os.path.join(app.config['UPLOAD_FOLDER'])


    dictFile=P.parseFile(path,filename,username)
    print dictFile
    global dictTab
    dictTab= dictFile   #j'enregistre mon nouveau dict du tableau dans ma variable global dictTab
    #print dictFile
    time_processing.endlog()
    return flask.jsonify(**dictFile)



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

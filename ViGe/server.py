
import flask
import common.parser as P
import common.addDictInDb as A
import common.kernel as K
import common.tree as T
from common.DNA_and_6FramesTraduction import DNA_and_6FramesTraduction
from common.getDbSnipSeq import getdbSnipSeq
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



#######################################################################################################################
###
#####################################################################################################################
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# route qui enregistre le fichier dans le fichier 'Upload'
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

            # enregistre le fichier dans le fichier 'Upload'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print 'upload_File'+' passed!'
            return flask.jsonify(**K.JSONResponse(None,False,'file uploaded'))

########################################################################################################################

@app.route('/api/v0/processFile/<filename>/',methods=['POST'])
def copy_File_and_his_output_in_DB_File_Content(filename):
            #print filename
            #dict=parseFile("/u/schwartzl/py/projetIric/20160114/ViGe/uploads/",'pep_pep_pep.csv','log')

            dictTab=P.parseFile(os.path.join(app.config['UPLOAD_FOLDER']),filename,authentification())

            if dictTab['error']==True:
                return dictTab ######################################message d'erreur
            else:
                print 'DictTab done!'
                try:
                    outputDict=A.addDictInDb(**dictTab['data'])
                except:
                    outputDict=O()
                    return flask.jsonify(**K.JSONResponse(outputDict,False,'file in db!'))

            if outputDict['error'] ==True:
                return outputDict ######################################message d'erreur
            else:
                print 'copy_File_and_his_output_in_DB_File_Content'+' passed!'
                #print outputDict['data']
                return flask.jsonify(**K.JSONResponse(outputDict['data'],False,'file in db!'))

########################################################################################################################
@app.route('/api/v0/loadFile/<fileName>/', methods=['POST','GET'])
def load_File_in_DB_File_Content_to_client(filename):

    return('',204)


########################################################################################################################
#produit un dict contenant les 6 frames d'ADN et leur traduction respectives

@app.route('/api/v0/getDNA&AA/<seq>/', methods=['POST','GET'])
def getSequences(seq):
    seq=str(seq)
    temp= K.JSONResponse(DNA_and_6FramesTraduction(seq),False,'')
    return flask.jsonify(**temp)


########################################################################################################################
########################################################################################################################
#produit un dict contenant les 6 frames d'ADN et leur traduction respectives

@app.route('/api/v0/getDNA&AADBSNIP/<chromosome>/<int:start>/<int:end>/<ref_strand>/', methods=['POST','GET'])
def getsequencesDbSNIP(chromosome,start,end,ref_strand):
    chromosome=str(chromosome)
    start=int(start)
    end=int(end)
    ref_strand=str(ref_strand)

    temp= K.JSONResponse(DNA_and_6FramesTraduction(getdbSnipSeq(chromosome,start,end,ref_strand)),False,'')
    return flask.jsonify(**temp)


########################################################################################################################


@app.route('/api/v0/modifyTree/<userChoice>/', methods=['GET'])
def modifyTree(userChoice):
    #print 'userChoice : '+userChoice

    global dictTab  #j'improte mon nouveau dict du tableau a partir de  ma variable global dictTab

    temp= K.JSONResponse(T.TreeJsInput(userChoice,dictTab),False,'')
    #print temp
    return flask.jsonify(**temp)






if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8091)



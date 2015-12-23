
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


#premier call envoie vers index.html
#ensuite c'est Angular qui gere les vues
@app.route('/')
def index():
  return flask.send_from_directory(app.static_folder,"index.html")


# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['csv'])


@app.route('/api/v0/rapido/', methods='GET')
def rapido():
    dict={'1': {'message': 'ok', 'data': {'CDS_start': None, 'chromosome': u'6', 'sequence': 'TTCCCCACGCATCTGAGGG', 'frame': None, 'number': 4, 'sequenceDbSNP': 'TTCCCCACGCATCTGAGGG', 'CDS_length': None, 'seqProt': 'N/A', 'protein': None, 'transcript': u'FLOT1-011', 'CDS_end': None, 'strand': u'-', 'end': 30698342, 'id': u'ENSE00003564703', 'start': 30698204, 'length': 138, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'FLOT1'}, 'error': False}, '0': {'message': 'ok', 'data': {'CDS_start': 3405547, 'chromosome': u'2', 'sequence': 'GGTGAAAAAGCTGCAGCAA', 'frame': 0, 'number': 2, 'sequenceDbSNP': 'GGTGAAAAAGCTGCAGCAA', 'CDS_length': 117, 'seqProt': 'MEDAGGGEETPAPEAP/LHPPQ/K/*/ELA/TPPEEQGLLFQEETIDLGGDEFGSEENK/ETASEGSSPLADKLNEHMMESVLISDSPNSEGDAGDLGRVRDEAEPGGEGDPGPEPAGTPSPSGEADGDCAPK/EDAAPSSGGAPRQDAAREVPGSEAAH/RPEQEPPVAEPVPVCTIFSQRAPPASGDGFEPQMVKSPSFGGASEASARTPPQVVQPSPSLSTFFGDTAASHSLASDFFDSL/FTTSAFISVSNPGAGSPAP/SASPPPLAVPGTEGRPEPVAMRGPQAAAPPASPEPFAHIQAVFAGSDDPFATALSMS/GEMDRRNDAWLPGEATRGVLRAVATQQRGAVFVDKENLTMPGLRFDNIQGDAVKDLMLRFLGEKAAAKRQVLNADSVEQSFVGLKQLISCRNWRAAVDLCGRLLTAHGQGYS/GKSE/GLLTSHTTDSLQLWFVRLALLVKLGLFQNAEMEFEPFGNLDQPDLYYEYYPHVYPGRRGSMVPFSMRILHAELQQYLGNPQESLDRLHKVKTVCSKILANLEQGLAEDGGMSSVTQEGRQASIRLWRSRLGRVMYSMANCLLLMKDYVLAVEAYHSVIKYYPEQEPQLLSGIGRISLQIGDIKTAEKYFQDVEKVTQKLDGLQGK/EIMVLMNSAFLHLGQNNFAEAHRFFTEILRMDPRNAVANNNAAVCLLYLGKLKDSLRQLEAMVQQDPRHYLHESVLFNLTTMYELESSRSMQKKQALLEAVAGKEGDSFNTQCLKLA', 'protein': None, 'transcript': u'TRAPPC12-001', 'CDS_end': 3405664, 'strand': u'+', 'end': 3405664, 'id': u'ENSE00001145941', 'start': 3405547, 'length': 117, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'TRAPPC12'}, 'error': False}, '3': {'message': 'ok', 'data': {'CDS_start': 36142145, 'chromosome': u'19', 'sequence': 'AGCACCATGGCGGAAGACA', 'frame': 0, 'number': 1, 'sequenceDbSNP': 'AGCACCATGGCGGAAGACA', 'CDS_length': 106, 'seqProt': 'MAEDMETKIKNYKTAPFDSRFPNQNQTRNCWQNYLDFHRCQKAMTAKGGDISVCEWYQRVYQSLCPTSWVTDWDEQRAEGTFPGKI', 'protein': None, 'transcript': u'COX6B1-003', 'CDS_end': 36142251, 'strand': u'+', 'end': 36142251, 'id': u'ENSE00003125961', 'start': 36142134, 'length': 117, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'COX6B1'}, 'error': False}, '2': {'message': 'ok', 'data': {'CDS_start': 48887293, 'chromosome': u'8', 'sequence': 'ATCCGCTTAGCAGAAGCCC', 'frame': 0, 'number': 14, 'sequenceDbSNP': 'ATCCGCTTAGCAGAAGCCC', 'CDS_length': 229, 'seqProt': 'MSSPASTPSRRGSRRGRATPAQTPRSEDARSSPSQRRRGEDSTSTGELQPMPTSPGVDLQSPAAQDVLFSSPPQMHSSAIPLDFDVSSPLTYGTPSSRVEGTPRSGVRGTPVRQRPDLGSA/SQKGLQVDLQSDGAAAEDIVASEQSLGQKLVIWGTDVNVAACKENFQRFLQRFIDPLAKEEENVGIDITEPLYMQRLGEINVIGEPFLNVNCEHIKSFDKNLYRQLISYPQEVIPTFDMAVNEIFFDH/RYPDSILEHQIQVRPL/FNALKTKNMRNLNPEDIDQLITISGI/MVIRTSQLIPEMQEAFFQCQVCAHTTRVEMDRGC/RIAEPSVCGRCHTTHSMALIHNRSLFSDKQMIKLQESPEDMPAGQTPHTVILFAHNDLVDKVQPGDRVNVTGIYRAVPIRVNPRVSNVKSVYKTHIDVIHYRKTDAKRLHGLDEEAEQKLFSEKRVELLKELSRKPDIYERLASALAPS/TIYEHEDIKKGILLQLFGGTRKDFSHTGRGKFRAEINILLCGDPGTSKSQLLQYVYNLVPRGQYTSGKGSSAVGLTAYVMKDPETRQLVLQTGALVLSDNGICCIDEFDKMNESTRSVLHEVMEQQTLSIAKAGIICQLNARTSVLAAANPIESQWNPKKTTIENIQLPHTLLSRFDLIFLM/LLDPQDEAYDRRLAHHLVALYYQSEEQAEEELLDMAVLKDYIAYAHSTIMPRLSEEASQALIEAYVDMRKIGSSRGMVSAYPRQLESLIRLAEAHAKVRLSNKVEAIDVEEAKRLHREALKQSATDPRTGIVDISILTTGMSATSRKRKEELAEALKKLILSKGKTPALKYQQLFEDIRGQSDIAITKDMFEEALH/RALADDDFLTVTGKTVRLL', 'protein': None, 'transcript': u'MCM4-004', 'CDS_end': 48887522, 'strand': u'+', 'end': 48887522, 'id': u'ENSE00003323524', 'start': 48887293, 'length': 229, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'MCM4'}, 'error': False}}
    return flask.jsonify(**dict)

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
    dictFile= P.parseFile(fileuploadedPath)
    #print dictFile
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

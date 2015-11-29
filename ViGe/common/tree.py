
########################################################################################################################
#script qui prend userChoice en argument et un dict
#
#ex input =>
#
#dict={'1': {'message': 'ok', 'data': {'CDS_start': None, 'chromosome': u'6', 'sequence': 'TTCCCCACGCATCTGAGGG', 'frame': None, 'number': 4, 'sequenceDbSNP': 'TTCCCCACGCATCTGAGGG', 'CDS_length': None, 'seqProt': 'N/A', 'protein': None, 'transcript': u'FLOT1-011', 'CDS_end': None, 'strand': u'-', 'end': 30698342, 'id': u'ENSE00003564703', 'start': 30698204, 'length': 138, 'genome': u'GRCh37.75', 'annotation': 'Intron', 'gene': u'FLOT1'}, 'error': False}, '0': {'message': 'ok', 'data': {'CDS_start': 3405547, 'chromosome': u'2', 'sequence': 'GGTGAAAAAGCTGCAGCAA', 'frame': 0, 'number': 2, 'sequenceDbSNP': 'GGTGAAAAAGCTGCAGCAA', 'CDS_length': 117, 'seqProt': 'MEDAGGGEETPAPEAP/LHPPQ/K/*/ELA/TPPEEQGLLFQEETIDLGGDEFGSEENK/ETASEGSSPLADKLNEHMMESVLISDSPNSEGDAGDLGRVRDEAEPGGEGDPGPEPAGTPSPSGEADGDCAPK/EDAAPSSGGAPRQDAAREVPGSEAAH/RPEQEPPVAEPVPVCTIFSQRAPPASGDGFEPQMVKSPSFGGASEASARTPPQVVQPSPSLSTFFGDTAASHSLASDFFDSL/FTTSAFISVSNPGAGSPAP/SASPPPLAVPGTEGRPEPVAMRGPQAAAPPASPEPFAHIQAVFAGSDDPFATALSMS/GEMDRRNDAWLPGEATRGVLRAVATQQRGAVFVDKENLTMPGLRFDNIQGDAVKDLMLRFLGEKAAAKRQVLNADSVEQSFVGLKQLISCRNWRAAVDLCGRLLTAHGQGYS/GKSE/GLLTSHTTDSLQLWFVRLALLVKLGLFQNAEMEFEPFGNLDQPDLYYEYYPHVYPGRRGSMVPFSMRILHAELQQYLGNPQESLDRLHKVKTVCSKILANLEQGLAEDGGMSSVTQEGRQASIRLWRSRLGRVMYSMANCLLLMKDYVLAVEAYHSVIKYYPEQEPQLLSGIGRISLQIGDIKTAEKYFQDVEKVTQKLDGLQGK/EIMVLMNSAFLHLGQNNFAEAHRFFTEILRMDPRNAVANNNAAVCLLYLGKLKDSLRQLEAMVQQDPRHYLHESVLFNLTTMYELESSRSMQKKQALLEAVAGKEGDSFNTQCLKLA', 'protein': None, 'transcript': u'TRAPPC12-001', 'CDS_end': 3405664, 'strand': u'+', 'end': 3405664, 'id': u'ENSE00001145941', 'start': 3405547, 'length': 117, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'TRAPPC12'}, 'error': False}, '3': {'message': 'ok', 'data': {'CDS_start': 36142145, 'chromosome': u'19', 'sequence': 'AGCACCATGGCGGAAGACA', 'frame': 0, 'number': 1, 'sequenceDbSNP': 'AGCACCATGGCGGAAGACA', 'CDS_length': 106, 'seqProt': 'MAEDMETKIKNYKTAPFDSRFPNQNQTRNCWQNYLDFHRCQKAMTAKGGDISVCEWYQRVYQSLCPTSWVTDWDEQRAEGTFPGKI', 'protein': None, 'transcript': u'COX6B1-003', 'CDS_end': 36142251, 'strand': u'+', 'end': 36142251, 'id': u'ENSE00003125961', 'start': 36142134, 'length': 117, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'COX6B1'}, 'error': False}, '2': {'message': 'ok', 'data': {'CDS_start': 48887293, 'chromosome': u'8', 'sequence': 'ATCCGCTTAGCAGAAGCCC', 'frame': 0, 'number': 14, 'sequenceDbSNP': 'ATCCGCTTAGCAGAAGCCC', 'CDS_length': 229, 'seqProt': 'MSSPASTPSRRGSRRGRATPAQTPRSEDARSSPSQRRRGEDSTSTGELQPMPTSPGVDLQSPAAQDVLFSSPPQMHSSAIPLDFDVSSPLTYGTPSSRVEGTPRSGVRGTPVRQRPDLGSA/SQKGLQVDLQSDGAAAEDIVASEQSLGQKLVIWGTDVNVAACKENFQRFLQRFIDPLAKEEENVGIDITEPLYMQRLGEINVIGEPFLNVNCEHIKSFDKNLYRQLISYPQEVIPTFDMAVNEIFFDH/RYPDSILEHQIQVRPL/FNALKTKNMRNLNPEDIDQLITISGI/MVIRTSQLIPEMQEAFFQCQVCAHTTRVEMDRGC/RIAEPSVCGRCHTTHSMALIHNRSLFSDKQMIKLQESPEDMPAGQTPHTVILFAHNDLVDKVQPGDRVNVTGIYRAVPIRVNPRVSNVKSVYKTHIDVIHYRKTDAKRLHGLDEEAEQKLFSEKRVELLKELSRKPDIYERLASALAPS/TIYEHEDIKKGILLQLFGGTRKDFSHTGRGKFRAEINILLCGDPGTSKSQLLQYVYNLVPRGQYTSGKGSSAVGLTAYVMKDPETRQLVLQTGALVLSDNGICCIDEFDKMNESTRSVLHEVMEQQTLSIAKAGIICQLNARTSVLAAANPIESQWNPKKTTIENIQLPHTLLSRFDLIFLM/LLDPQDEAYDRRLAHHLVALYYQSEEQAEEELLDMAVLKDYIAYAHSTIMPRLSEEASQALIEAYVDMRKIGSSRGMVSAYPRQLESLIRLAEAHAKVRLSNKVEAIDVEEAKRLHREALKQSATDPRTGIVDISILTTGMSATSRKRKEELAEALKKLILSKGKTPALKYQQLFEDIRGQSDIAITKDMFEEALH/RALADDDFLTVTGKTVRLL', 'protein': None, 'transcript': u'MCM4-004', 'CDS_end': 48887522, 'strand': u'+', 'end': 48887522, 'id': u'ENSE00003323524', 'start': 48887293, 'length': 229, 'genome': u'GRCh37.75', 'annotation': 'Exon', 'gene': u'MCM4'}, 'error': False}}
#userchoice='annotation'
#
#renvoie une liste de dictionnaire contenant des liste au format interpretable par js
#ex tree= TreeJsInput('annotation',dict)
#=> [{'name': 'annotation', 'parent': 'null', 'children': [{'name': 'Intron', 'parent': 'annotation', 'children': [{'name': '1', 'parent': 'Intron'}]}, {'name': 'Exon', 'parent': 'annotation', 'children': [{'name': '0', 'parent': 'Exon'}, {'name': '3', 'parent': 'Exon'}, {'name': '2', 'parent': 'Exon'}]}]}]
########################################################################################################################

#cette fonction prend un dictionnaire compose de 3 niveaux d'imbriquation
#et imprime tous les elements et sous element

def TreeDictBuilder(dico):
    out=[]
    x=-1
    #premier niveau key correspond au userChoice dans le code et a pour valeur un dict
    #contenant toute les possibilitees presentent dans le resultat de cette requete pour l'userChoice
    for element in dico:
        out.append(f(element,'null',[]))
        #print out

        #2eme niveau correspond a toutes les possibilite pour l'userChoice presente dans les resultats
        for elemen in dico[element]:
            out[0]['children'].append(f(elemen,element,[]))

            x+=1
            #print out

            #3eme niveau correspond a l'index des lignes rentrant dans chaque possibilite
            for eleme in dico[element][elemen]:
                #print out[0]['children'][x]
                out[0]['children'][x]['children'].append(f(eleme,elemen,None))

    return out





#fonction qui prends en arguments une string representant le choix de l'user et un dict de donnee outputee
#Les donnes outputtees sont sous le format:
#{'annotation': {'Intron': ['1'], 'Exon': ['0', '3', '2']}}
def TreeConstructorInput (userChoice, dict):
    output={}
    output[userChoice]={}
    for element in dict:
        value=dict[element]['data'][userChoice]

        if value not in output[userChoice]:
            output[userChoice][value]= []
            output[userChoice][value].append(element)
        else:
            output[userChoice][value].append(element)
    return output

###############################################################


def f(name,parent='null',children=[]):
    if children != None: #a modifier
        return {"name": name,"parent": parent,"children":children}
    else:
        return {"name": name,"parent": parent}


def TreeJsInput(userChoice,dict):
    L= TreeDictBuilder(TreeConstructorInput(userChoice,dict))
    return L




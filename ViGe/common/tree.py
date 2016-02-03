
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
        #print dict[element]
        #si input est sous format dict={'1': {'message': 'ok', 'data': {'CDS_start': None, 'chromosome': u'6',...
        #value=dict[element]['data'][userChoice]

        #si input est sous format dict={'1': {'CDS_start': None, 'chromosome': u'6',...
        try:
            value=dict[element][userChoice]

            if value not in output[userChoice]:
                output[userChoice][value]= []
                output[userChoice][value].append(element)
            else:
                output[userChoice][value].append(element)
        except:
            continue
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

'''
input={
    9: {'groupe':'sain',u'CDS_start': 20022968, 'peptide': 'AEAEAVREVY', u'protein_name': None, u'sequence': u'GCGAATCCACACAATTATGATGCATGGTTTGATTACTTGCGCTTGGTAGAAAGTGACGCAGAAGCTGAAGCCGTGAGAGAAGTCTATGAAAGGGCCATTGCCAATGTCCCACCCATTCAGGAGAAGAGGCACTGGAAGCGCTACATTTATCTTTGGATCAACTATGCACTCTATGAAGAATTGGAGGCAAAG', 'strand_mutation': '-', u'_rev': u'6648786362161', u'number': 7, u'gene_id': u'ENSG00000101343', u'CDS_length': 192, u'transcript_id': u'ENST00000536226', u'CDS_end': 20023160, 'strand': u'-', 'end_mutation': '20023103', 'enst': 'ENST00000536226', u'_id': u'Exon/6648783019825', 'end': 20023160, u'_key': u'6648783019825', u'protein_id': None, u'id': u'ENSE00003521184', 'start': 20022968, u'length': 192, 'ensg': 'ENSG00000101343', 'chromosome': u'20', u'transcript_name': u'CRNKL1-007', 'start_mutation': '20023073', u'frame': 0, u'gene_name': u'CRNKL1'},
    10:{'groupe':'sain',u'CDS_start': 41355027, 'peptide': 'AEAEKLGGQSY', u'protein_name': None, u'sequence': u'ATTGATAGGCAGCAGTTTGAAGAAACAGTTCGAACTCTAAATAACCTTTATGCAGAAGCAGAGAAGCTCGGCGGCCAGTCATATCTCGAAGGTTGTTTGGCTTGTTTAACAGCATATACCATCTTCCTATGCATGGAAACTCATTATGAGAAG', 'strand_mutation': '+', u'_rev': u'4792296906545', u'number': 2, u'gene_id': u'ENSG00000147533', u'CDS_length': 153, u'transcript_id': u'ENST00000520817', u'CDS_end': 41355180, 'strand': u'+', 'end_mutation': '41355111', 'enst': 'ENST00000520817', u'_id': u'Exon/4792293564209', 'end': 41355180, u'_key': u'4792293564209', u'protein_id': None, u'id': u'ENSE00003637833', 'start': 41355027, u'length': 153, 'ensg': 'ENSG00000147533', 'chromosome': u'8', u'transcript_name': u'GOLGA7-002', 'start_mutation': '41355078', u'frame': 0, u'gene_name': u'GOLGA7'},
    11:{'groupe':'sain',u'CDS_start': 53275147, 'peptide': 'AEAELLNLRKI', u'protein_name': None, u'sequence': u'GGCCATGCAGCTCCCATCCTCTACGCGGTCTGGGCTGAAGCTGGTTTCCTGGCCGAGGCGGAGCTGCTGAACCTGAGGAAGATCAGCTCCGACTTGGACGGGCACCCGGTCCCG', 'strand_mutation': '-', u'_rev': u'3715710230321', u'number': 3, u'gene_id': u'ENSG00000163931', u'CDS_length': 114, u'transcript_id': u'ENST00000296289', u'CDS_end': 53275261, 'strand': u'-', 'end_mutation': '53275210', 'enst': 'ENST00000296289', u'_id': u'Exon/3715706887985', 'end': 53275261, u'_key': u'3715706887985', u'protein_id': None, u'id': u'ENSE00003481595', 'start': 53275147, u'length': 114, 'ensg': 'ENSG00000163931', 'chromosome': u'3', u'transcript_name': u'TKT-201', 'start_mutation': '53275177', u'frame': 0, u'gene_name': u'TKT'},
    12:{'groupe':'sain',u'CDS_start': 56346847, 'peptide': 'AEAEQTLRF', u'protein_name': None, u'sequence': u'GCAGAGGAATTCCACTCGGTGGTACATGCCCTCTTGGAGTGGCTGGCTGAGGCGGAGCAAACCCTGCGTTTCCATGGTGTCCTCCCAGATGATGAGGATGCTCTCCGGACTCTCATTGATCAGCATAAA', 'strand_mutation': '-', u'_rev': u'4316982583089', u'number': 70, u'gene_id': u'ENSG00000151914', u'CDS_length': 129, u'transcript_id': u'ENST00000244364', u'CDS_end': 56346976, 'strand': u'-', 'end_mutation': '56346931', 'enst': 'ENST00000244364', u'_id': u'Exon/4316979240753', 'end': 56346976, u'_key': u'4316979240753', u'protein_id': None, u'id': u'ENSE00003588779', 'start': 56346847, u'length': 129, 'ensg': 'ENSG00000151914', 'chromosome': u'6', u'transcript_name': u'DST-005', 'start_mutation': '56346904', u'frame': 0, u'gene_name': u'DST'},
    13:{'groupe':'sain',u'CDS_start': 30433573, 'peptide': 'AEAFEAIPRAL', u'protein_name': None, u'sequence': u'ACATGTCCTGGACTTGAACAGTATGCTATTAAGAAGTTTGCTGAGGCATTTGAAGCTATTCCCCGCGCACTGGCAGAAAACTCTGGAGTTAAGGCCAATGAAGTAATCTCTAAACTTTATGCAGTACATCAAGAAGGAAATAAAAACGTTGGATTAGATATTGAG', 'strand_mutation': '-', u'_rev': u'7091910057777', u'number': 12, u'gene_id': u'ENSG00000156261', u'CDS_length': 165, u'transcript_id': u'ENST00000286788', u'CDS_end': 30433738, 'strand': u'-', 'end_mutation': '30433699', 'enst': 'ENST00000286788', u'_id': u'Exon/7091906715441', 'end': 30433738, u'_key': u'7091906715441', u'protein_id': None, u'id': u'ENSE00003539207', 'start': 30433573, u'length': 165, 'ensg': 'ENSG00000156261', 'chromosome': u'21', u'transcript_name': u'CCT8-003', 'start_mutation': '30433666', u'frame': 0, u'gene_name': u'CCT8'},
    14:{'groupe':'malade',u'CDS_start': 76196831, 'peptide': 'AEAGHLEGHCL', u'protein_name': None, u'sequence': u'CGTGTGCCGCTTATGGAGGGAGTGTGTGCGCAGAGTATTGCGGACCCATCGGAGCGTAACCTGGATCTCCGCAGGCCTGGCGGAGGCCGGCCACCTGGAGGGGCATTGCTTGGTTCGCGTGGTAGCAGAGGAGCTTGAG', 'strand_mutation': '+', u'_rev': u'6036859756337', u'number': 1, u'gene_id': u'ENSG00000167196', u'CDS_length': 139, u'transcript_id': u'ENST00000565036', u'CDS_end': 76196970, 'strand': u'+', 'end_mutation': '76196943', 'enst': 'ENST00000565036', u'_id': u'Exon/6036856414001', 'end': 76196970, u'_key': u'6036856414001', u'protein_id': None, u'id': u'ENSE00003552363', 'start': 76196831, u'length': 139, 'ensg': 'ENSG00000167196', 'chromosome': u'15', u'transcript_name': u'FBXO22-006', 'start_mutation': '76196910', u'frame': 1, u'gene_name': u'FBXO22'},
    15:{'groupe':'malade',u'CDS_start': 48887293, 'peptide': 'AEAHAKVRL', u'protein_name': None, u'sequence': u'GCTTATGTAGACATGAGGAAGATTGGCAGTAGCCGGGGAATGGTTTCTGCATACCCTCGACAGCTAGAGTCATTAATCCGCTTAGCAGAAGCCCATGCTAAAGTAAGATTGTCTAACAAAGTTGAAGCCATTGATGTGGAAGAGGCCAAACGCCTCCATCGGGAAGCTCTGAAGCAGTCTGCAACTGATCCCCGGACTGGCATCGTGGACATATCTATTCTTACTACGG', 'strand_mutation': '+', u'_rev': u'4801728847665', u'number': 14, u'gene_id': u'ENSG00000104738', u'CDS_length': 229, u'transcript_id': u'ENST00000523944', u'CDS_end': 48887522, 'strand': u'+', 'end_mutation': '48887404', 'enst': 'ENST00000523944', u'_id': u'Exon/4801725505329', 'end': 48887522, u'_key': u'4801725505329', u'protein_id': None, u'id': u'ENSE00003323524', 'start': 48887293, u'length': 229, 'ensg': 'ENSG00000104738', 'chromosome': u'8', u'transcript_name': u'MCM4-004', 'start_mutation': '48887377', u'frame': 0, u'gene_name': u'MCM4'},
    16:{'groupe':'malade',u'CDS_start': 127339540, 'peptide': 'AEAHARIHL', u'protein_name': None, u'sequence': u'GCGACAGGCAGCATCCCCATTACGGTGCGGCACATCGAGTCCATGATCCGCATGGCGGAGGCCCACGCGCGCATCCATCTGCGGGACTATGTGATCGAAGACGACGTCAACATGGCCATCCGCGTGATGCTGGAGAGCTTCATAGACACACAGAAGTTCAGCGTCATGCGCAGCATGCGCAAG', 'strand_mutation': '+', u'_rev': u'3777082203953', u'number': 13, u'gene_id': u'ENSG00000073111', u'CDS_length': 183, u'transcript_id': u'ENST00000265056', u'CDS_end': 127339723, 'strand': u'+', 'end_mutation': '127339621', 'enst': 'ENST00000265056', u'_id': u'Exon/3777078861617', 'end': 127339723, u'_key': u'3777078861617', u'protein_id': None, u'id': u'ENSE00003643982', 'start': 127339540, u'length': 183, 'ensg': 'ENSG00000073111', 'chromosome': u'3', u'transcript_name': u'MCM2-001', 'start_mutation': '127339594', u'frame': 0, u'gene_name': u'MCM2'}
}

print TreeJsInput('groupe',input)
'''
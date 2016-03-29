
import random

########################################################################################################################
#script qui prend userChoice en argument et un dict
#
#ex input =>
#

#fonction qui produit l'input pout generer un pie chart
#si pour un noeud il n'y a pas de child => value == 100

def listOccurencePie (dictCol):
    listPie = []
    dictIndexlistPieColor = {}
    counter = 0
    for item in dictCol.values():
        listPie.append({'value':0,'color':item})
        dictIndexlistPieColor[item] = counter
        counter+=1

    #print listPie # liste a assigner a chaque noeud
    #print dictIndexlistPieColor #index des couleurs dans la liste precedente
    return listPie,dictIndexlistPieColor

def bakePieChart(out, dictCol):

    dictIndexlistPieColor = listOccurencePie(dictCol)[1]



    for root in out:
        root['pie'] = listOccurencePie(dictCol)[0]

        for groupParameter in root['_children']:
            #print groupParameter['color']
            groupParameter['pie']= listOccurencePie(dictCol)[0]

            #on regarde si le niveau des possibilite pour ce parametre est splite
            if '-' in groupParameter['name']:

                #le niveau des possibilite pour ce parametre est splite
                for nodeparameter in groupParameter['_children']:
                    nodeparameter['pie']= listOccurencePie(dictCol)[0]
                    #print nodeparameter['color']

                    for groupnode in nodeparameter['_children']:
                        groupnode['pie']= listOccurencePie(dictCol)[0]
                        #print groupnode['color']
                        #on regarde si le niveau des tabrow est splite
                        if len(groupnode['_children'])>0:

                            #le niveau des tabrow est splite
                            for node in groupnode['_children']:
                                node['pie']= listOccurencePie(dictCol)[0]
                                #print dictIndexlistPieColor[node['color']]
                                #print node['color']
                                #on ajoute +1 au compteur de cette couleur dans les noeuds sup



                                node['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                                groupnode['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                                nodeparameter['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                                groupParameter['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                                root['pie'][dictIndexlistPieColor[node['color']]]['value']+=1

                        else:
                            #le niveau des possibilite n'est pas splite
                            #print dictIndexlistPieColor[groupnode['color']]
                            #print groupnode['color']
                            #on ajoute +1 au compteur de cette couleur dans les noeuds sup

                            groupnode['pie'][dictIndexlistPieColor[groupnode['color']]]['value'] +=1
                            nodeparameter['pie'][dictIndexlistPieColor[groupnode['color']]]['value']+=1
                            groupParameter['pie'][dictIndexlistPieColor[groupnode['color']]]['value']+=1
                            root['pie'][dictIndexlistPieColor[groupnode['color']]]['value']+=1

            else:
                #le niveau des possibilite n'est pas splite
                for groupnode in groupParameter['_children']:
                    groupnode['pie']= listOccurencePie(dictCol)[0]
                    #print groupnode['color']
                    #on regarde si le niveau des tabrow est splite
                    if len(groupnode['_children'])>0:
                        #le niveau des tabrow est splite
                        for node in groupnode['_children']:
                            node['pie']= listOccurencePie(dictCol)[0]
                            #print dictIndexlistPieColor[node['color']]
                            #print node['color']

                            node['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                            groupnode['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                            groupParameter['pie'][dictIndexlistPieColor[node['color']]]['value']+=1
                            root['pie'][dictIndexlistPieColor[node['color']]]['value']+=1

                    else:
                        #le niveau des tabrow n'est pas splite
                        #print dictIndexlistPieColor[groupnode['color']]
                        #print groupnode['color']

                        groupnode['pie'][dictIndexlistPieColor[groupnode['color']]]['value']+=1
                        groupParameter['pie'][dictIndexlistPieColor[groupnode['color']]]['value']+=1
                        root['pie'][dictIndexlistPieColor[groupnode['color']]]['value']+=1

    return out


def printLeaf(inpt):

    print inpt
    for item in inpt:
        print '#'*50
        print item
        print '#'*50

        for element in inpt[item]:
            for it in inpt[item][element]:
                print '####', it['color']


        '''
        if len(inpt[item]['_children'])>0:
            printLeaf(item['_children'])

        else:
            print item['name'],item['color']
        '''
    return




#fourni la liste des feuilles qu'il ne reste plus qu'a ajouter au dernier niveau de l'arbre dans un dict

def listOut (dictInput, dict_input=None, parameter = None, dictCol=None):


    out = {}
    for root in dictInput:
        for possibilite in dictInput[root]:
            out[possibilite] = []
            for i in range (0, len(dictInput[root][possibilite])):

                if type (dictInput[root][possibilite][i]) == type([]):

                    sublist = []
                    for v in range (0, len(dictInput[root][possibilite][i])):

                        if parameter is None:
                            sublist.append(f(dictInput[root][possibilite][i][v], nameList(dictInput[root][possibilite][i]), [],layer ='null'))

                        else:
                            try:
                                #print '### int', eleme
                                dict_input_key = dict_input[int(dictInput[root][possibilite][i][v])]
                            except:
                                #print '### string', elem
                                dict_input_key = dict_input[str(dictInput[root][possibilite][i][v])]

                            color = None
                            #on fait la comparaison et on imprime si c'est bon
                            if parameter in dict_input_key.keys():
                                color = str(dictCol[dict_input_key[parameter]])

                            sublist.append(f(dictInput[root][possibilite][i][v], nameList(dictInput[root][possibilite][i]), [], color = color,layer=parameter))
                    out[possibilite].append(f(nameList(dictInput[root][possibilite][i]), possibilite, sublist,layer=parameter))

                else:

                    if parameter is None:
                        out[possibilite].append(f(dictInput[root][possibilite][i], possibilite, [],layer ='null'))

                    else:
                        try:
                            #print '### int', eleme
                            dict_input_key = dict_input[int(dictInput[root][possibilite][i])]
                        except:
                            #print '### string', elem
                            dict_input_key = dict_input[str(dictInput[root][possibilite][i])]

                        color = None
                        #on fait la comparaison et on imprime si c'est bon
                        if parameter in dict_input_key.keys():
                            color = str(dictCol[dict_input_key[parameter]])
                        out[possibilite].append(f(dictInput[root][possibilite][i], possibilite, [],color = color,layer=parameter))

    return out
########################################################################################################################

# fonction permet de fournir la couleur des noeuds dans le cadre ou on applique un calque
def makeDictColor(dict):
    '''
    A partir d'un output de TreeConstructorInput fait sur le parametre desire
    exemples d'input
    {'strand': {'+': [1, 4, 5, 7, 95, 96], u'-': [  91, 93, 94, 97, 98]}}
    '''

    item=[]
    for it in dict[dict.keys()[0]]:
        item.append(it)

    #cette liste contient toutes les couleurs possibles pour l'arbre
    listColor=['#fee0d2','#efedf5','#bcbddc','#de2d26','#756bb1','#fee6ce','#fdae6b','#e6550d','#fc9272','#f0f0f0','#bdbdbd','#636363','#e5f5e0','#a1d99b','#31a354','#deebf7','#9ecae1','#3182bd']
    random.shuffle(listColor)

    dictColor = {}
    for i in range(0, len(item)):
        # le 18 dans [i%18]correspond a len(listcolor)
        dictColor[item[i]] = listColor[i%18]

    #print dictColor
    return dictColor

#cette fonction prend une liste en parametre et retourne une liste de liste dont la longueur max est 10
def splitList(seq,out=[]):
    #print 'seq',seq
    out=out
    n = len(seq)
    if n <= 10:
        # here the recursion stops, do your stuff with the sequence
        out.append(seq)
        return

    a = splitList(seq[:n/2],out=out)
    b = splitList(seq[n/2:],out=out)
    # combine the answer from both subsequences
    return out

def nameList(list):
    return str(list[0])+'-'+str(list[len(list)-1])


#cette fonction est un contructeur de noeud
#mettre ici les attributs que l'on veut que nos noeuds possedent
def f(name,parent=None,children=[],color="orange",layer=None):

    if layer is None:
        layer = 'null'

    if children != None: #a modifier
        return {"name": name,"parent": parent,"_children":children, 'children_length':len(children), 'color':color, 'layer':layer, "pie" : [] }
    else:
        return {"name": name,"parent": parent, 'color':color,'layer':layer, "pie" : [] }


#cette fonction prend un dictionnaire compose de 3 niveaux d'imbriquation
#et imprime tous les elements et sous element

def splitDictKeyList(l,root,parameter):

        #pour les listes mixtes on separe les int des alpha
        int = []
        alpha = []

        #on test pour chaque item si c'est une liste ou un int
        for item in l:
            try:
                float(item)
                int.append(item)
            except:
                alpha.append(str(item))

        int.sort(key=float)
        alpha.sort(key=str)
        #maintenant nous avons 2 listes triee

        if len(int)>=10:
            int = splitList(int,out=[])
        else:
            if len(int)!=0:
                int = [int]
        if len(alpha)>=10:
            alpha = splitList(alpha,out=[])
        else:
            if len(alpha)!=0:
                alpha = [alpha]


        if root == 'chromosome':
            int = sorted(int)
            for list in alpha:
                for chro in list:
                    int[len(int)-1].append(chro)
            out = int
        else:
            out = sorted(int+alpha)

        return out




def TreeDictBuilder(dicoInput, dict_input, parameter=None, dicoParameter=None, dictCol=None):

    #print 'pppppppppppppp',dicoParameter

    splitFeuille = False

    #on regarde si la longueur des feuilles est > a 10
    for root in dicoInput:
        for possibilites in dicoInput[root]:
            if len(dicoInput[root][possibilites])>10:
                dicoInput[root][possibilites] = splitDictKeyList(dicoInput[root][possibilites],root,parameter)
                splitFeuille = True

    listLeaf = listOut(dicoInput,dict_input,parameter,dictCol)




    out=[]
    x=-1

    #premier niveau key correspond au userChoice dans le code et a pour valeur un dict
    #contenant toute les possibilitees presentent dans le resultat de cette requete pour l'userChoice
    for root in dicoInput:
        out.append(f(root,'null',[], layer = parameter))

        #print '#'*200
        #print '#'*200

        #est ce que la length du premier niveau est > 10 et doit etre splitte?
        if len(dicoInput[root].keys()) > 10 :
            lists = splitDictKeyList(dicoInput[root].keys(),root,parameter)
            for list in lists:
                #print list
                out[0]['_children'].append(f(nameList(list),root, layer = parameter))
                out[0]['children_length']+=1

            w=0
            wo=[]
            for list in lists:
                i=[]
                for item in list:
                    print list
                    print '#'*200
                    print item
                    i.append(f(item,nameList(list),listLeaf[str(item)], layer = parameter))
                wo.append(f(nameList(list),root,i))
                out[0]['_children'][w]['children_length']+=1
                out[0]['_children']=wo
                w+=1

        else :
            listePossibilites = []
            for possibilites in dicoInput[root]:
                out[0]['children_length'] += 1
                print listLeaf
                print '#'*200
                print possibilites
                print '#'*200
                print listLeaf[str(possibilites)]
                print '#'*200
                listePossibilites.append(f(possibilites, root, listLeaf[str(possibilites)]))
            out[0]['_children'] = listePossibilites


    #l'arbre est termine
    #Maintenant on ajoute les valeurs du pie chart pour chaque noeud si parameter
    if parameter:
        out = bakePieChart(out,dictCol)



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

# cette fonction genere un dict a partir d'une liste
def listToDict(dict):
    d={}
    x=1
    for item in dict:
       d[x]=item
       x+=1
    return d

def TreeJsInput(userChoice,liste,parameter=None):
    #on transforme la liste de l'input en dict
    dict=listToDict(liste)

    if parameter is not None:
        dictParameter=TreeConstructorInput (parameter, dict)
        #on fait ensuite rouler l'algorithme dessus
        dictCol= makeDictColor(dictParameter)

        L= TreeDictBuilder(TreeConstructorInput(userChoice,dict),dict,parameter,dictParameter,dictCol)

    else:
        L= TreeDictBuilder(TreeConstructorInput(userChoice,dict),dict)

    return L

###############################################################

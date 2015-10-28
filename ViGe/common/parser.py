__author__ = 'schwartzl'

def parseURL( input_data, separator = '%20'):
    #l'input est une chaine de caracteres sortis de l'URL
    # format: chr1%20pos1%20chr2%20pos2...



    #split l'input en fonction des espaces
    if ' ' in input_data:
        lines=input_data.split(" ")
    #sinon split l'input en fonction du "separator"
    elif separator in input_data:
        lines=input_data.split(separator)
    data={}

    #formate chaque lignes de sorte a faire ressortir le chr et la position
    #format : [chr1,pos1,chr2,pos2,...]

    x=0
    while x < len(lines):
        if lines[x]!='':
            #on regarde si c'est une cle=chr ou une value=pos
            #on utilise le modulo pour associer chaque position a son chromosome
            if x%2==0:
                #verifie si le chromosome (lines[x]) est une cle de data, si oui on append sa liste sinon on cree cette cle
                if lines[x] not in data.keys():
                    data[str(lines[x])]=[]

                #puis on append la liste de ce chromosome pour ajouter la nouvelle position
                try:
                    data[lines[x]].append(int(lines[x+1]))
                except:
                    print ('erreur format')
            x+=1

        #ex format data renvoye
        # {'Y': [2655643,656435],'13':[2556463,365645,564564]}

    return data




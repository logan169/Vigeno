__author__ = 'schwartzl'


def parseFile( filePath, separator = '\t', lineseparator='\n'):

    #ouvre le fichier
    filename = filePath
    f = open(filename)
    lines = f.readlines()
    data={}


    #formate chaque lignes de sorte a faire ressortir le chr et la position
    for line in lines:
        line=line.replace(lineseparator,"")
        line=line.replace("\'","")
        line=line.replace("\"","")
        line=line.replace(" ","")

        if line !='':

            if '\t'in line:
                line=line.split(separator)

            elif ' ' in line:
                line = line.split(' ')
                if len(line)>2:
                    print 'errrrooooor!!!!!'

            elif '%' in line:
                line = line.split('%')
                if len(line)>2:
                    print 'errrrooooor!!!!!!!!!'

            else:
                print ('errrrooooor!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

            #verifie si le chr de line est une cle de data, si oui on append sa liste sinon on cree cette cle et on append la liste
            if line[0] not in data.keys():
                data[str(line[0])]=[]
            data[line[0]].append(line[1])
    f.close()
    return data




def parseURL( input_data, separator = '%20'):

    #split l'input
    if ' ' in input_data:
        lines=input_data.split(" ")

    if separator in input_data:
        lines=input_data.split(separator)

    data={}



    #formate chaque lignes de sorte a faire ressortir le chr et la position
    x=0

    while x < len(lines):
        #on regarde si c'est une cle=chr ou une value=pos

        if lines[x]!='':

            if x%2==0:
                #verifie si le chr de line est une cle de data, si oui on append sa liste sinon on cree cette cle et on append la liste
                if lines[x] not in data.keys():
                    data[str(lines[x])]=[]
                try:
                    data[lines[x]].append(int(lines[x+1]))
                except:
                    print ('erreur format')

            x+=1
    return data




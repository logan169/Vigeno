

l=[]

for x in range (0,100):
    l.append(x)

print l
print '#'*20

def splitList(seq,out=[]):
    out=out
    n = len(seq)
    if n <= 10:
        # here the recursion stops, do your stuff with the sequence
        out.append(seq)
        return
    a = splitList(seq[:n/2])
    b = splitList(seq[n/2:])
    # combine the answer from both subsequences
    return out


def nameList(list):
    print str(list[0])+'-'+str(item[len(list)-1])



listColor=[{'background-color':'#0f0'},{'background-color':'#fff'},{'background-color':'#ffffcc'},{'background-color':'#0074D9'},{'background-color':'#7FDBFF'},{'background-color':'#39CCCC'},{'background-color':'#3D9970'},{'background-color':'#2ECC40'},{'background-color':'#01FF70'},{'background-color':'#FFDC00'},{'background-color':'#FF851B'},{'background-color': 'red'},{'background-color':'#9966ff'},{'background-color':'#F012BE'},{'background-color':'#B10DC9'},{'background-color':'#AAAAAA'},{'background-color':'#DDDDDD'},{'background-color':'palegoldenrod'},{'background-color':'royalblue'},{'background-color':'#c7996b'},{'background-color':'SILVER'},{'background-color':'#ffcce6'},{'background-color':'salmon'}]

print len(listColor)

##############################################################################
import random

def randCol():
    r = random.randrange(0,250)
    g = random.randrange(0,250)
    b = random.randrange(0,250)
    return 'rgb('+str(r)+','+str(g)+','+str(b)+')'


item=["l","p","c",'j','5','8','p']

dictColor={}
for i in range (0, len(item)):
    dictColor[item[i]] = randCol()

print dictColor

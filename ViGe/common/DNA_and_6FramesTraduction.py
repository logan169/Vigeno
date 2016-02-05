
from pyGeno.tools.UsefulFunctions import *

#
#Ce script prend une sequence d'adn en input, => 'acgatgctacgagct'
#Il retourne un dictionnaire composee


def DNA_and_6FramesTraduction(seq):
    print seq
    try:
        seq=seq.upper()
    except:
        pass

    outputDict={}
    DNAs=[seq, seq[1:], seq[2:], reverseComplement(seq), reverseComplement(seq)[1:], reverseComplement(seq)[2:]]

    translation=translateDNA_6Frames(sequence=seq)
    frames = ["f1", "f2", "f3", "r1", "r2", "r3"]

    for frame, DNA, AA in zip(frames, DNAs, translation ) :
        outputDict[frame] = ({ "DNA" : DNA, "AA" : AA})

    return outputDict


'''
l=DNA_and_6FramesTraduction(complement('CGATTCGGAGGATATAGTTTT'),'+')
m=DNA_and_6FramesTraduction(complement('CGATTCGGAGGATATAGTTTT'),'-')

for element in l:
    print element,l[element],m[element]
'''
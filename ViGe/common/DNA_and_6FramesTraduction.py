
from pyGeno.tools.UsefulFunctions import *

#
#Ce script prend une sequence d'adn en input, => 'acgatgctacgagct'
#Il retourne un dictionnaire composee


def DNA_and_6FramesTraduction(seq):
    seq=seq.upper()
    outputDict={}

    seqf1=seq
    seqf2=seq[1:]
    seqf3=seq[2:]
    seqr1=reverseComplement(seq)
    seqr2=reverseComplement(seq)[1:]
    seqr3=reverseComplement(seq)[2:]

    translation=translateDNA_6Frames(sequence=seq)

    outputDict['f1']=[seqf1,translation[0]]
    outputDict['f2']=[seqf2,translation[1]]
    outputDict['f3']=[seqf3,translation[2]]
    outputDict['r1']=[seqr1,translation[3]]
    outputDict['r2']=[seqr2,translation[4]]
    outputDict['r3']=[seqr3,translation[5]]
    return outputDict


from pyGeno.tools.UsefulFunctions import *

#
#Ce script prend une sequence d'adn en input, => 'acgatgctacgagct'
#Il retourne un dictionnaire composee


def DNA_and_6FramesTraduction(seq):
    seq=seq.upper()
    outputListe=[]

    seqf1=seq
    seqf2=seq[1:]
    seqf3=seq[2:]
    seqr1=reverseComplement(seq)
    seqr2=reverseComplement(seq)[1:]
    seqr3=reverseComplement(seq)[2:]

    translation=translateDNA_6Frames(sequence=seq)

    outputListe.append([seqf1,translation[0]])
    outputListe.append([seqf2,translation[1]])
    outputListe.append([seqf3,translation[2]])
    outputListe.append([seqr1,translation[3]])
    outputListe.append([seqr2,translation[4]])
    outputListe.append([seqr3,translation[5]])
    return outputListe
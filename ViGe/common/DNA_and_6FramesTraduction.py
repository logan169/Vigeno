
from pyGeno.tools.UsefulFunctions import *

#
#Ce script prend une sequence d'adn en input, => 'acgatgctacgagct'
#Il retourne un dictionnaire composee


def DNA_and_6FramesTraduction(seq,ref_strand,frame):

    try:
        seq=seq.upper()
    except:
        pass


    print frame

    if ref_strand == '+':
        frames = ["f1", "f2", "f3", "r1", "r2", "r3"]

    elif ref_strand == '-':
        frames = ["f1", "f2", "f3", "r1", "r2", "r3"]
        #frames = [ "r1", "r2", "r3","f1", "f2", "f3"]


    outputDict={}


    DNAs=[seq, seq[1:], seq[2:], reverseComplement(seq), reverseComplement(seq)[1:], reverseComplement(seq)[2:]]
    
    print DNAs

    if ref_strand == '-':
        DNAs=[seq, seq[1:], seq[2:], reverseComplement(seq), reverseComplement(seq)[1:], reverseComplement(seq)[2:]]
    print DNAs

    translation=translateDNA_6Frames(sequence=seq)

    for f, DNA, AA in zip(frames, DNAs, translation ) :

        outputDict[f] = ({ "DNA" : DNA, "AA" : AA})

    return outputDict



from pyGeno.tools.UsefulFunctions import *

#
#Ce script prend une sequence d'adn en input, => 'acgatgctacgagct'
#Il retourne un dictionnaire composee


def DNA_and_6FramesTraduction(seq,ref_strand):

    try:
        seq=seq.upper()
    except:
        pass


    print seq

    if ref_strand == '+':
        frames = ["f1", "f2", "f3", "r1", "r2", "r3"]
        pass

    elif ref_strand == '-':

        frames = ["r1", "r2", "r3","f1", "f2", "f3"]
        pass

    print seq

    outputDict={}
    DNAs=[seq, seq[1:], seq[2:], reverseComplement(seq), reverseComplement(seq)[1:], reverseComplement(seq)[2:]]

    translation=translateDNA_6Frames(sequence=seq)

    for frame, DNA, AA in zip(frames, DNAs, translation ) :
        outputDict[frame] = ({ "DNA" : DNA, "AA" : AA})

    return outputDict


'''
DNA_and_6FramesTraduction("TACTGCCCTATCGGTTGAAAAGACAAG",'+')
DNA_and_6FramesTraduction("TACTGCCCTATCGGTTGAAAAGACAAG",'-')
'''

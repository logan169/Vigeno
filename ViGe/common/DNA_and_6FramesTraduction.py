
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
        if frame == '0':
            frames = ["f1", "f2", "f3", "r1", "r2", "r3"]

        elif frame == '1':
            frames = ["f3","f1", "f2", "r3", "r1", "r2" ]

        elif frame == '2':
            frames = [ "f1","f2", "f3","r1",  "r2", "r3"]



    elif ref_strand == '-':
        if frame == '0':
            frames = [ "r1", "r2", "r3","f1", "f2", "f3"]

        elif frame == '1':
            frames = [ "r2","r1","r3", "f1","f2","f3" ]

        elif frame == '2':
            frames = [  "r2", "r3","r1", "f2", "f3","f1"]




    outputDict={}


    DNAs=[seq, seq[1:], seq[2:], reverseComplement(seq), reverseComplement(seq)[1:], reverseComplement(seq)[2:]]
    #if ref_strand == '-':
    #    DNAs=[seq[::-1], seq[1:][::-1], seq[2:][::-1], reverseComplement(seq)[::-1], reverseComplement(seq)[1:][::-1], reverseComplement(seq)[2:]][::-1]


    translation=translateDNA_6Frames(sequence=seq)

    for f, DNA, AA in zip(frames, DNAs, translation ) :

        outputDict[f] = ({ "DNA" : DNA, "AA" : AA})

    return outputDict

print DNA_and_6FramesTraduction('TCTCCATAATCACGGATAAACAATTCT','-','1')



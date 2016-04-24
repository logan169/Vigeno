__author__ = 'schwartzl'
import random

file = open('pep_pep_pep.csv','r')
out = open('pep_pep_pep_out1.csv','a')

for line in file:
    line = line.rstrip()
    r = random.random()

    if r > 0.75:
        if r > 0.88:
            #print ',cancer'
            line+=',cancer\n'
        else:
            #print 'control'
            line+=',control\n'
    else:
        #print 'common'
        line+=',common\n'
    print line
    out.write(line)

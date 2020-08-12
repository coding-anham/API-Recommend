import RNA
import random
import numpy as np
from hyperparams import *

"""
for i in range(10):
    f = open(PAIRS_PATH["rand"][i], 'w')
    for j in range(1000):
        f.write(str(j) + ',' + results[j] + '\n')
    f.close()
"""

chromosomes = []
scores = np.zeros(10000)

def makeCh():
    global  chromosomes
    APT_pool = "ACGU"
    seq = ""
    chromosomes = []
    # length - 10 , 10000 seq
    for i in range(10000):
        for j in range(10):
            seq += random.choice(APT_pool)
        chromosomes.append(seq)
        seq = ""

def eval():
    global chromosomes, scores
    scores = np.zeros(10000)

    for i in range(10000):
        seq = chromosomes[i]
        (ss, mfe) = RNA.fold(seq)
        # cond#1 3 consecutive base pairs

        # cond#2 free Energy <= -5.7
        if mfe <= -5.7:
            scores[i] += 1
        # cond#3 11 unpaired base


def main():
    global chromosomes
    makeCh()

if __name__ == '__main__':
    main()
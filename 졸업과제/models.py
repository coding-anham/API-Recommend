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
new_chroms = []
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
        if ss[0] == ".":
            if ss[1] == "(" and ss[2] == "(" and ss[3] == "(":
                if ss[-1] == "." and ss[-2] == ")" and ss[-3] == ")" and ss[-4] == ")":
                    scores[i] += 1
                if ss[-1] == ")" and ss[-2] == ")" and ss[-3] == ")":
                    scores[i] += 1
        if ss[0] == "(":
            if ss[1] == "(" and ss[2] == "(":
                if ss[-1] == "." and ss[-2] == ")" and ss[-3] == ")" and ss[-4] == ")":
                    scores[i] += 1
                if ss[-1] == ")" and ss[-2] == ")" and ss[-3] == ")":
                    scores[i] += 1

        # cond#2 free Energy <= -5.7
        if mfe <= -5.7:
            scores[i] += 1

        # cond#3 11 unpaired base
        for i in range(27):
            base = 0
            if ss[i] == ".":
                base += 1
        if base>11 :
            scores += (base-11)
            #scores += 1
            #scores += (base-11)/2.0

def selection():
    global chromosomes, scores, new_chroms
    selected = 0
    max = np.max(scores)
    while(selected != 100):
        for i in range(1000):
            if scores[i] == max and selected<100:
                new_chroms.append(chromosomes[i])
                selected += 1
        max -= 1

def crossover():
    global chromosomes, scores, new_chroms
    parent1 = new_chroms[:50]
    parent2 = new_chroms[50:]

    str_len = len(parent1[0])

    for i in range(50):
        child1 = parent1[:str_len/2] + parent2[str_len/2:]
        child2 = parent2[:str_len/2] + parent1[str_len/2:]
        new_chroms.append(child1)
        new_chroms.append(child2)


def main():
    global chromosomes
    makeCh()

if __name__ == '__main__':
    main()
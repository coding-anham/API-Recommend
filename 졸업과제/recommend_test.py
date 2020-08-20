import pickle
from hyperparams import *
from random_APT import *
import numpy as np
import pandas as pd

imsi = []
last = []
def getResult():

    RFC_A = pickle.load(open(PIC_PATH["mix_randomForests"], 'rb'))
    positive = 0

    for i in range(0,29):
        Results = []
        Train_A = np.load(NPZ_PATH["genetic"][i])
        Train_P = np.load(NPZ_PATH["protein"])

        X_A = Train_A['XA']
        X_P = Train_P['XP']

        Train = np.concatenate((X_P, X_A), axis=-1)
        pdA = RFC_A.predict(Train)

        pair_path = PAIRS_PATH["genetic"][i]
        f = open(pair_path, 'r')
        lines = f.readlines()
        for j in range(100000):
            if pdA[j]==1 :
                target_data = lines[j].split(",")[1]
                Result = target_data[:-1]
                Results.append(Result)
                positive += 1
        f.close()
        print(Results)
        print(Results[0])

    print("positive: " + str(positive))
    return Results

def recommend100(imsi):
    genetic_apt_arr = getResult()
    print(len(genetic_apt_arr))
    scores = np.zeros(len(genetic_apt_arr))
    for i in range(len(genetic_apt_arr)):
        str_len = len(genetic_apt_arr[i])
        (ss, mfe) = RNA.fold(genetic_apt_arr[i])
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
        for i in range(str_len):
            base = 0
            if ss[i] == ".":
                base += 1
        if base >= 11:
            scores[i] += 1


    for i in range(len(genetic_apt_arr)):
        imsi.append((genetic_apt_arr[i], scores[i]))
    imsi = sorted(imsi, key=lambda imsi : imsi[1], reverse=True)

    for i in range(100):
        last.append(imsi[i][0])
    print(last)


if __name__ == "__main__":
    recommend100(imsi)
"""
def check(pdA: object, rand_apt) -> object:
    rst = np.where(pdA == 1)
    apt_list = ""
    X = []

    for i in rst:
        temp = rand_apt[i-1]
        apt_list = ""
        for j in temp:
            tmp = np.array_str(j)
            tmp = tmp.split(" ")
            apt = ''.join(tmp[1])
            apt = apt.translate({ord(i): None for i in ']'})
            apt = apt.translate({ord(i): None for i in '\''})
            X.append(apt)

    return X

for i in range(10):
    Train_A = np.load(NPZ_PATH["rand"][i])
    Train_P = np.load(NPZ_PATH["protein"])

    X_A = Train_A['XA']
    X_P = Train_P['XP']

    Train = np.concatenate((X_P, X_A), axis=-1)

    pdA = RFC_A.predict(Train)
    print("A {}".format(pdA))
"""
"""
for j in range(100):
    for i in range(100):
        print(str(pdA[j*100+1]), end=' ')
    print(" ")


"""
import pickle
from hyperparams import *
from random_APT import *
import numpy as np
import pandas as pd

def getResult():

    RFC_A = pickle.load(open(PIC_PATH["mix_randomForests"], 'rb'))
    positive = 0

    for i in range(20,30):
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
        #print(Results)

    print("positive: " + str(positive))

if __name__ == "__main__":
    getResult()
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
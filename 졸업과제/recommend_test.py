import pickle
from hyperparams import *
import numpy as np
import random

imsi = []

def getResult():

    RFC_A = pickle.load(open(PIC_PATH["mix_randomForests"], 'rb'))
    positive = 0
    Results = []

    for i in range(10,19):
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

    print("positive: " + str(positive))
    return Results

def recommend100(imsi):
    genetic_apt_arr = getResult()
    print("len: " + str(len(genetic_apt_arr)))
    scores = np.zeros(len(genetic_apt_arr))

    test = []
    for i in range(100):
        insert_num = random.randint(0,len(genetic_apt_arr)-1)
        while insert_num in test:
            insert_num = random.randint(0,len(genetic_apt_arr)-1)
        test.append(insert_num)
        imsi.append(genetic_apt_arr[insert_num])

    for i in range(100):
        print("Number " + str(i) + " : " + str(imsi[i]))


if __name__ == "__main__":
    recommend100(imsi)

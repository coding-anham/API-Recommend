import pickle
from hyperparams import *
import numpy as np

RFC_A = pickle.load(open(PIC_PATH["mix_randomForests"], 'rb'))


for i in range(10):
    Train_A = np.load(NPZ_PATH["rand"][i])
    Train_P = np.load(NPZ_PATH["protein"])

    X_A = Train_A['XA']
    X_P = Train_P['XP']

    Train = np.concatenate((X_P, X_A), axis=-1)

    pdA = RFC_A.predict(Train)

    print("A {}".format(pdA))
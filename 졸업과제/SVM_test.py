#!/usr/bin/env python
# coding: utf-8

import numpy as np
from sklearn import svm


A_train = np.load('npz/API_A_train.npz')
RPI = np.load('npz/RPI488.npz')

A_XP = A_train['XP']
A_XA = A_train['XR']
A_Y = A_train['Y']

R_XP = RPI['XP']
R_XR = RPI['XR']
R_Y = RPI['Y']

print(len(A_XP))
print(len(A_XA))
print(len(A_Y))

print(len(R_XP))
print(len(R_XR))
print(len(R_Y))


X = []

for i in range(5):
    temp = [R_XP[i], R_XR[i]]
    X.append(temp)

X_np = np.array(X)
X_np.shape
print("{}".format(X_np))








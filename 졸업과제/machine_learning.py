import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score

def svm():
    A_train = np.load('npz/API_B_train.npz')

    A_XP = A_train['XP']
    A_XA = A_train['XR']
    A_Y = A_train['Y']

    A_XP = np.array(A_XP)
    A_XA = np.array(A_XA)

    X_train = np.concatenate((A_XP, A_XA), axis=-1)
    Y_train = np.array(A_Y)

    clf = SVC()
    clf.fit(X_train, Y_train)
    print(clf)

    A_test = np.load('npz/API_B_test.npz')
    T_XP = A_test['XP']
    T_XA = A_test['XR']
    T_Y = A_test['Y']

    T_XP = np.array(T_XP)
    T_XA = np.array(T_XA)

    X_test = np.concatenate((T_XP, T_XA), axis=-1)
    Y_test = np.array(T_Y)

    #Y_predict = clf.predict(X_test)

    scores = cross_val_score(clf, X_test, Y_test, cv=5)

    print(Y_train.shape)
    print(Y_test.shape)

    #print(classification_report(Y_predict, Y_test))
    print("{}".format(scores))

def randomForests():
    A_train = np.load('npz/API_B_train.npz')

    A_XP = A_train['XP']
    A_XA = A_train['XR']
    A_Y = A_train['Y']

    A_XP = np.array(A_XP)
    A_XA = np.array(A_XA)

    X_train = np.concatenate((A_XP, A_XA), axis=-1)
    Y_train = np.array(A_Y)

    clf = RandomForestClassifier(n_estimators=100, criterion="entropy")
    clf = clf.fit(X_train, Y_train)

    A_test = np.load('npz/API_B_test.npz')
    T_XP = A_test['XP']
    T_XA = A_test['XR']
    T_Y = A_test['Y']

    T_XP = np.array(T_XP)
    T_XA = np.array(T_XA)

    X_test = np.concatenate((T_XP, T_XA), axis=-1)
    Y_test = np.array(T_Y)

    #Y_predict = clf.predict(X_test)

    scores = cross_val_score(clf, X_test, Y_test, cv=5)

    print(Y_train.shape)
    print(Y_test.shape)

    #print(classification_report(Y_predict, Y_test))
    print("{}".format(scores))


if __name__ == "__main__":
    print("SVM")
    svm()

    print("Random Forest Classification")
    randomForests()

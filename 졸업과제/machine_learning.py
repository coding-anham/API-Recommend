import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

def testset_set():
    A_test = np.load('npz/API_A_test.npz')
    A_T_XP = A_test['XP']
    A_T_XA = A_test['XR']
    A_T_Y = A_test['Y']
    B_test = np.load('npz/API_B_test.npz')
    B_T_XP = B_test['XP']
    B_T_XA = B_test['XR']
    B_T_Y = B_test['Y']
    A_T_XP = np.array(A_T_XP)
    A_T_XA = np.array(A_T_XA)
    B_T_XP = np.array(B_T_XP)
    B_T_XA = np.array(B_T_XA)
    A_X_test = np.concatenate((A_T_XP, A_T_XA), axis=-1)
    A_Y_test = np.array(A_T_Y)
    B_X_test = np.concatenate((B_T_XP, B_T_XA), axis=-1)
    B_Y_test = np.array(B_T_Y)
    return A_X_test, A_Y_test, B_X_test, B_Y_test


def trainset_set():
    A_train = np.load('npz/API_A_train.npz')
    B_train = np.load('npz/API_B_train.npz')
    A_XP = A_train['XP']
    A_XA = A_train['XR']
    A_Y = A_train['Y']
    B_XP = B_train['XP']
    B_XA = B_train['XR']
    B_Y = B_train['Y']
    A_XP = np.array(A_XP)
    A_XA = np.array(A_XA)
    B_XP = np.array(B_XP)
    B_XA = np.array(B_XA)
    A_X_train = np.concatenate((A_XP, A_XA), axis=-1)
    A_Y_train = np.array(A_Y)
    B_X_train = np.concatenate((B_XP, B_XA), axis=-1)
    B_Y_train = np.array(B_Y)
    return A_X_train, A_Y_train, B_X_train, B_Y_train

def svm():
    A_X_train, A_Y_train, B_X_train, B_Y_train = trainset_set()

    A_clf = SVC()
    A_clf.fit(A_X_train, A_Y_train)

    B_clf = SVC()
    B_clf.fit(B_X_train, B_Y_train)

    A_X_test, A_Y_test, B_X_test, B_Y_test = testset_set()

    A_scores = cross_val_score(A_clf, A_X_test, A_Y_test, cv=5)
    B_scores = cross_val_score(B_clf, B_X_test, B_Y_test, cv=5)

    print("A: {}".format(A_scores))
    print("B: {}".format(B_scores))
    print("mean A: {}, B: {}".format(np.mean(A_scores), np.mean(B_scores)))


def randomForests():
    A_X_train, A_Y_train, B_X_train, B_Y_train = trainset_set()

    A_clf = RandomForestClassifier(n_estimators=100, criterion="entropy")
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = RandomForestClassifier(n_estimators=100, criterion="entropy")
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    A_X_test, A_Y_test, B_X_test, B_Y_test = testset_set()

    A_scores = cross_val_score(A_clf, A_X_test, A_Y_test, cv=5)
    B_scores = cross_val_score(B_clf, B_X_test, B_Y_test, cv=5)

    print("A: {}".format(A_scores))
    print("B: {}".format(B_scores))
    print("mean A: {}, B: {}".format(np.mean(A_scores), np.mean(B_scores)))


def NaiveBayesClassifier():
    pass

if __name__ == "__main__":
    print("SVM")
    svm()

    print("Random Forest Classification")
    randomForests()

import numpy as np
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB


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

def learning(func):
    A_X_train, A_Y_train, B_X_train, B_Y_train = trainset_set()

    A_clf, B_clf = func(A_X_train, A_Y_train, B_X_train, B_Y_train)

    A_X_test, A_Y_test, B_X_test, B_Y_test = testset_set()

    A_scores = cross_val_score(A_clf, A_X_test, A_Y_test, cv=5)
    B_scores = cross_val_score(B_clf, B_X_test, B_Y_test, cv=5)

    print("A: {}".format(A_scores))
    print("B: {}".format(B_scores))
    print("mean A: {}, B: {}".format(np.mean(A_scores), np.mean(B_scores)))


def svm(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = SVC()
    A_clf.fit(A_X_train, A_Y_train)

    B_clf = SVC()
    B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def randomForests(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = RandomForestClassifier(n_estimators=100, criterion="entropy")
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = RandomForestClassifier(n_estimators=100, criterion="entropy")
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def NaiveBayesClassifier(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = GaussianNB()
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = GaussianNB()
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def GradientBoost(A_X_train, A_Y_train, B_X_train, B_Y_train):
    A_clf = GradientBoostingClassifier(random_state=0)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = GradientBoostingClassifier(random_state=0)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

def BaggingLinearsvmClassifier(A_X_train, A_Y_train, B_X_train, B_Y_train):
    estimator = LinearSVC()
    A_clf = BaggingClassifier(base_estimator=estimator, n_estimators=10, max_samples=1./10, n_jobs=1)
    A_clf = A_clf.fit(A_X_train, A_Y_train)
    B_clf = BaggingClassifier(base_estimator=estimator, n_estimators=10, max_samples=1./10, n_jobs=1)
    B_clf = B_clf.fit(B_X_train, B_Y_train)

    return A_clf, B_clf

if __name__ == "__main__":
    print("SVM")
    learning(svm)
    print("Random Forest Classification")
    learning(randomForests)
    print("Naive Bayes Classification")
    learning(NaiveBayesClassifier)
    print("Bagging Linear svm Classification")
    learning(BaggingLinearsvmClassifier)
    print("Gradient Boosting Classification")
    learning(GradientBoost)
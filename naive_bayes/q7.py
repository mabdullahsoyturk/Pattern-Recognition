#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
C_values = [10,100,1000,10000]
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

for c in C_values:
    clf = svm.SVC(kernel="rbf", C=c)
    t0 = time()

    clf.fit(features_train, labels_train)
    #print "training time:", round(time()-t0, 3), "s"

    t1 = time()
    y_pred = clf.predict(features_test)
    #print "prediction time:", round(time()-t1, 3), "s"
    print "C=", c, "Accuracy=", accuracy_score(y_pred, labels_test)
#########################################################



# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:31:52 2019

@author: Shrishti D Hore
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

'''
print(digits.data)
print(digits.target)
print(digits.images[0])
'''

clf = svm.SVC(gamma=0.01, C=100)

print(len(digits.data))

x,y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)

print('Prediction:', clf.predict(digits.data[-1]))

plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest" )
plt.show()
# -*- coding: utf-8 -*-
"""
The following program is for the cross entropy function 
This is a quiz, which is part of the AI Programming with Python Nanodegree from Udacity
"""

import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
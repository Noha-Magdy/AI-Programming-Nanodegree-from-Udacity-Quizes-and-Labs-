# -*- coding: utf-8 -*-
"""
The following program is for the softmax function 
This is a quiz, which is part of the AI Programming with Python Nanodegree from Udacity
"""

import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
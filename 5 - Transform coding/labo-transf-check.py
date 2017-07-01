# -*- coding: utf-8 -*-

import numpy as np
import scipy
import scipy.ndimage
from math import *
from numpy import *
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
# examples of transform matrices of size n; for Haar n must be a power of 2

def T_haar_matrix(n):
    level = int(math.log(n, 2))
    h = np.array([1], dtype="double")
    nc = 1 / math.sqrt(2)
    lp = np.array([1, 1], dtype="double")
    hp = np.array([1, -1], dtype="double")
    for i in range(level):
        h = nc*np.vstack((np.kron(h, lp),np.kron(np.eye(2 ** i, 2 ** i), hp)))
        h = np.reshape(h, (2 ** (i + 1), 2 ** (i + 1)))
    return h

def T_DCT_matrix(N):
    mat = np.zeros((N,N))
    for j in range(N):
        mat[0,j] = sqrt(1/N);
        for i in range(1,N):
            mat[i,j] = cos(i*(j+0.5)*pi/N)*sqrt(2/N);
    return mat

#------------------------------------------------------------------------------
# examples of quantizing matrices

Q_JPEG_standard = np.array([
[16 ,11, 10, 16,  24,  40,  51,  61],
[12, 12, 14, 19,  26,  58,  60,  55],
[14, 13, 16, 24,  40,  57,  69,  56],
[14, 17, 22, 29,  51,  87,  80,  62],
[18, 22, 37, 56,  68, 109, 103,  77],
[24, 35, 55, 64,  81, 104, 113,  92],
[49, 64, 78, 87, 103, 121, 120, 101],
[72, 92, 95, 98, 112, 100, 103,  99]])
    
def Q_constant(N=8,q=100):
    m = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            m[i,j] = q;
    return m
def Q_matrix(N=8,q=1):
    m=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            m[i,j] = (1+i+j)*q;
    return m

img=scipy.misc.imread('lena_gray_512.png');
                     
""" now you check your implementation as shown below
using several transform matrices and several quantization matrices;
you may change the size
(with the JPEG standard quantization matrix size is always 8);
experiment also with other images """

newimg = lossy_transform(img,T_DCT_matrix(16),Q_matrix(16,10))
imgerr = abs(img-newimg)

fig = plt.figure(figsize=(15,15)) #change the size 15 to adapt to your screen
fig.add_subplot(1,3,1)
plt.imshow(img.astype(np.uint8),cmap=plt.cm.gray)
fig.add_subplot(1,3,2) 
plt.imshow(newimg.astype(np.uint8),cmap=plt.cm.gray)
fig.add_subplot(1,3,3) 
plt.imshow(imgerr.astype(np.uint8),cmap=plt.cm.gray)
plt.show()

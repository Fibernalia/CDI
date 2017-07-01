from matplotlib.pyplot import imshow, show
from numpy import array, zeros, insert, round, delete, dot
from numpy.linalg import inv
from scipy import misc
from math import cos, pi, sqrt

def append_extra_rows_or_columns(img,N,m,n,extra_rows,extra_columns):
    last_row = img[n-1:]
    while n % N != 0:
        img = insert(img, n, last_row, 0)
        n += 1
        extra_rows += 1
    last_col = img[:,m-1]
    while m % N != 0:
        img = insert(img, m, last_col, 1)
        m += 1
        extra_columns += 1
    return img,m,n,extra_rows,extra_columns

def remove_extra_rows_or_columns(img,m,n,extra_rows,extra_columns):
    while extra_rows > 0:
        img = delete(img, n-1, 0)
        n -= 1
        extra_rows -= 1
    while extra_columns > 0:
        img = delete(img, m-1, 1)
        m -= 1
        extra_columns -= 1
    return img

def lossy_transform(img,T,Q):
    N = T.shape[0]
    m = img.shape[1]
    n = img.shape[0]
    extra_rows = 0
    extra_columns = 0
    if m % N != 0 or n % N != 0:
        img,m,n,extra_rows,extra_columns = append_extra_rows_or_columns(img,N,m,n,extra_rows,extra_columns)
    try:
        channels = img.shape[2]
        B = zeros((n,m,channels))
        for f in range(0, n, N):
            for c in range(0, m, N):
                for k in range(channels):
                    aux = dot(T, img[f:f+N,c:c+N,k])
                    B[f:f+N,c:c+N,k] = dot(aux, T.transpose())
        for f in range(0, n, N):
            for c in range(0, m, N):
                for k in range(channels):
                    B[f:f+N,c:c+N,k] = round(B[f:f+N,c:c+N,k]/Q)
        for f in range(0, n, N):
            for c in range(0, m, N):
                for k in range(channels):
                    B[f:f+N,c:c+N,k] = B[f:f+N,c:c+N,k]*Q
        for f in range(0, n, N):
            for c in range(0, m, N):
                for k in range(channels):
                    aux = dot(inv(T), B[f:f+N,c:c+N,k])
                    B[f:f+N,c:c+N,k] = dot(aux, inv(T.transpose()))
        B = round(B)
    except:
        B = zeros((n,m))
        for f in range(0, n, N):
            for c in range(0, m, N):
                aux = dot(T, img[f:f+N,c:c+N])
                B[f:f+N,c:c+N] = dot(aux, T.transpose())
        for f in range(0, n, N):
            for c in range(0, m, N):
                B[f:f+N,c:c+N] = round(B[f:f+N,c:c+N]/Q)
        for f in range(0, n, N):
            for c in range(0, m, N):
                B[f:f+N,c:c+N] = B[f:f+N,c:c+N]*Q
        for f in range(0, n, N):
            for c in range(0, m, N):
                aux = dot(inv(T), B[f:f+N,c:c+N])
                B[f:f+N,c:c+N] = dot(aux, inv(T.transpose()))
        B = round(B)
    newimg = remove_extra_rows_or_columns(B,m,n,extra_rows,extra_columns)
    return newimg

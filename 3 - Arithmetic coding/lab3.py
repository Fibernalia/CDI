from math import floor
len2 = len
bin2 = bin

def arithmetic_decode(bin,src,k,len):
    suma = 0
    src2 = []
    for i in range(len2(src)):
        suma += src[i][1]
    for i in range(len2(src)):
        src2.append((src[i][0],src[i][1]/suma))
    alpha = '0' * k
    beta = '1' * k
    gamma = bin[:k]
    usados = k
    x = ''
    cumulative_probs = [0]
    aux = 0.0
    for i in range(len2(src2)):
        aux += src2[i][1]
        cumulative_probs.append(aux)
    while len2(x) != len:
        delta = int(beta,2) - int(alpha,2) + 1
        subintervals = []
        for j in range(1, len2(cumulative_probs)):
            aux = (int(alpha,2) + int(floor(delta * cumulative_probs[j-1])),
                   int(alpha,2) + int(floor(delta * cumulative_probs[j]) - 1))
            subintervals.append(aux)
        for ind, subint in enumerate(subintervals):
            if subint[0] <= int(gamma,2) <= subint[1]:
                x += src2[ind][0]
                alpha = bin2(subint[0])[2:].zfill(k)
                beta = bin2(subint[1])[2:].zfill(k)
        if len2(x) == len:
            break
        while alpha[0] == beta[0]:
            alpha = alpha[1:] + '0'
            beta = beta[1:] + '1'
            if usados == len2(bin):
                gamma = gamma[1:] + '0'
            else:
                gamma = gamma[1:] + bin[usados]
                usados += 1
        while alpha[:2] == '01' and beta[:2] == '10':
            alpha = alpha[0] + alpha[2:] + '0'
            beta = beta[0] + beta[2:] + '1'
            if usados == len2(bin):
                gamma = gamma[0] + gamma[2:] + '0'
            else:
                gamma = gamma[0] + gamma[2:] + bin[usados]
                usados += 1
    return x

def arithmetic_encode(str,src,k):
    suma = 0
    src2 = []
    for i in range(len2(src)):
        suma += src[i][1]
    for i in range(len2(src)):
        src2.append((src[i][0],src[i][1]/suma))
    alpha = '0' * k
    beta = '1' * k
    c = ""
    u = 0
    cumulative_probs = [0]
    aux = 0.0
    for i in range(len(src2)):
        aux += src2[i][1]
        cumulative_probs.append(aux)
    for i in range(len(str)):
        delta = int(beta,2) - int(alpha,2) + 1
        subintervals = []
        for j in range(1, len(cumulative_probs)):
            aux = (int(alpha,2) + int(floor(delta * cumulative_probs[j-1])),
                   int(alpha,2) + int(floor(delta * cumulative_probs[j]) - 1))
            subintervals.append(aux)
        ind = [src2.index(tupla) for tupla in src2 if tupla[0] == str[i]][0]
        alpha = bin(subintervals[ind][0])[2:].zfill(k)
        beta = bin(subintervals[ind][1])[2:].zfill(k)
        while alpha[0] == beta[0]:
            c += alpha[0]
            if alpha[0] == '0':
                    c += '1' * u
            else:
                    c += '0' * u
            u = 0
            alpha = alpha[1:] + '0'
            beta = beta[1:] + '1'
        while alpha[:2] == '01' and beta[:2] == '10':
            alpha = alpha[0] + alpha[2:] + '0'
            beta = beta[0] + beta[2:] + '1'
            u += 1
    return c + '1'
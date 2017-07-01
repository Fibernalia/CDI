import random
from math import log2

def random_text(txt):
    output = ""
    prob = []
    for char in set(txt):
        prob.append( (char, txt.count(char) / len(txt)) )
    for j in range(len(txt)):
        r = random.random()
        aux = 0
        for k in range(len(prob)):
            aux += prob[k][1]
            if r < aux:
                output += prob[k][0]
                break
    return output

def random_text_joint(txt):
    prob = []
    pairs = list(txt[i:i+2] for i in range(len(txt)-1))
    for pair in set(pairs):
        prob.append( (pair, pairs.count(pair) / (len(txt)-1)) )
    r = random.choice(txt)
    output = r
    for j in range(len(txt)-1):
        probcond = []
        probr = txt[:-1].count(r) / (len(txt)-1)
        for k in range(len(prob)):
            if prob[k][0][0] == r:
                probcond.append( (prob[k][0][1], prob[k][1] / probr) )
        if len(probcond) == 0:
            output += txt[0]
            r = txt[0]
        else:
            r2 = random.random()
            aux = 0
            for i in range(len(probcond)):
                aux += probcond[i][1]
                if r2 < aux:
                    output += probcond[i][0]
                    r = probcond[i][0]
                    break
    return output

def entropy(txt):
    hx = 0.0
    prob = []
    for char in set(txt):
        prob.append( (char, txt.count(char) / len(txt)) )
    for i in range(len(prob)):
        pxi = prob[i][1]
        hx += pxi*(log2(1.0/pxi))
    return hx

def joint_entropy(txt):
    hxy = 0.0
    prob = []
    pairs = list(txt[i:i+2] for i in range(len(txt)-1))
    for pair in set(pairs):
        prob.append( (pair, pairs.count(pair) / (len(txt)-1)) )
    for i in range(len(prob)):
        pxiyj = prob[i][1]
        hxy += pxiyj*(log2(1.0/pxiyj))
    return hxy

def conditional_entropy1(txt,ltr):
    hyxi = 0.0
    pxi = txt[:-1].count(ltr) / (len(txt)-1)
    if pxi > 0:
        pairs = list(txt[i:i+2] for i in range(len(txt)-1))
        for j in set(txt):
            pxiyj = pairs.count(ltr+j) / (len(txt)-1)
            pyjxi = pxiyj / pxi
            if pyjxi > 0:
                hyxi += pyjxi*(log2(1.0/pyjxi))
    return hyxi

def conditional_entropy(txt):
    hyx = 0.0
    for char in set(txt):
        pxi = txt[:-1].count(char) / (len(txt)-1)
        hyx += pxi * conditional_entropy1(txt,char)
    return hyx

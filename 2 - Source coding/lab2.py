import queue
from math import log2, ceil
from itertools import product

class HuffmanNode(object):
    def __init__(self, left, right, root):
        self.left = left
        self.right = right
        self.root = root

def source(str):
    output = []
    for char in set(str):
        output.append( (char, str.count(char) / len(str)) )
    return output

def source_extension(src,k):
    letters = []
    output = []
    for tupla in src:
        letters.append(tupla[0])
    permutations = [''.join(i) for i in product(letters, repeat = k)]
    for perm in permutations:
        suma = 1
        for let in letters:
            problet = [tupla[1] for tupla in src if tupla[0] == let]
            suma *= problet[0]**(perm.count(let))
        output.append((perm, suma))
    return output

def entropy_source(src):
    hx = 0.0
    for i in range(len(src)):
        pxi = src[i][1]
        hx += pxi*(log2(1.0/pxi))
    return hx

def fromRootToLeafs(node, binarywords, aux):
    if (node.left == None and node.right == None):
         binarywords.append(aux)
    else:
        if (node.right != None):
            aux += '0'
            fromRootToLeafs(node.right,binarywords,aux)
            aux = aux[:len(aux)-1]
        if (node.left != None):
            aux += '1'
            fromRootToLeafs(node.left,binarywords,aux)
            
def huffman_code(src):
    id_desempate = 0
    q = queue.PriorityQueue()
    q2 = queue.PriorityQueue()
    for tupla in src:
        leafNode = HuffmanNode(None, None, tupla[1])
        q.put( (tupla[1], id_desempate, leafNode) )
        q2.put( (tupla[1], id_desempate, leafNode) )
        id_desempate += 1
    while q.qsize() > 1:
        leftNode, rightNode = q.get()[2], q.get()[2]
        parentNode = HuffmanNode(leftNode, rightNode, leftNode.root+rightNode.root)
        q.put((parentNode.root, id_desempate, parentNode))
        id_desempate += 1
    huffmanTree = q.get()[2]
    binarywords = []
    fromRootToLeafs(huffmanTree,binarywords,'')
    binarywords.sort(key = len)
    mean_length = 0.0
    for binword in reversed(binarywords):
        mean_length += q2.get()[0] * len(binword)
    return binarywords, mean_length

def prefix_code(lst):
    output = []
    for index, i in enumerate(lst):
        if (index is 0):
            output.append(bin(0)[2:].zfill(i))
        else:
            for j in range(0, 2**i):
                prefix = False
                aux = bin(j)[2:].zfill(i)
                for binword in output:
                    prefix = ( (aux.startswith(binword)) or (binword.startswith(aux)) )
                    if prefix:
                        break
                if not prefix:
                    output.append(aux)
                    break
    return output

def shannon_code(src):
    lengths = []
    mean_length = 0.0
    for let,pxi in src:
        lengths.append( ceil( (log2(1.0/pxi)) ) )
        mean_length += pxi * ceil( (log2(1.0/pxi)) ) 
    return prefix_code(sorted(lengths)), mean_length

def divide(listOfTuples):
    if len(listOfTuples) <= 2:
        return 1;
    indexToDivide = 0
    lastSuma = 0
    lastSuma2 = 0
    for i in range(1,len(listOfTuples)+1):
        suma = sum([x[0] for x in listOfTuples[:i]])
        suma2 = sum([x[0] for x in listOfTuples[i:]])
        if suma == suma2:
            indexToDivide = i
            break
        if suma > suma2:
            if i == 1:
                indexToDivide = i
            elif (suma-suma2) < (lastSuma2-lastSuma):
                indexToDivide = i
            else:
                indexToDivide = i-1
            break
        lastSuma = suma
        lastSuma2 = suma2
    return indexToDivide
        
def shannon_fano_code(src):
    binarywords = []
    mean_length = 0.0
    aux = []
    for tupla in sorted(src, key=lambda x: x[1], reverse=True):
        aux.append( (tupla[1],'') )
    q = queue.Queue()
    q.put(aux)
    while (len(binarywords) < len(aux)):
        qaux = q.get()
        indexToDivide = divide(qaux)
        q1 = []
        for i in qaux[:indexToDivide]:
            q1.append((i[0],i[1]+'0'))
        q2 = []
        for j in qaux[indexToDivide:]:
            q2.append((j[0],j[1]+'1'))
        if (len(q1) == 1):
            binarywords.append(q1[0][1])
            mean_length += q1[0][0] * len(q1[0][1])
        else:
            q.put(q1)
        if (len(q2) == 1):
            binarywords.append(q2[0][1])
            mean_length += q2[0][0] * len(q2[0][1])
        else:
            q.put(q2)
    return binarywords, mean_length
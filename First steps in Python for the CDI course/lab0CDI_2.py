def prefix_code(lst):
    output = []
    sumatorio = 0
    for i in lst:
        sumatorio += 2**(-i)
    if (sumatorio > 1):
        return output
    else:
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

def main():
    prova = [1,3,3,3,4,4]
    binarywords = prefix_code(prova)
    print ("Binary words")
    if not binarywords:
        print("There is no solution")
    else:
        [print(binword) for binword in binarywords]
        
    prova = [2,2,2,3,4]
    binarywords = prefix_code(prova)
    print ("Binary words")
    if not binarywords:
        print("There is no solution")
    else:
        [print(binword) for binword in binarywords]
        
    prova = [1,2,2,3,4]
    binarywords = prefix_code(prova)
    print ("Binary words")
    if not binarywords:
        print("There is no solution")
    else:
        [print(binword) for binword in binarywords]
    
    lst1 = [5, 5, 2, 6, 4, 3, 6, 3, 6, 4, 3, 3, 6]
    binarywords = prefix_code(lst1)
    print ("Binary words")
    if not binarywords:
        print("There is no solution")
    else:
        [print(binword) for binword in binarywords]
        
    lst2 = [5, 5, 2, 6, 4, 3, 6, 3, 6, 4, 3, 3, 4]
    binarywords = prefix_code(lst2)
    print ("Binary words")
    if not binarywords:
        print("There is no solution")
    else:
        [print(binword) for binword in binarywords]
    
main()

'''
Binary words
0
100
101
110
1110
1111
Binary words
00
01
10
110
1110
Binary words
There is no solution
Binary words
00000
00001
01
000100
0010
100
000101
101
000110
0011
110
111
000111
Binary words
There is no solution
'''

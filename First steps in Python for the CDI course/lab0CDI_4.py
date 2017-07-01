def decode(bstr,C):
    output = ""
    aux = ""
    for bit in bstr:
        if not aux:
            letter = [tupla[0] for tupla in C if tupla[1] == bit]
        else:
            letter = [tupla[0] for tupla in C if tupla[1] == aux+bit]
        if not letter:
            aux += bit
        else:
            output += str(letter).strip("'[]'")
            aux = ""
    return output
            
def main():
    bstr = '10100011011111100010011110101100101011101011100010011110010111001101111010010010110010011110000110101100111010111001111100010001011100110'
    C = [('a', '11100'),('d', '11101'),('e', '00'),('f', '111100'),('g', '1011'),
        ('j', '010'),('m', '111101'),('n', '100'),('p', '111110'),('s', '1010'),
        ('t', '110'),('u', '011'),('z', '111111')]
    decoding = decode(bstr,C)
    print(decoding)

main()

'''
setzejutgesdunjutjatmengenfetgedunpenjat
'''

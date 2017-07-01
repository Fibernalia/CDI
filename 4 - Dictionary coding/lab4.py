def LZ77_encode(txt,s,t):
    tok = []
    tok.append((0, 0, txt[0]))
    current_pos = 1
    search = txt[0]
    lookahead = txt[1:1+t]
    while current_pos < len(txt):
        offset = 0
        length = 0
        char = lookahead[0]
        window = search + lookahead
        for i in range(len(search)-1, -1, -1):
            if search[i] == lookahead[0]:
                match = True
                iwind = i+1
                jwind = len(search)+1
                maxlen = 1
                while match and jwind < len(window):
                    if window[iwind] == window[jwind]:
                       maxlen += 1
                       iwind += 1
                       jwind += 1
                    else:
                        match = False
                if (maxlen > length):
                    offset = len(search)-i
                    length = maxlen
                    try:
                        char = window[jwind]
                    except:
                        try:
                            char = txt[current_pos+length]
                        except:
                            char = window[jwind-1]
                            length -= 1
                            if (length == 0):
                                offset = 0
        tok.append((offset, length, char))
        current_pos += length+1
        if (current_pos-s < 0):
            search = txt[0:current_pos]
        else:
            search = txt[current_pos-s:current_pos]
        lookahead = txt[current_pos:current_pos+t]
    return tok

def LZ77_decode(tok):
    txt = ''
    for offset, length, char in tok:
        if offset == 0 and length == 0:
            txt += char
        else:
            for i in range(length):
                txt += txt[-offset]
            txt += char
    return txt

def LZSS_encode(txt,s,t,m):
    tok = []
    tok.append((0, txt[0]))
    current_pos = 1
    search = txt[0]
    lookahead = txt[1:1+t]
    while current_pos < len(txt):
        offset = 0
        length = 0
        window = search + lookahead
        for i in range(len(search)-1, -1, -1):
            if search[i] == lookahead[0]:
                match = True
                iwind = i+1
                jwind = len(search)+1
                maxlen = 1
                while match and jwind < len(window):
                    if window[iwind] == window[jwind]:
                       maxlen += 1
                       iwind += 1
                       jwind += 1
                    else:
                        match = False
                if (maxlen > length):
                    offset = len(search)-i
                    length = maxlen
        if length < m:
            tok.append((0, lookahead[0]))
            current_pos += 1
        else:
            tok.append((1,offset,length))
            current_pos += length
        if (current_pos-s < 0):
            search = txt[0:current_pos]
        else:
            search = txt[current_pos-s:current_pos]
        lookahead = txt[current_pos:current_pos+t]
    return tok

def LZSS_decode(tok):
    txt = ''
    for token in tok:
        if token[0] == 0:
            txt += token[1]
        else:
            for i in range(token[2]):
                txt += txt[-token[1]]
    return txt

def LZ78_encode(txt):
    tok = []
    tok.append((0, txt[0]))
    dictionary = ['', txt[0]]
    current_pos = 1
    while current_pos < len(txt):
        pointer = ''
        for i,x in enumerate(dictionary):
            if x == txt[current_pos]:
                pointer = i
                break
        if not pointer:
            tok.append((0, txt[current_pos]))
            dictionary.append(txt[current_pos])
            current_pos += 1
        else: 
            pos = current_pos+1
            b = True
            while b and pos < len(txt):
                b = False
                for i,x in enumerate(dictionary):
                    if x == txt[current_pos:pos+1]:
                        pointer = i
                        b = True
                        break
                pos += 1
            if b and pos == len(txt):
                tok.append((pointer, ''))
            else:
                tok.append((pointer, txt[pos-1]))
            dictionary.append(txt[current_pos:pos])
            current_pos = pos
    return tok

def LZ78_decode(tok):
    txt = ''
    dictionary = ['']
    for token in tok:
        txt += dictionary[token[0]] + token[1]
        dictionary.append(dictionary[token[0]] + token[1])
    return txt

def LZW_encode(txt,alp):
    tok = []
    dictionary = alp
    current_pos = 0
    while current_pos < len(txt):
        pointer = dictionary.index(txt[current_pos])
        pos = current_pos+1
        b = True
        while b and pos < len(txt):
            b = False
            for i,x in enumerate(dictionary):
                if x == txt[current_pos:pos+1]:
                    pointer = i
                    b = True
                    break
            pos += 1
        tok.append(pointer)
        dictionary.append(txt[current_pos:pos])
        if current_pos == len(txt)-1:
            current_pos = pos
        else:
            current_pos = pos-1
    return tok

def LZW_decode(tok,alp):
    return "".join(alp[tok[i]] for i in range(len(tok)))
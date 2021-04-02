s = '6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr'
k = 87
lst = list(s)
fin = []
k = k%26
for l in lst:
    if ((ord(l)>=65  and ord(l)<=90) or (ord(l)>=97  and ord(l)<=122)):
        c = ord(l)+k
        if (c > 122 and ord(l) <= 122 and ord(l) >= 97) or (c > 90 and ord(l) <= 90 and ord(l) >= 65):
            c = c-26
        fin.append(chr(c))
    else:
        fin.append(l)
out = ''
for l in fin:
    out += l
print(out)
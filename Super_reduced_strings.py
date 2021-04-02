str1 = 'baab'
s1 = list(str1)

flag = 0
ship = 0
i = 0
while flag == 0 and ship == 0:
    if s1[i] == s1[i+1]:
        s1.pop(i)
        s1.pop(i)
    else:
        i+=1
    for i in range(len(s1)-1):
        if s1[i] == s1[i+1]:
            ship = 0
            break
        else:
            ship = 1
    if i >= len(s1)-1 :
        flag = 1
out = ''
for letter in s1:
    out += letter
if out == '':
    out = "Empty String"
print(out)
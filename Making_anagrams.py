str1 = 'abc'
str2 = 'amnop'

excess = []
s1 = sorted(list(str1))
s2 = sorted(list(str2))

i = 0
j = 0
while s1 != s2 and i < len(s1) and j < len(s2):
    while (s1[i] != s2[j]):
        k = s1.pop(i) if s1[i] < s2[j] else s2.pop(j)
        excess.append(k)
        if i >= len(s1) or j >= len(s2):
            break
    i += 1
    j += 1

if len(s1) > len(s2):
    while len(s1) != len(s2):
        excess.append(s1.pop(len(s2)))
else:
    while len(s1) != len(s2):
        excess.append(s2.pop(len(s1)))

print(excess)
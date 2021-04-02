password = str(input("String:"))

flag = [1, 1, 1, 1]
s = list(password)
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
n = list(numbers)
l = list(lower_case)
u = list(upper_case)
sp = list(special_characters)

for letter in s:
    if any(letter in word for word in n):
        flag[0] = 0
    if any(letter in word for word in l):
        flag[1] = 0
    if any(letter in word for word in u):
        flag[2] = 0
    if any(letter in word for word in sp):
        flag[3] = 0
    if flag == [0, 0, 0, 0]:
        break
final = 0
for l in flag:
    final += l
if len(s) < 6:
    final += max(0, 6 - (len(s)+final))
print(final)

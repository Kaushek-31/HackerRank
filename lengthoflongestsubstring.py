def lengthOfLongestSubstring(s):
    if len(s)>1:
        count = 1
        max = 0
        i = 1
        flag = 0
        while i != len(s):
            if s[flag:i].find(s[i]) >= 0:
                if count > max:
                    max = count
                flag = s[flag:i].find(s[i]) + 1 + len(s[0:flag])
                count = len(s[flag:i+1])
                
            else:
                count += 1

            i += 1
        if count > max:
            max = count
    else:
        max = len(s)
    return max

print(lengthOfLongestSubstring("cuu"))
def longestPalindrome(s):
    if len(s) > 1:
        d = [i for i in range(len(s), 1, -1)]
        maxi = ''
        for i in d:
            flag = 0
            for j in range(len(s)-i+1):
                c = s[j:j+i]
                a = c[0: int(len(c)/2)]
                b = c[int(len(c)/2) + (len(c) % 2):]
                b = b[::-1]
                if a == b:
                    flag = 1
                    maxi = c
                    break
            if flag == 1:
                break
        if flag == 0:
            maxi = s[0]
    else:
        maxi = s
    return maxi
s = "dumpyxybklgdwxbmhptxdckihigddiqzcyvhjhxdekozqxkwaiassrxalcnrlqjbakekgkbpsznmxfvdlhjuokdvzuetuoargsrrfboenozkrglrjnmlsntrxafvqfjniugdzxeutyjybdqfyqmqlkhgvryuwegoibobkstpirzdaspjyxddnyniaywgziqbmkwqaotxirlimlhiuxoyxwsnnmsyzpfxlatnpdqvbiafzqkfssetleiobwwpubzumgittqtrjzeioxkrujkdgzfykyypvnpsxnouxeeqmarjploacjntpixpglugxtiwycmeywhnjyqsmbgxchhtlpjesmhoaskatbfvqodtboozgwlpqclkigpqzvatavdzvgoibmygjsskynldvxevbprdxzpqcpuokyqyseyrekoiipoytftnwqawykfpcqriuazjoqucjkyknmcbiykqerpxxdkqlxvlijqegpexvylgkqygbgkicwmplnwubjwqnarulzlbrdftmzyrzhrmfqoiwzlncdreqaiipnqlwffxircopksnwizmyvzfphlqlvqpcsfjmyssrheczllgkvnretmtixoibncraddatreejidxilnplcrufhdgktvkzuaggcumykgklypodjrpdpjcneagjfxahtjeurotkufkmxsoelzpttfeugdculuxjddghlisdytyjwwnftjbvrwyntqwqjrwlfynczndjyiyaxozdlgdzjseyfumvxuclmszawzwiunwqouycmfgkpzgivsemxamnfjzcabkgkgxcruqhpbkzhpdrcexnioaxbjwxbuipnjbsujajpnqeckfgxyuydytrfhhwsxfjeahpiaoojdwkzstnxflxddljpbhfirteejbtcxpvwutsgrrjv"
print(longestPalindrome(s))
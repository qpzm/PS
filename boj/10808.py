s = input()
l = [0] * 26
for c in s:
    l[ord(c) - ord('a')] +=1
print(' '.join(map(str, l)))

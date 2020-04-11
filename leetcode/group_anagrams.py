from collections import defaultdict

def groupAnagrams(strs):
    dic = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        dic[key].append(word)
    return dic.values()

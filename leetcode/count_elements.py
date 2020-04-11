from collections import Counter

def countElements(arr):
    c = Counter(arr)
    result = 0
    for k in c:
        if c[k+1] != 0:
            result += c[k]

    return result

assert(countElements([1,1,3,3,5,5,7,7]) == 0)
assert(countElements([1,3,2,3,5,0]) == 3)
assert(countElements([1,1,2]) == 2)

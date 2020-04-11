def parse(S):
    stk = []
    for c in S:
        if c != '#':
            stk.append(c)
        elif stk:
            stk.pop()
    return ''.join(stk)

def backspaceCompare(S, T):
    return parse(S) == parse(T)

assert(backspaceCompare("ab#c", "ad#c"))
assert(backspaceCompare("a##c", "#a#c"))
assert(backspaceCompare("ab##", "c#d#"))
assert(not backspaceCompare("a#c", "b"))

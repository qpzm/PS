s = input()
l = map(lambda c: s.find(c), [chr(x) for x in range(97, 123)])
print(' '.join(map(str, l)))

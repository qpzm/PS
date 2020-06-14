from functools import reduce

def naive_match(query, word):
    if len(query) != len(word):
        return False

    for w_char, q_char in zip(list(word), list(query)):
        if q_char == '?' or w_char == q_char:
            continue
        else:
            return False
    return True

def naive_solution(words, queries):
    answer = list(
        map(lambda q:
            reduce(lambda x, y: x + y,
                   map(lambda w:
                       naive_match(q, w),
                       words)
                   ),
            queries))
    return answer

# Passed solution
# Problem: Testcase 5 requires 1.3 Gb because this saves child counts
#          of each length in dict

from collections import defaultdict

class Node:
    def __init__(self):
        self.count = defaultdict(int) # 0: num of words ending here
        self.children = [None] * 26

    def put(self, word):
        cur = self

        while(len(word) != 0):
            cur.count[len(word)] += 1
            c = word[0]
            child = cur.children[ord(c) - ord('a')]
            if child == None:
                cur.children[ord(c) - ord('a')] = Node()

            cur = cur.children[ord(c) - ord('a')]
            word = word[1:]

        cur.count[len(word)] += 1

    def search(self, word):
        cur = self
        i = 0
        while(word[i] != '?'):
            child = cur.children[ord(word[i]) - ord('a')]
            if child == None:
                return 0
            cur = child
            i += 1

        return cur.count[len(word) - i]


def solution(words, queries):
    answer = [0] * len(queries)
    len_words = len(words)
    prefix_tree = Node()
    suffix_tree = Node()

    for w in words:
        prefix_tree.put(w)
        suffix_tree.put(w[::-1])

    for i, q in enumerate(queries):
        if q[0] == '?' and q[-1] == '?':
            ans = prefix_tree.count[len(q)]
        elif q[0] == '?':
            ans = suffix_tree.search(q[::-1])
        else:
            ans = prefix_tree.search(q)

        answer[i] = ans

    return answer

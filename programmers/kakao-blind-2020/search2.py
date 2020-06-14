# Soluiton2: Create a trie for each length, which requires 870Mb in Testcase 5
# https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/

from collections import defaultdict

class Node:
    def __init__(self):
        self.count = 0
        self.children = [None] * 26

    def put(self, word):
        cur = self

        while(len(word) != 0):
            cur.count += 1
            c = word[0]
            child = cur.children[ord(c) - ord('a')]
            if child == None:
                cur.children[ord(c) - ord('a')] = Node()

            cur = cur.children[ord(c) - ord('a')]
            word = word[1:]

        cur.count += 1

    def search(self, word):
        cur = self
        i = 0
        while(word[i] != '?'):
            child = cur.children[ord(word[i]) - ord('a')]
            if child == None:
                return 0
            cur = child
            i += 1

        return cur.count


def solution(words, queries):
    answer = [0] * len(queries)
    len_words = len(words)
    # Create a trie for each length
    prefix_trees = defaultdict(Node)
    suffix_trees = defaultdict(Node)

    for w in words:
        l = len(w)
        prefix_trees[l].put(w)
        suffix_trees[l].put(w[::-1])

    for i, q in enumerate(queries):
        l = len(q)
        if q[0] == '?' and q[-1] == '?':
            ans = prefix_trees[l].count
        elif q[0] == '?':
            ans = suffix_trees[l].search(q[::-1])
        else:
            ans = prefix_trees[l].search(q)

        answer[i] = ans

    return answer

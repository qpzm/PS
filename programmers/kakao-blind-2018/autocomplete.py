class TrieNode:
    def __init__(self):
        self.end = False
        self.children_count = 0
        self.children = [None] * 26 # 'a' ~ 'z'

    def iterative_insert(self, word):
        i, cur = 0, self
        while(i < len(word)):
            first_character = word[i]
            child = cur.children[self.__to_index(first_character)]
            if not child:
                child = TrieNode()

            cur.children[self.__to_index(first_character)] = child
            cur.children_count += 1
            cur = child
            i += 1

        cur.end = True

    def recursive_insert(self, word):
        # Put a dummy node to mark the end of the word
        # [ g ] -> [ o , end: True] -> [ n ] -> [ e ] -> [... end: True]
        if len(word) == 0:
            self.end = True
            return

        first_character = word[0]
        child = self.children[self.__to_index(first_character)]
        if not child:
            child = TrieNode()

        child.insert(word[1:])
        self.children[self.__to_index(first_character)] = child
        self.children_count += 1

    def iterative_search(self, word):
        i, cur = 0, self

        while(i < len(word)):
            if cur.children_count == 1:
                # If cur.end == False, You don't have to come this node.
                i += int(cur.end)
                break

            first_character = word[i]
            cur = cur.children[self.__to_index(first_character)]
            i += 1

        return i # index is # of characters checked

    def recursive_search(self, word):
        # No Not Found case
        # Case 1. When you reach the end
        if len(word) == 0:
            return 0

        # Case 2 ["go", "gone"]: [ g ] -> [ o ] -> [ n, end: True] -> [ e ] -> [... end: True]
        # "go" is not enough for "gone". You can figure out with end property, which
        # means you have a word which has "go" as its suffix.
        # Case 3 ["ab", "cd", "de"]: [a] -> [b, end: False] "a" is enough.
        if self.children_count == 1:
            return int(self.end)

        # Case 4. Access the children
        first_character = word[0]
        child = self.children[self.__to_index(first_character)]
        return 1 + child.search(word[1:])

    def __to_index(self, char):
        return ord(char) - ord('a')

def solution(words):
    total = 0
    trie = TrieNode()
    for w in words:
        trie.iterative_insert(w)

    for w in words:
        res = trie.iterative_search(w)
        total += res

    return total

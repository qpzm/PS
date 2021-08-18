class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            x = self.longestPalindrome(s[:-1])
            if (s[0] == s[-1]):
                y = s[0] + self.longestPalindrome(s[1:-1]) + s[-1]
                if (len(x) > len(y)):
                    return x
                else:
                    return y
            else:
                y = self.longestPalindrome(s[1:])
                if (len(x) > len(y)):
                    return x
                else:
                    return y



def main():
    problems = ["babad", "cbbd", "a", "ac", "aacabdkacaa"]
    answers = ["bab", "bb", "a", "a", "aca"]
    s = Solution()
    for p, a in zip(problems, answers):
        print(s.longestPalindrome(p) == a)


if __name__ == '__main__':
    main()

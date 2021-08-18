class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = s[0]  # len = 1일 때 아래가 range(1, 1) 이렇게 되므로
        for i in range(2, 2 * len(s) - 1):
            x = self._longestPalindrome(s, i)
            if len(ret) < len(x):
                ret = x

        return ret

    def _longestPalindrome(self, s: str, i: int) -> str:
        x = ""
        j = 0
        if (i % 2 == 0): # 사이에서 시작하면 양쪽이 같아야 계속 확인
            j = (i // 2) - 1
            if (s[j] == s[j+1]):
                x = s[j: j+2]
                l, r = j-1, j+2
            else:
                return ""
        else:
            j = (i - 1) // 2
            x = s[j]
            l, r = j-1, j+1

        while (0 <= l and r < len(s)):
            if(s[l] == s[r]):
                x = s[l] + x + s[r]
                l = l - 1
                r = r + 1
            else:
                break

        return x


def main():
    problems = ["babad", "cbbd", "a", "ac", "aacabdkacaa", "ccc"]
    answers = ["bab", "bb", "a", "a", "aca", "ccc"]
    s = Solution()
    for p, a in zip(problems, answers):
        print(s.longestPalindrome(p))


if __name__ == '__main__':
    main()

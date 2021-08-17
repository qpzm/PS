from typing import List


class Solution:

    def isValid(self, s: str) -> bool:
        return self._isValid(s, 0, [])

    def _isValid(self, s: str, i: int, stack: List) -> bool:
        if i == len(s):
            return len(stack) == 0
        else:
            if (s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
                return self._isValid(s, i + 1, stack)
            else:
                if (len(stack) == 0):
                    return False
                else:
                    x = stack.pop()
                    if ((x == "(" and s[i] == ")") or (x == "{" and s[i] == "}") or (x == "[" and s[i] == "]")):
                        return self._isValid(s, i + 1, stack)
                    else:
                        return False


def main():
    problems = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    answers = [True, True, False, False, True]
    sol = Solution()

    for prob, ans in zip(problems, answers):
        print(sol.isValid(prob) == ans)


if __name__ == '__main__':
    main()

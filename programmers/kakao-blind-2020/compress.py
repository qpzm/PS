def solution(s):
    answer = 1000

    for length in range(1, max(1, len(s) // 2) + 1):
        cnt, before, compressed = 1, "", ""
        for chunk in list(map(''.join, zip(*[iter(s)] * length))):
            if chunk == before:
                cnt += 1
            else:
                if cnt == 1:
                    compressed += f"{before}"
                else:
                    compressed += f"{cnt}{before}"

                before = chunk
                cnt = 1

        if cnt == 1:
            compressed += f"{before}"
        else:
            compressed += f"{cnt}{before}"

        suffix_len = len(s) % length
        if suffix_len != 0:
            compressed += s[-suffix_len:]

        new_answer = len(compressed)
        answer = min(new_answer, answer)

    return answer

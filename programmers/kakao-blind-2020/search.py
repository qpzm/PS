def match(query, word):
    if len(query) != len(word):
        return False

    for w_char, q_char in zip(list(word), list(query)):
        if q_char == '?' or w_char == q_char:
            continue
        else:
            return False
    return True

def solution(words, queries):
    answer = [0] * len(queries)
    for i, q in enumerate(queries):
        for w in words:
            if match(q, w):
                answer[i] += 1
    return answer

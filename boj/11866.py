# input
# 7 3
# output
# <3, 6, 2, 7, 5, 1, 4>

def main():
    N, K = map(lambda x: int(x), input().split())
    answer = list()
    persons = list(range(1, N + 1))
    i = 0
    while len(persons) != 0:
        i = run(persons, i, K, answer)

    formatted_answer = ', '.join(answer)
    print(f'<{formatted_answer}>')

def run(persons, i, K, answer):
    next = (i + K - 1) % len(persons) # pop 을 하면서 한 칸씩 당겨지기 때문에 K - 1 만큼만 가면 된다.
    x = persons.pop(next)
    answer.append(str(x))
    return next


main()

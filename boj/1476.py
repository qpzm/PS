# e, s, m = 3 4 5 일 때
# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 1 2 3 1 2 3 # 3 이 나오면 사실 모듈러는 0
# 1 2 3 4 1 2 3 4
# 1 2 3 4 5 1 2 3 4 5

def main():
    e, s, m = map(lambda x: int(x), input().split(' '))
    print(translate(e, s, m))


def translate(e, s, m):
    # (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
    e, s, m = e % 15, s % 28, m % 19
    for n in range(1, 7981):
        if(n % 15 == e and n % 28 == s and n % 19 == m):
            return n


if __name__ == '__main__':
    main()

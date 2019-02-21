def main():
    N = int(input())
    print(fib(N))

def fib(N):
    return fib_iter(0, 1, 0, N)

def fib_iter(cur_res, next_res, cur, end):
    if cur == end:
        return cur_res
    else:
        return fib_iter(next_res, cur_res + next_res, cur + 1, end)


if __name__ == "__main__":
    main()

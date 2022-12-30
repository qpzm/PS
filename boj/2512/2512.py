N = int(input())
l = list(map(int, input().split()))
allowance = int(input())
answer = 0

def calc(limit):
    left = allowance
    for x in l:
        left -= min(limit, x)
        if left < 0:
            return False

    return True


def bsearch(start, end):
    # print(f"start: {start}, end: {end}")
    global answer

    mid = (start + end) // 2

    if calc(mid):
        answer = mid
        if start != end:
            bsearch(mid + 1, end)
    else:
        if start != end and start <= mid - 1:
            bsearch(start, mid - 1)


bsearch(0, max(l))
print(answer)

from itertools import product

def determine(cur, key):
    cnt, ones = 0, sum(cur)
    for x, y in zip(cur, key):
        cnt += int(x == 1 and y == 1)
    return cnt == ones


def find_smallest(keys):
    print(keys)
    result = []
    while(len(keys) != 0):
        result.append(keys.pop(0))
        cur = result[-1]
        # print(f'cur: {cur}')
        # print(ones)
        keys = [x for x in keys if not determine(cur, x)]

    return result


def subrow(row, sel):
    res = []
    for item, s in zip(row, sel):
        if s== 1:
            res.append(item)
    return str(res)


def solution(relation):
    n_rows, n_cols = len(relation), len(relation[0])
    uniques = []
    for sel in product(range(2), repeat=n_cols):
        s = set(map(lambda row: subrow(row, sel), relation))

        if len(s) == n_rows:
            uniques.append(sel)
    return len(find_smallest(uniques))


if __name__ == "__main__":
    relation = [
        ["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]
    ]
    solution(relation)

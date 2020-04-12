def stair_number(n: int) -> int:
    suffix_counts = [0] + [1] * 9
    new_counts = [0] * 10
    while(n != 1):
        n -= 1
        for i in range(10):
            if i == 0:
                new_counts[i] = suffix_counts[1]
            elif i == 9:
                new_counts[i] = suffix_counts[8]
            else:
                new_counts[i] = (suffix_counts[i-1] + suffix_counts[i+1]) % 1_000_000_000
        suffix_counts = new_counts
        new_counts = [0] * 10

    return sum(suffix_counts) % 1_000_000_000

N = int(input())
print(stair_number(N))
assert(stair_number(1) == 9)
assert(stair_number(2) == 17)

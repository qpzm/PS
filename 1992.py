def main():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    print(quadtree(N, arr, 0, 0))


def quadtree(size, arr, i, j):
    a = arr[i][j]

    for x in range(size):
        for y in range(size):
            if arr[i + x][j + y] != a:
                half = size // 2
                return '(' + ''.join([
                    quadtree(half, arr, i, j),
                    quadtree(half, arr, i, j + half),
                    quadtree(half, arr, i + half, j),
                    quadtree(half, arr, i + half, j + half)
                ]) + ')'

    return a


if __name__ == "__main__":
    main()

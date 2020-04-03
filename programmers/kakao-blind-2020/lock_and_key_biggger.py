def rotate(square):
    N = len(square)
    result = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            result[j][-i-1] = square[i][j]
    return result

def solution(key, lock):
    M, N = len(key), len(lock)
    len_bg = N + 2 * (M-1)

    for _ in range(4):
        for offset_i in range(len_bg - M + 1):
            for offset_j in range(len_bg - M + 1):
                bg = [[0] * len_bg for _ in range(len_bg)]
                for i in range(M):
                    for j in range(M):
                        bg[offset_i + i][offset_j + j] += key[i][j]

                for i in range(N):
                    for j in range(N):
                        bg[M - 1 + i][M - 1 + j] += lock[i][j]

                result = True
                for i in range(N):
                    for j in range(N):
                        result = result and bg[M - 1 + i][M - 1 + j] == 1

                if result:
                    return True
        key = rotate(key)

    return False

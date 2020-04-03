def is_all_one(square):
    N = len(square)
    for i in range(N):
        for j in range(N):
            if square[i][j] != 1:
                return False
    return True

def rotate(square):
    N = len(square)
    result = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            result[j][-i-1] = square[i][j]
    return result

def fit(key, lock, row_offset, col_offset):
    M, N = len(key), len(lock)
    overlap = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            key_i, key_j = i - row_offset, j - col_offset
            if 0 <= key_i < M and 0 <= key_j < M:
                overlap[i][j] = lock[i][j] + key[key_i][key_j]
            else:
                overlap[i][j] = lock[i][j]

    return is_all_one(overlap)

def solution(key, lock):
    M, N = len(key), len(lock)
    for _ in range(4):
        # Note! offset ends at N-1, not M-1
        for row_offset in range(-M + 1, N):
            for col_offset in range(-M + 1, N):
                if fit(key, lock, row_offset, col_offset):
                    return True
        key = rotate(key)
    return False

def build_col(answer, x, y):
    if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
        answer.append([x, y, 0])

def build_row(answer, x, y):
    if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
        answer.append([x, y, 1])
        return

    if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
        answer.append([x, y, 1])

def delete_col(answer, x, y):
    if [x, y + 1, 0] in answer and [x - 1, y + 1, 1] not in answer and [x, y + 1, 1] not in answer:
       return
    if [x - 1, y + 1, 1] in answer and [x - 1, y, 0] not in answer and not ([x - 2, y + 1, 1] in answer and [x, y + 1, 1] in answer):
       return
    if [x, y + 1, 1] in answer and [x + 1, y, 0] not in answer and not ([x - 1, y + 1, 1] in answer and [x + 1, y + 1, 1] in answer):
       return

    answer.remove([x, y, 0])

def delete_row(answer, x, y):
    # left col
    if [x, y, 0] in answer and [x, y - 1, 0] not in answer and [x - 1, y, 1] not in answer:
        return
    # right col
    if [x + 1, y, 0] in answer and [x + 1, y - 1, 0] not in answer and [x + 1, y, 1] not in answer:
        return
    # left row
    if [x - 1, y, 1] in answer and [x - 1, y - 1, 0] not in answer and [x, y - 1, 0] not in answer:
        return
    # right row
    if [x + 1, y, 1] in answer and [x + 1, y - 1, 0] not in answer and [x + 2, y - 1, 0] not in answer:
        return
    answer.remove([x, y, 1])

def solution(n, build_frame):
    answer = []
    for x, y, is_row, is_build in build_frame:
        if is_row and is_build:
            build_row(answer, x, y)
        elif is_row and not is_build:
            delete_row(answer, x, y)
        elif not is_row and is_build:
            build_col(answer, x, y)
        else:
            delete_col(answer, x, y)

    answer.sort()
    return answer

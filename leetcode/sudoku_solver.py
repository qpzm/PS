from sys import stdin, stdout

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        slots = []
        cur = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    slots.append((i, j))

        while cur != len(slots):
            i, j = slots[cur]
            lower_limit = 1
            if board[i][j] != '.':
                lower_limit = int(board[i][j]) + 1
            if not self.solve(board, i, j, lower_limit):
                cur -= 1
                board[i][j] = '.'
            else:
                cur += 1

        for i in range(9):
            for j in range(9):
                stdout.write(f'{board[i][j]} ')
        stdout.write('\n')

    def check(self, board, row, col, x):
        row_corner = row - (row % 3)
        col_corner = col - (col % 3)

        # check row
        for j in range(0, 9):
            if board[row][j] != '.' and int(board[row][j]) == x:
                return False

        # check col
        for i in range(0, 9):
            if board[i][col] != '.' and int(board[i][col]) == x:
                return False

        # check square
        for i in range(row_corner, row_corner + 3):
            for j in range(col_corner, col_corner + 3):
                if board[i][j] != '.' and int(board[i][j]) == x:
                    return False

        return True


    def solve(self, board, row, col, lower_limit):
        for k in range(lower_limit, 10):
            if self.check(board, row, col, k):
                board[row][col] = str(k)
                return True

        return False


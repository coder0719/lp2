class NQueens:
    def __init__(self, n):
        self.n = n
        self.result = []

    def is_safe(self, board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check upper diagonal on right side
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if board[i][j] == 1:
                return False

        return True

    def solve_backtracking(self, board, row):
        if row == self.n:
            self.result.append([row[:] for row in board])
            return

        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row][col] = 1
                self.solve_backtracking(board, row + 1)
                board[row][col] = 0

    def solve_branch_and_bound(self, board, row):
        if row == self.n:
            self.result.append([row[:] for row in board])
            return

        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row][col] = 1
                if self.solve_branch_and_bound(board, row + 1):
                    return True
                board[row][col] = 0
        return False

    def print_solution(self):
        for solution in self.result:
            for row in solution:
                print(' '.join(map(str, row)))
            print()

# Example usage
n = int(input("Enter number of queens: "))
n_queens = NQueens(n)

# Backtracking
board_backtracking = [[0] * n for _ in range(n)]
n_queens.solve_backtracking(board_backtracking, 0)
print("Backtracking solutions:")
n_queens.print_solution()

# Branch and bound
board_branch_bound = [[0] * n for _ in range(n)]
n_queens.result = []  # Clear result list before using branch and bound
n_queens.solve_branch_and_bound(board_branch_bound, 0)
print("Branch and Bound solutions:")
n_queens.print_solution()

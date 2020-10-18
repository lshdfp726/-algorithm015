class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        l = len(board)
        if l == 0:
            return board

        self.dfs(board)
        return board
    
    def dfs(self, board) -> bool:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    for c in range(1,10):
                        if self.isVaild(i, j, str(c), board):
                            board[i][j] = str(c)
                            if self.dfs(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def isVaild(self, i, j, c, board) -> bool:
        for k in range(9):
            if board[i][k] != '.' and board[i][k] == c:return False
            if board[k][j] != '.' and board[k][j] == c:return False
            if board[(i // 3) * 3 + k // 3][(j // 3) * 3 + k % 3] != '.' and board[(i // 3) * 3 + k // 3][(j // 3) * 3 + k % 3] == c: return False
        return True

if __name__ == "__main__":
    print(Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

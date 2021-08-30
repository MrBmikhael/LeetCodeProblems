class Solution(object):
    def isValid(self, board, location, num):
        row = ''.join(board[location[0]])
        col = ''.join([x[location[1]] for x in board])
        
        y = (location[0] // 3) * 3
        x = (location[1] // 3) * 3
        
        block = ''.join([ ''.join(board[i][x:x+3]) for i in range(y, y+3) ])
        
        if num in row or num in col or num in block:
            return False
        return True
        
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for n in range(1,10):
                        if self.isValid(board, [i,j], str(n)):
                            board[i][j] = str(n)
                            if self.solveSudoku(board):
                                return True
                            board[i][j] = "."
                    return False
        return True
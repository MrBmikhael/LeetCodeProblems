class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            row = str(''.join(board[i])).replace('.', '')
            if len(row) != len(set(row)):
                return False
            col = []
            for j in range(9):
                col.append(board[j][i])
            col = str(''.join(col)).replace('.', '')
            if len(col) != len(set(col)):
                return False
            
        for i in range(3):
            for j in range(3):
                block = []
                block += board[0 + (i*3)][0 + (j*3):3 + (j*3)]
                block += board[1 + (i*3)][0 + (j*3):3 + (j*3)]
                block += board[2 + (i*3)][0 + (j*3):3 + (j*3)]
                block = str(''.join(block)).replace('.', '')
                if len(block) != len(set(block)):
                    return False
        return True
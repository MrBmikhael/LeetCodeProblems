class Solution(object):
    
    def validLocation(self, board, newLocation):
        if newLocation[0] < 0 or newLocation[0] >= len(board) or newLocation[1] < 0 or newLocation[1] >= len(board[0]):
            return None
        return newLocation
    
    def findWord(self, board, word, location, visited):
        if self.validLocation(board, location) and location not in visited:
            if len(word) == 1 and board[location[0]][location[1]] == word[0]:
                return True
            elif word[0] == board[location[0]][location[1]]:
                visited.append(location)
                upCell = self.findWord(board, word[1:], [location[0]-1, location[1]], visited)
                downCell = self.findWord(board, word[1:], [location[0]+1, location[1]], visited)
                leftCell = self.findWord(board, word[1:], [location[0], location[1]-1], visited)
                rightCell = self.findWord(board, word[1:], [location[0], location[1]+1], visited)
                res = upCell or downCell or leftCell or rightCell

                if not res:
                    visited.remove(location)
                
                return res
            else:
                return False
        else:
            return False
    
    def getValidWords(self, board, words):
        validWords = []
        alpha = set()
        for r in board:
            for l in r:
                alpha.add(l)
        for w in words:
            ws = set(w)
            if len(ws - alpha) == 0:
                validWords.append(w)
        return validWords
                    
    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        
        words = self.getValidWords(board, words)
        
        for w in words:
            added = False
            for i in range(len(board)):
                if added: break
                for j in range(len(board[0])):
                    if board[i][j] == w[0]:
                        if self.findWord(board, w, [i,j], []):
                            if not added:
                                output.append(w)
                                added = True
                                break
        return output

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def tous_differents(tab):
            vus = set()
            for x in tab:
                if x == ".":
                    continue
                if x in vus:
                    return False
                vus.add(x)
            return True

        # check les lignes
        for i in board:
            if not tous_differents(i):
                return False
        
        # check les colonnes
        for i in range(9):
            tab = []
            for j in range(9):
                tab.append(board[j][i])
            
            if not tous_differents(tab):
                return False

        # check les carres
        for k in range(0,7, 3):
            for l in range(0, 7, 3):
                tab = []
                for i in range(3):
                    for j in range(3):
                        tab.append(board[k+i][l+j])
                
                if not tous_differents(tab):
                    return False

        return True
        

# https://leetcode.com/problems/sudoku-solver/
# backtracking 
# base case is the full borad is filled and all valid
# functions : findempty(to find blocks that needed to be filled. if False, meet the base case). valid(test each number to see if it is valid). backtracking(if at any point the block can not be valid with all numbers, 
# set the previous one to 0 and try a different number.)

# need to be adjusted
# not good yet
class Solution:
    def findempty(self,board):
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    return r,c
        return None
    
    
    def valid(board,r,c,num):
        # check rows
        for i in range(len(board[r][:])):
            if board[r][c] == num and c != i:
                return False
        # check columns
        for i in range(len(board[:][c])):
            if board[r][c] == num and r != i:
                return False
        # check squares
        for i in range(3*(r//3),3*(r//3)+3):
            for j in range(3*(c//3),3*(c//3)+3):
                if board[r][c] == num and [i,j] != [r,c]:
                    return False

        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        # find empty, fill, valid, backtracking or done
        find = self.findempty(board)
        if not find:
            return True
        else:
            r,c = find
        
        for num in range(1,10):
            if self.valid(board,r,c,num):
                board[r][c] = num
                
                if solvesudoku(board):
                    return True
                
                board[r][c] = 0
        return False
# code above  need to be adjusted 



def fillempty(r,c,rows,cols,boxes,board):
	for r in range(len(rows)):
		for c in range(len(cols)):
			if board[r][c] != '.':
				continue
	
			for num in range(1,10):
				if (num in rows[r] or num in cols[c]
					or num in boxes[(r//3,c//3)]):
						continue
				board[r][c] = num
				
def valid(board, num, r, c):
	# check rows
	for i in range(len(board[r][:])):
		if board[r][c] == num  and c != i:
			return False
	# check columns
	for i in range(len(board[:]{c})):
		if board[r][c] == num and r != i:
			return False
	# check squares
	for i in range(3*(r//3), 3*(r//3) + 3):
		for j  in range(3*(c//3), 3*(c//3) + 3):
			if board[r][c] == num and [i,j] != [r,c]:
				return False

def 
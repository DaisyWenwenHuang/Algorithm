# https://leetcode.com/problems/sudoku-solver/
# backtracking 
# base case is the full borad is filled and all valid
# functions : findempty(to find blocks that needed to be filled. if False, meet the base case). valid(test each number to see if it is valid). backtracking(if at any point the block can not be valid with all numbers, 
# set the previous one to 0 and try a different number.)
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
	# check
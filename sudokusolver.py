# https://leetcode.com/problems/sudoku-solver/
# backtracking 
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
				
				
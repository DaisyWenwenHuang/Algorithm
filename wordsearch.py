# https://leetcode.com/problems/word-search/
# can not revisit the path, need a set to track the path
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = 'AAB'
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"

rows, cols = len(board1),len(board1[0])
path = set()


def dfs(r,c,i):
	if i == len(word):
		return True
	if (r < 0 or c > 0 or r>= rows or c >= cols 
	   or word[i] != board[r][c] or (r,c) in path):
		   return False
	path.add((r,c))
	print(path)
	res = (dfs(r+1,c,i+1) or
		   dfs(r-1,c, i+1) or
		   dfs(r, c+1,i+1) or 
		  dfs(r,c-1,i+1))
	# remove used path after one path of search
	path.remove((r,c))
	print(res)
	return res


for r in range(rows):
	for c in range(cols):
		if dfs(r,c,0):
			print(True)
print(False)  

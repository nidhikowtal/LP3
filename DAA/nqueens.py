N = 4

""" ld is an array where its indices indicate row-col+N-1
(N-1) is for shifting the difference to store negative
indices """
ld = [0] * 30

""" rd is an array where its indices indicate row+col
and used to check whether a queen can be placed on
right diagonal or not"""
rd = [0] * 30

"""column array where its indices indicates column and
used to check whether a queen can be placed in that
	row or not"""
cl = [0] * 30

""" A utility function to print solution """
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

def solveNQUtil(board, col):
	
	""" base case: If all queens are placed
		then return True """
	if (col >= N):
		return True
		
	""" Consider this column and try placing
		this queen in all rows one by one """
	for i in range(N):
		
		""" Check if the queen can be placed on board[i][col] """
		""" A check if a queen can be placed on board[row][col].
		We just need to check ld[row-col+n-1] and rd[row+coln]
		where ld and rd are for left and right diagonal respectively"""
		if ((ld[i - col + N - 1] != 1 and
			rd[i + col] != 1) and cl[i] != 1):
				
			""" Place this queen in board[i][col] """
			board[i][col] = 1
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
			
			""" recur to place rest of the queens """
			if (solveNQUtil(board, col + 1)):
				return True
				
			""" If placing queen in board[i][col]
			doesn't lead to a solution,
			then remove queen from board[i][col] """
			board[i][col] = 0 # BACKTRACK
			ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

	return False

def solveNQ():
	board = [[0, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 0],
			[0, 0, 0, 0]]
	cl[2]=1
	rd[2]=1
	ld[5]=1
	if (solveNQUtil(board, 1) == False):
		print("Solution does not exist")
		return False
	printSolution(board)
	return True

solveNQ()


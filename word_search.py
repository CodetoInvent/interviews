# Word Search

# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

board = [
	["A","B","C","E"],
	["S","F","E","S"],
	["A","D","E","E"]
]



# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


def word_search(board, word):
	if not board: return False
	if not word: return True

	starts = find_first_letters(board, word[0])

	if not starts: return False

	for start in starts:
		if traverse_board(board, word, 1, [], *start):
			return True
	return False


def find_first_letters(board, letter):

	starts = []
	for row in range(len(board)):
		for column in range(len(board[row])):
			if board[row][column] == letter:
				starts.append((row, column))

	return starts


def traverse_board(board, word, next_index, seen, row, column):
	if next_index > len(word) - 1: 
		return True

	letter = word[next_index]
	seen.append((row, column))

	out_of_bounds = lambda row, column, board: \
		(row >= len(board) or row < 0) or \
		(column >= len(board[0]) or column < 0)

	neighboring = [
		(row-1, column), 
		(row+1, column), 
		(row, column-1), 
		(row, column+1)
	]

	for (r, c) in neighboring:
		if out_of_bounds(r, c, board): continue
		if board[r][c] == letter and (r, c) not in seen:
			print letter
			if traverse_board(board, word, next_index+1, seen, r, c):
				return True

	seen.remove((row, column))
	return False



print word_search(board, "ABCESEEEFS")
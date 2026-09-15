from collections import Counter

side = 5  # the board has 5 columns by 5 lines
generations = 5  # how many rounds (generations) we'll draw

# each cell is a pair (column, line) - these 5 form the Glider in generation 0
alives = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}

def neighbors(column, line):
	lap = []
	for dc in (-1, 0, 1):
		for dl in (-1, 0, 1):
			if (dc, dl) != (0, 0):  # (0,0) would be the cell itself: doesn't count as a neighbor
				lap.append((column + dc, line + dl))  # add the offset and store the neighbor
	return lap


def next(board):
	count = Counter()  # will become "how many ALIVE neighbors each house has"
	for column, line in board:  # for each living cell
		for home in neighbors(column, line):
			count[home] += 1  # ...it gives 1 point to each neighbor

	new = set()  # the board that will be valid in the next generation

	for home, n in count.items():  # look only at houses that have some living neighbor
		born = (n == 3)  # with exactly 3 neighbors the house lives: is born or continues
		survive = (n == 2 and home in board)  # was already alive and has 2 neighbors: continues
		if born or survive:  # the rest (0, 1, 4 or more neighbors) dies
			new.add(home)  # whoever passed the rules enters the next generation
	return new  # return the brand new board

pics = []  # we'll store one "photo" of the board per generation

for g in range(generations):  # run all 5 generations, one at a time
	pics.append(alives)  # store the photo of how the board is right now
	alives = next(alives)  # and advance one generation

tittles = []  # top row of the drawing: Generation 0, Generation 1...

for g in range(generations):
	tittles.append(('Generation %d' % g).ljust(side * 2 - 1))  # align the title with the board
print('   '.join(tittles))  # print the 5 titles side by side

for line in range(side):  # draw the board top to bottom, line by line
	strips = []  # one text strip per generation
	for pic in pics:  # the SAME line, seen in each of the 5 photos
		strips.append(' '.join('#' if (column, line) in pic else '.'
			for column in range(side)))  # #=alive, .=empty
	print('      '.join(strips))  # print the 5 strips side by side

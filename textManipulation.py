import string

## Strips leading and trailing punctuation from a word(buggy)
def stripPunctuation(a_word):
	## loop untill all external punctuation has been removed
	while ((len(a_word) > 0) and ((a_word[0] in string.punctuation) or (a_word[len(a_word)-1] in string.punctuation))):
		for punct in string.punctuation:
			a_word = a_word.strip(punct)
	return a_word

## Loops over all words(whitespace deliminated) and returns a list of keywords
def extractKeywords(stext, stop_words):
	all_words = stext.split()
	keywords = []
	for word in all_words:
		if word not in stop_words:
			keywords.append(word)
	return keywords

## Uses simple edit distance algo to best guess what user ment(untested)
def alias(stext, dictionary):
    distances = {} ## Dict of form {edit dist: word}
    ## Uses first leter to cut down on search time
    first_letter = stext[0]
    for word in dictionary:
        if first_letter == word[0]:
            curr_dist = editDistance(word, stext)
            distances[curr_dist] = word
    ## A very python line
    return distances[distances.keys().sort()[0]]

## Creates 2d array
## Each char in first_str represents a row, each char in second_str represents column
## Each cell holds a tupel of form : (distance, direction)
def editDistance(first_str, second_str):
    ## Add extra space to both
    first_str = "-" + first_str
    second_str = "-" + second_str
    ## Create structure of matrix
    return_matrix = [None] * len(first_str)
    for row in xrange(len(first_str)):
        internal_matrix = [None] * len(second_str)
        for col in xrange(len(second_str)):
            if (row == 0) and (col != 0):
                internal_matrix[col] = (col,"hori")
            elif (col == 0) and (row != 0):
                internal_matrix[col] = (row,"vert")
            elif (row == 0) and (col == 0):
                internal_matrix[col] = (0,"diag")
            else:
                internal_matrix[col] = (None,None)
        return_matrix[row] = internal_matrix
    fillMatrix(return_matrix, first_str, second_str)
	rows = len(row_str)
	cols = len(col_str)
	distance, None = full_matrix[rows-1][cols-1]
	return distance

## Fills in values for rest of the matrix
## Calculates cell's value based on neighbors
def fillMatrix(empty_matrix, row_str, col_str):
    for x in xrange(1,len(row_str)):
        for y in xrange(1,len(col_str)):
            ## Set op_cost
            if row_str[x] != col_str[y]:
                op_cost = 1
            else:
                op_cost = 0
            ## Find min distance
            distance1, _ = empty_matrix[x-1][y-1]
            distance2, _ = empty_matrix[x][y-1]
            distance3, _ = empty_matrix[x-1][y]
            min_neighbor = min(distance1 + op_cost, distance2 + 1, distance3 + 1)
            ## Determine direction
            if min_neighbor == distance1 + op_cost:
                empty_matrix[x][y] = (min_neighbor, "diag")
            elif min_neighbor == distance2  + 1:
                empty_matrix[x][y] = (min_neighbor, "hori")
            elif min_neighbor == distance3 + 1:
                empty_matrix[x][y] = (min_neighbor, "vert")

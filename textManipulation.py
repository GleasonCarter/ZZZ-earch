import string

## Strips leading and trailing punctuation from a word(buggy)
def stripPunctuation(a_word):
	for punct in string.punctuation:
		a_word.strip(punct)

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
            ## Run edit distance TODO
            ## Add distance to list of distances
            pass
    ## A very python line
    return distances[distances.keys().sort()[0]]

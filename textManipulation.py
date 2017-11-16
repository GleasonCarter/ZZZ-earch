import string

## Strips leading and trailing punctuation from a word
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

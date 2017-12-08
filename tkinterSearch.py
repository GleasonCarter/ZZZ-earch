import sys
import os
from tkinter import *
import webbrowser
import string
import json
import requests
import random
import math

STOP_WORDS = ["the","of","a","and","to","was","he","in","it",
				"that","his","had","as","at","for","be",
				"but","is","on","or","which","by","from",
				"i","an","there","were","when","could","been",
				"her","out","this","are","said","what"]

## identifies ngrams in query
def ngram(n, stext, stop_words):
	ngrams = []
	words = stext.split()
	## increment first word of n-gram
	#print( "Constructing " + str(n) + "-grams:")
	for i in range(0, len(words)-(n-1)):
		## construct an individual ngram
		word_count = 0
		this_gram = ""
		for j in range(0, n):
			current_word = words[i + j]
			## ensure no stop words
			if current_word not in stop_words:
				word_count += 1;
				this_gram = this_gram + " " + current_word
				#print( "Adding " + current_word)
				this_gram = this_gram.lstrip(" ")
				#print ("Ngram now is " + this_gram)
		if word_count == n:
			ngrams.append(this_gram)
	return ngrams

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
			#possibly strip punctation here
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
    #distance, None = full_matrix[rows-1][cols-1]
    distance = full_matrix[rows-1][cols-1]
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

#all starts from the user input
def userInput(self):
        mtext = ment.get()
        if validSearch(mtext):
                manipulateText(mtext)

def validSearch(txt):
        return bool(re.search(r'[0-9A-Za-z]', txt))

#need to do stuff with text
def manipulateText(stext):
	word_arr = stext.split()
	#grab the key words
	#need to get the list of stop words
	#need access to indexing teams index here

	key_words = extractKeywords(stext,STOP_WORDS);
	#aliased_words = alias(stext,index)
	#print(stext)
	#print ("This is new:")
	for word in word_arr:
		stripPunctuation(word)
		#print(word)

	#write results to a file TODO need to implement transform search stuff
	transform_search = "Need to do --> Transformed Search "
	search_id = random.randint(0, 10000)
	for char in stext:
		search_id += ord(char)
	t_key_words = "Need to do --> Transformed Tokens"
	data1 = {}
	data1['search'] = search_id
	data1['raw'] = []
	data1['raw'].append({
		"raw_search": stext,
		"raw_tokens": key_words
	})
	data1['transformed'] = []
	data1['transformed'].append ({
		"transformed_search": transform_search,
		"transformed_tokens": t_key_words,
		"transformed_bigrams": ngram(2, stext, STOP_WORDS),
		"transformed_trigrams": ngram(3, stext, STOP_WORDS)
	})

	with open('data.txt', 'w') as outfile:
	    json.dump(data1, outfile)

	#url = "team__.cs.rpi.edu/ranking"
	url = "http://google.com"
	#make data look pretty
	data1 = json.dumps(data1,indent=4)
	#send data to ranking team
	r = requests.post(url, data=data1)
	print("\n\n" + data1)
	#Get data back from ranking
	r = requests.get(url)

	#give ranking our file that has the query
	#file = ranking("output.txt")
	results(stext,"file.txt")
	return

#need to print results somehow
def results(stext,file1):
	mGui2 = Tk()
	mGui2.focus_force()
	mGui2.geometry('800x500+300+250')
	mGui2.title('Results for "' + stext + '"')

	# Create scrollbar for right side of popup text box
	# Issues: Packs in above listed out "results" ADDRESS THIS
	frame = Frame(mGui2, bd=2, relief=SUNKEN, width=300, height=300)

	global canvas
	canvas = Canvas(frame, bd=0)
	yscrollbar = Scrollbar(frame, orient=VERTICAL)
	yscrollbar.pack(side=RIGHT,fill=Y)
	yscrollbar.config(command=canvas.yview)
	canvas.config(yscrollcommand=yscrollbar.set)
	canvas.pack(side=LEFT,expand=TRUE,fill=BOTH)
	frame.pack(side=LEFT, fill=BOTH, expand=True)
	canvas.bind_all("<MouseWheel>", onScroll)
	#data2 = json.load(open('HelloWorldTest.json'))

	#pprint(data2)

	data2 = json.load(open('Elephants.json'))

	j = 0
	array = []
	for d in data2['ranking']:
		url = (data2['ranking'][j]['url'])
		name = stext + str(j+1)

		addSearchResult(canvas, j, name, url, "this is a snippet")
		j+=1

	return

def onScroll(event):
        sign = event.delta / math.fabs(event.delta)
        sign = int(sign)
        canvas.yview_scroll(-sign * int(math.ceil(math.fabs(event.delta/120))), "units")

def callback(url):
    webbrowser.open(url)

#makes link labeled 'txt' that directs to 'url'
def makeLink(root, txt, url):
        link = Label(root, text=txt, anchor=NW, fg="blue", cursor="hand2", font="Arial 12 underline")
        link.bind("<Button-1>", lambda x: callback(url))
        return link

#add a search result to canvas
def addSearchResult(canvas, itemOffset, title, url, snippet):
        lnk = makeLink(canvas, title, url)
        canvas.create_window(10, 52 * itemOffset, anchor=NW, window=lnk)

        lbl = Label(canvas, anchor=NW, text="..." + snippet + "...", font="Arial 11")
        objId = canvas.create_window(10, 52 * itemOffset + 21, anchor=NW, window=lbl)

        canvas.config(scrollregion=canvas.bbox(ALL))
        return objId


def restart():
	python = sys.executable
	os.execl(python,python,*sys.argv)
	return

def quit(root):
	root.quit()


#set up the frame
mGui = Tk()
ment = StringVar()

#build the dimensions
mGui.geometry('800x110+300+90')
mGui.title('ZZZ-earch!!')

#mlabel = Label(mGui, text='My Label').pack()

#search Button
mbutton = Button(mGui,text ="Search", font="Arial 15", command = lambda: userInput(mGui), relief=GROOVE).pack(pady=10)
mGui.bind('<Return>', userInput)

#text box to enter search into
mEntry = Entry(mGui,textvariable=ment, width=120, font = "Arial 22", relief=RIDGE).pack(padx=20)

#mbutton = Button(mGui,text='Quit',command=quit).pack(side=LEFT, anchor=S, padx=[200,10])

mGui.mainloop()

import sys
import os
from Tkinter import *
import webbrowser
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
def userInput():
	mtext = ment.get()
	## mlabel2 = Label(mGui, text = mtext).pack()
	manipulateText(mtext)
	return

#need to do stuff with text
def manipulateText(stext):
	word_arr = stext.split()
	#grab the key words
	#need to get the list of stop words
	#need access to indexing teams index here
	stop_words = ["the","of","and","is"]
	key_words = extractKeywords(stext,stop_words);
	#aliased_words = alias(stext,index)
	print(stext)
	print ("This is new:")
	for word in word_arr:
		stripPunctuation(word)
		print(word)

	#write results to a file
	f1 = open("output.txt", "w")
	f1.write("WHOLE TEXT\n")
	f1.write(stext)
	f1.write("\nKEYWORDS\n")
	for kword in key_words:
		f1.write(kword)
		f1.write("\n")
	f1.write("ALIAS\n")
	#for aword in aliased_words:
	#	f1.write(aword)
	f1.close()

	#give ranking our file that has the query
	#file = ranking("output.txt")
	results(stext,"file.txt")
	return

#need to print results somehow
def results(stext,file1):
	mGui2 = Tk()
	mGui2.geometry('800x500+300+200')
	mGui2.title('Results for "' + stext + '"')
	#Label(mGui2,text=stext).pack()
	#mbutton = Button(mGui2,text ="Search",command = userInput, fg='red',bg = 'blue').pack()
	#text box to enter search into
	#mEntry = Entry(mGui2,textvariable=ment).pack()


	# Create scrollbar for right side of popup text box
	# Issues: Packs in above listed out "results" ADDRESS THIS
	frame = Frame(mGui2, bd=2, relief=SUNKEN, width=300, height=300)
	#frame.grid_rowconfigure(0, weight=1)
	#frame.grid_columnconfigure(0, weight=1)
	canvas = Canvas(frame, bd=0)
	#canvas.grid(row=0, column=0, sticky=N+S+E+W)
	yscrollbar = Scrollbar(frame, orient=VERTICAL)
	yscrollbar.pack(side=RIGHT,fill=Y)
	yscrollbar.config(command=canvas.yview)
	canvas.config(yscrollcommand=yscrollbar.set)
	canvas.pack(side=LEFT,expand=TRUE,fill=BOTH)
	frame.pack(side=LEFT, fill=BOTH, expand=True)
	# Currently creates for a listbox on popup text/results box
	#listbox = Listbox(mGui2, yscrollcommand=scrollbar.set)
	#for i in range(100):
	#	listbox.insert(END, str(i))
	#listbox.pack(side=LEFT, fill=BOTH)
	#scrollbar.config(command=listbox.yview)

	with open(file1, "r") as ins:
		array = []
		i = 0
		for line in ins:
			if(line != '\n'):
				array.append(line)
				#makeLink(canvas, line, r"http://www.google.com").pack(fill=X)

				lnk = makeLink(canvas, line, r"http://www.google.com")
				canvas.create_window(10, 35 * i, anchor=NW, window=lnk)
				i+=1
				canvas.config(scrollregion=canvas.bbox(ALL))
				#Label(canvas,text=line,anchor=NW).pack(fill=X)
	return

def callback(url):
    webbrowser.open(url)

#makes link labeled 'text' that directs to 'url' and packs it
def makeLink(root, txt, url):
        link = Label(root, text=txt, anchor=NW, fg="blue", cursor="hand2", font="Arial 10 underline")
        #link.pack(fill=X)
        link.bind("<Button-1>", lambda x: callback(url))
        return link

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
mGui.geometry('800x60+300+100')
mGui.title('ZZZ-earch!!')

#mlabel = Label(mGui, text='My Label').pack()

#search Button
mbutton = Button(mGui,text ="Search",command = userInput, fg='red',bg = 'blue').pack()

#text box to enter search into
mEntry = Entry(mGui,textvariable=ment, width=120).pack()

#mbutton = Button(mGui,text='Quit',command=quit).pack(side=LEFT, anchor=S, padx=[200,10])

mGui.mainloop()

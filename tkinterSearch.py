import sys
import os
import textManipulation as tM
from Tkinter import *

stp_wrds = ["the", "and", "of", "a", "but", "this", "that"] ## temporary test set of words

#all starts from the user input
def userInput():
	mtext = ment.get()
	mlabel2 = Label(mGui, text = mtext).pack()
	manipulateText(mtext)
	return

#need to do stuff with text
def manipulateText(stext):
	print "Base value:"
	print(stext)
	print "Keywords:"
	our_keywords = tM.extractKeywords(stext, stp_wrds)
	for word in our_keywords:
		print(word)

	#give the results of running the
	#file = ranking(arr or text file whatever we are giving them)
	results(stext,"file.txt")
	return

#need to print results somehow
def results(stext,file1):
	mGui2 = Tk()
	mGui2.geometry('450x450+200+100')
	mGui2.title('Results')
	Button(mGui2,text="Restart",command = restart).pack()
	Label(mGui2,text=stext).pack()
	with open(file1, "r") as ins:
		array = []
		for line in ins:
			array.append(line)
			Label(mGui2,text=line).pack()
	return

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
mGui.geometry('450x450+200+100')
mGui.title('My Search Bar')

#mlabel = Label(mGui, text='My Label').pack()

#search Button
mbutton = Button(mGui,text ="Search",command = userInput, fg='red',bg = 'blue').pack()


#text box to enter search into
mEntry = Entry(mGui,textvariable=ment).pack()



#mbutton = Button(mGui,text='Quit',command=quit).pack(side=LEFT, anchor=S, padx=[200,10])

mGui.mainloop()

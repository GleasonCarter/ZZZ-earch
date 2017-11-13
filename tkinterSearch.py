import sys
from tkinter import *

#all starts from the user input
def userInput():
	mtext = ment.get()
	mlabel2 = Label(mGui, text = mtext).pack()
	manipulateText(mtext)
	return 

#need to do stuff with text 
def manipulateText(stext):
	print(stext)
	results()
	return

#need to print results somehow
def results():
	Label(mGui,text="RESULTS").pack()
	with open("file.txt", "r") as ins:
		array = []
		for line in ins:
			array.append(line)
			Label(mGui,text=line).pack()
	return



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


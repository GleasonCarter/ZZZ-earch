import sys
import os
from tkinter import *
import webbrowser

#all starts from the user input
def userInput():
	mtext = ment.get()
	mlabel2 = Label(mGui, text = mtext).pack()
	manipulateText(mtext)
	return 

#need to do stuff with text 
def manipulateText(stext):
	word_arr = stext.split()
	print(stext)
	print ("This is new:")
	for word in word_arr:
		print(word)

	#give the results of running the 
	#file = ranking(arr or text file whatever we are giving them)
	results(stext,"file.txt")
	return

#need to print results somehow
def results(stext,file1):
	mGui2 = Tk()
	mGui2.geometry('1000x1000+200+100')
	mGui2.title('Results')
	Button(mGui2,text="Restart",command = restart).pack()
	Label(mGui2,text=stext).pack()

	# Create scrollbar for right side of popup text box
	# Issues: Packs in above listed out "results" ADDRESS THIS
	frame = Frame(mGui2, bd=2, relief=SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=1)
	yscrollbar = Scrollbar(frame, orient=VERTICAL)
	yscrollbar.grid(row=0, column=1, sticky=N+S)
	canvas = Canvas(frame, bd=0, yscrollcommand=yscrollbar.set)
	canvas.grid(row=0, column=0, sticky=N+S+E+W)
	yscrollbar.config(command=canvas.yview)
	frame.pack(side=LEFT, fill=BOTH, expand=True)
	# Currently creates for a listbox on popup text/results box
	#listbox = Listbox(mGui2, yscrollcommand=scrollbar.set)
	#for i in range(100):
	#	listbox.insert(END, str(i))
	#listbox.pack(side=LEFT, fill=BOTH)
	#scrollbar.config(command=listbox.yview)

	with open(file1, "r") as ins:
		array = []
		for line in ins:
			array.append(line)
			#makeLink(mGui2, line, r"http://www.google.com")
			Label(canvas,text=line,anchor=NW).pack(fill=X)
	return

def callback(url):
    webbrowser.open(url)

#makes link labeled 'text' that directs to 'url' and packs it
def makeLink(root, txt, url):
        link = Label(root, text=txt, fg="blue", cursor="hand2", font="Arial 10 underline")
        link.pack()
        link.bind("<Button-1>", lambda x: callback(url))

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
mGui.geometry('200x60+100+100')
mGui.title('My Search Bar')

#mlabel = Label(mGui, text='My Label').pack()

#search Button
mbutton = Button(mGui,text ="Search",command = userInput, fg='red',bg = 'blue').pack()

#text box to enter search into
mEntry = Entry(mGui,textvariable=ment).pack()

#mbutton = Button(mGui,text='Quit',command=quit).pack(side=LEFT, anchor=S, padx=[200,10])

mGui.mainloop()

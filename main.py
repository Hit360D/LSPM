from tkinter import *

#window
win = Tk()
win.title('LSPM - Least Secure Password Manager')

#---------------------------------------------#

def render_frame(selection):
	if selection == "Show tables":
		show_tables()

	# if selection == 1:

	# if selection == 2:

	# if selection == 3:

	# if selection == 4:

	# if selection == 5:

	# if selection == 6:

	# if selection == 7:


#---------------------------------------------#

def show_tables():
	cframe = Frame(frame, width=500, height=500)
	cframe.pack(expand='true', fill='both', side='top')
	lab = Label(cframe, text="works")
	lab.pack()


#---------------------------------------------#

#sidebar
sidebar = Frame(win, width=200, height=500, bg='#111111')

#to get active selection
selection = "nothing"
def getSel(event):
	selection = str(listbox.get(listbox.curselection()))
	render_frame(selection)

#list
listbox = Listbox(sidebar, relief='flat', bd=0, selectmode='single', bg='#111111', fg='#666666')
listbox.insert(0, "Show tables")
listbox.insert(1, "Create new table")
listbox.insert(2, "Table properties")
listbox.insert(3, "Add an entry")
listbox.insert(4, "Remove an entry")
listbox.insert(5, "Find an entry")
listbox.insert(6, "Show all entries")
listbox.insert(7, "Remove table")

listbox.bind('<<ListboxSelect>>', getSel)

listbox.pack()

sidebar.pack(side = 'left', expand = 'false', fill='both')

#main view
frame = Frame(win, width=500, height=500, bg='#444444')
frame.pack(expand='true', fill='both', side='right')

#function to render inside parent frame
# render_frame(selection, frame)

win.mainloop()







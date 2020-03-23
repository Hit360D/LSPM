from tkinter import *
import mysql.connector

#window
win = Tk()
win.geometry('1000x1000')
win.title('LSPM - Least Secure Password Manager')

#---------------------------------------------#

#command module
def sql_command(type):
	connection = mysql.connector.connect(host='localhost', database='suryansh', user='suryansh', password='suryansh')

	if connection.is_connected():
		db_Info = connection.get_server_info()
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		return (db_Info, record)


#---------------------------------------------#

def render_frame(selection):
	if selection == "Show tables":
		show_tables(selection)

	# if selection == "Create new table":

	# if selection == "Table properties":

	# if selection == "Add an entry":

	# if selection == "Remove an entry":

	# if selection == "Find an entry":

	# if selection == "Show all entries":

	# if selection == "Remove table":


#---------------------------------------------#

def show_tables(selection):
	cframe = Frame(frame, width=500, height=500)

	output = Entry(cframe, borderwidth=0)
	db_Info, record = sql_command(selection)
	output.insert(0, "Connected to MySQL Database version " + db_Info)
	output.pack()

	cframe.pack(expand='true', fill='both', side='top')


#---------------------------------------------#


#---------------------------------------------#

#sidebar
sidebar = Frame(win, width=200, height=500, bg='#111111')

#to get active selection from list
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

win.mainloop()







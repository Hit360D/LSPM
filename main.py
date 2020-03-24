from tkinter import *
from tkinter import ttk
import mysql.connector

#window
win = Tk()
win.geometry('700x500')
win.title('LSPM - Least Secure Password Manager')

style = ttk.Style(win)

#---------------------------------------------#

#command module (under parent = cframe)
def sql_command(selection):
	connection = mysql.connector.connect(host='localhost', database='suryansh', user='suryansh', password='suryansh')

	if connection.is_connected():
		db_Info = connection.get_server_info()
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()

		#sql queries
		create_table_query = "SHOW tables"
		cursor = connection.cursor()
		result = cursor.execute(create_table_query)
		table = cursor.fetchall()
		return table



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
	#remove the frame if it already exists
	for child in frame.winfo_children():
		child.destroy()

	cframe = Frame(frame, width=500, height=500, bg="#444444")

	#ttk treeview
	tree = ttk.Treeview(cframe)

	table_label = Label(cframe, text="Tables", fg="white", bg="#444444")
	
	#change treeview style
	style.configure("Treeview", relief="flat", bg = "#444444", fieldbackground="#444444", fg="#444444")

	#get tables
	sql_tables = sql_command(selection)
	for x in sql_tables:
		tree.insert("", 0, text=x)

	table_label.pack()
	tree.pack(side='top', fill='x')

	cframe.pack(expand='true', fill='both', side='top')


#---------------------------------------------#


#---------------------------------------------#

#sidebar
sidebar = Frame(win, width=200, height=500, bg='#111111')

#to get active selection from list
selection = "nothing"
def getSel(event):
	selection = str(listbox.get(listbox.curselection()))
	#render frame based on selection
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

#get list selection
listbox.bind('<<ListboxSelect>>', getSel)

listbox.pack()

sidebar.pack(side = 'left', expand = 'false', fill='both')

#main view
frame = Frame(win, width=500, height=500, bg='#444444')
frame.pack(expand='true', fill='both', side='right')

win.mainloop()







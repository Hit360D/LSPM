from tkinter import *
from tkinter import ttk
import mysql.connector

#window
win = Tk()
win.geometry('700x500')
win.title('LSPM - Least Secure Password Manager')

style = ttk.Style(win)

#---------------------------------------------#

def render_frame(selection):
	if selection == "Show tables":
		show_tables(selection)

	if selection == "Create new table":
		create_table(selection)

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





def create_table(selection):
	#remove the frame if it already exists
	for child in frame.winfo_children():
		child.destroy()

	#get field input and execute code
	def btn_input(selection, field):
		field_text = field.get("1.0",'end-1c')

		connection = mysql.connector.connect(host='localhost', database='suryansh', user='suryansh', password='suryansh')

		if connection.is_connected():
			db_Info = connection.get_server_info()
			cursor = connection.cursor()
			cursor.execute("select database();")
			record = cursor.fetchone()

			create_table_query = "CREATE TABLE " + field_text + " (id int not null AUTO_INCREMENT, website varchar(200) not null, username varchar(200) not null, password varchar(200) not null, primary key (id))"
			cursor = connection.cursor()
			result = cursor.execute(create_table_query)

		#to clear text field
		field.delete(1.0, END)


	cframe = Frame(frame, width=500, height=500, bg="#444444")

	text = Label(cframe, text="Table name", width=10, bg="#444444", fg='white')
	text.grid(row=0, column=0)
	field = Text(cframe, height=1, width=50)
	field.grid(row=0, column=1)
	add_button = Button(cframe, text="Add table", command=lambda: btn_input(selection, field))
	add_button.grid(row=1, column=1)



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
listbox.insert(2, "Add an entry")
listbox.insert(3, "Remove an entry")
listbox.insert(4, "Find an entry")
listbox.insert(5, "Show all entries")
listbox.insert(6, "Remove table")

#get list selection
listbox.bind('<<ListboxSelect>>', getSel)

listbox.pack()

sidebar.pack(side = 'left', expand = 'false', fill='both')

#main view
frame = Frame(win, width=500, height=500, bg='#444444')
frame.pack(expand='true', fill='both', side='right')

win.mainloop()







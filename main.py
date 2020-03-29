from tkinter import *
from tkinter import ttk
import mysql.connector

#window
win = Tk()
win.geometry('1000x500')
win.title('LSPM - Least Secure Password Manager')

style = ttk.Style(win)

#---------------------------------------------#

def render_frame(selection):
    if selection == "Show tables":
        show_tables(selection)

    if selection == "Find password":
        find_password(selection)


#---------------------------------------------#

#show tables
def show_tables(selection):
    #remove the frame if it already exists
    for child in frame.winfo_children():
        child.destroy()

    #get field input and execute code
    def btn_input(selection, field):
        field_text = field.get("1.0",'end-1c')

        connection = mysql.connector.connect(host='localhost', database='suryansh', user='suryansh', password='suryansh')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor(buffered = True)
            cursor.execute("select database();")
            record = cursor.fetchone()

            create_table_query = "CREATE TABLE " + field_text + " (id int not null AUTO_INCREMENT, website varchar(200) not null, username varchar(200) not null, password varchar(200) not null, primary key (id))"
            cursor = connection.cursor(buffered = True)
            result = cursor.execute(create_table_query)
            if connection.is_connected():
                cursor.close()
                connection.close()

        #to clear text field
        field.delete(1.0, END)

        #remove the frame if it already exists
        for child in frame.winfo_children():
            child.destroy()
        show_tables(selection)

    #to load treeview content
    def sql_command(selection):
        connection = mysql.connector.connect(host='localhost', database='suryansh', user='suryansh', password='suryansh')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            cursor = connection.cursor(buffered = True)
            cursor.execute("select database();")
            record = cursor.fetchone()

            #sql queries
            create_table_query = "SHOW tables"
            cursor = connection.cursor(buffered = True)
            result = cursor.execute(create_table_query)
            table = cursor.fetchall()
            if connection.is_connected():
                cursor.close()
                connection.close()
            return table

    cframe = Frame(frame, width=500, height=500, bg="#444444")

    #text = Label(cframe, text="Table name", width=10, bg="#444444", fg='white')
    #text.grid(row=0, column=0)
    field = Text(cframe, height=1, width=100)
    field.grid(row=1, column=0)
    add_button = Button(cframe, text="Add table", command=lambda: btn_input(selection, field))
    add_button.grid(row=2, column=0)

    #ttk treeview
    tree = ttk.Treeview(cframe, selectmode='browse')

    table_label = Label(cframe, text="Tables", fg="white", bg="#444444")
    
    #change treeview style
    style.configure("Treeview", relief="flat", bg = "#444444", fieldbackground="#444444", fg="#444444", expand='true', fill='x')

    #get tables
    sql_tables = sql_command(selection)
    for x in sql_tables:
        tree.insert("", 0, text=x)

    table_label.grid(row=3, column=0)

    #scrollbar for treeview
    scrollbar = Scrollbar(cframe, orient='vertical', command= tree.yview)
    tree.config(yscrollcommand = scrollbar.set)

    tree.grid(row=4, column=0, sticky="NSEW", padx=10, pady=5)
    scrollbar.grid(row=4, column=1, sticky="NSW", columnspan=5, rowspan=4)

    cframe.pack(expand='true', fill='both', side='top')

    


#find password
def find_password(selection):
    #remove the frame if it already exists
    for child in frame.winfo_children():
        child.destroy()

    #to fill tree with tuples
    def show_table(table):
        for x in table:
            tree.insert("", 0, text=x)
    
    
    #button1 function
    def btn_input_one(text1): 

        text_input = text1.get("1.0", "end-1c")

        connection = mysql.connector.connect(host='localhost',
                                         database='suryansh',
                                         user='suryansh',
                                         password='suryansh')
        if connection.is_connected():
            cursor = connection.cursor(buffered = True)
            cursor.execute("select database();")


            #sql queries
            create_table_query = "select * from " + text_input
            cursor = connection.cursor(buffered = True)
            result = cursor.execute(create_table_query)
            table = cursor.fetchall()
            show_table(table)


    #subframe
    cframe = Frame(frame, width=500, height=500, bg='#444444')

    tree = ttk.Treeview(cframe, selectmode='browse', columns=('username', 'password'))

    #to find table
    label1 = Label(cframe, text='Table', bg='#444444', fg='white')
    label1.pack(side='top')

    text1 = Text(cframe, height=1, width=100)
    text1.pack(side='top')

    button1 = Button(cframe, text='Show all content', command=lambda: btn_input_one(text1))
    button1.pack(side='top')




    #to find table contents
    label2 = Label(cframe, text='\nFind password by website', bg='#444444', fg='white')
    label2.pack(side='top')

    text2 = Text(cframe, height=1, width=100)
    text2.pack(side='top')

    button2 = Button(cframe, text='Find')
    button2.pack(side='top')


    tree.heading('#0', text='Website')
    tree.heading('#1', text='Username')
    tree.heading('#2', text='Password')

    #content
    tree.pack(expand='true', fill='both', side='left')

    #scrollbar for content
    scrollbar = Scrollbar(cframe, command= tree.yview)

    tree.config(yscrollcommand = scrollbar.set)

    scrollbar.pack(side='right', fill='y')


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
listbox.insert(1, "Find password")

#get list selection
listbox.bind('<<ListboxSelect>>', getSel)

listbox.pack()

sidebar.pack(side = 'left', expand = 'false', fill='both')

#main view
frame = Frame(win, width=500, height=500, bg='#444444')
frame.pack(expand='true', fill='both', side='right')

win.mainloop()







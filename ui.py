#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.9
# In conjunction with Tcl version 8.6
#    Mar 01, 2017 10:44:06 PM
import sys

from functools import partial

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.geometry("600x600+465+46")
    root.title("Database")
    root.configure(background="#34abd9")

    top = Database (root)
    root.mainloop()

class Database:
    def __init__(self, top=None):
        self.root=top
        self.show_login(top)
    
    def show_login(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        self.password = Entry(self.root, show="*")
        self.password.place(relx=0.33, rely=0.38, relheight=0.07, relwidth=0.31)
        self.password.configure(background="white")
        self.password.configure(font="TkFixedFont")
        self.password.configure(width=150)

        self.login_label = Label(self.root)
        self.login_label.place(relx=0.17, rely=0.38, height=48, width=96)
        self.login_label.configure(activebackground="#80ecec")
        self.login_label.configure(background="#34abd9")
        self.login_label.configure(text='''Password''')
        self.login_label.configure(width=96)

        self.login_button = Button(top, command=self.show_main)
        self.login_button.place(relx=0.43, rely=0.5, height=26, width=70)
        self.login_button.configure(activebackground="#d9d9d9")
        self.login_button.configure(text='''Submit''')

    def show_main(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        self.clear_screen()
        self.cat_home = Button(self.root, command=self.show_category)
        self.cat_home.place(relx=0.38, rely=0.26, height=46, width=227)
        self.cat_home.configure(activebackground="#d9d9d9")
        self.cat_home.configure(text='''Add Category''')

        self.cus_home = Button(self.root, command=self.show_customer)
        self.cus_home.place(relx=0.38, rely=0.33, height=46, width=227)
        self.cus_home.configure(activebackground="#d9d9d9")
        self.cus_home.configure(text='''Add Customer''')
        
        self.search_home = Button(self.root)
        self.search_home.place(relx=0.38, rely=0.4, height=46, width=227)
        self.search_home.configure(activebackground="#d9d9d9")
        self.search_home.configure(text='''Search''')

    def show_category(self):

        self.clear_screen()
        
        self.Label1 = Label(self.root)
        self.Label1.place(relx=0.13, rely=0.25, height=18, width=96)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#34acd9")
        self.Label1.configure(text='''Category id''')

        self.Label2 = Label(self.root)
        self.Label2.place(relx=0.11, rely=0.33, height=18, width=96)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#34acd9")
        self.Label2.configure(text='''Category name''')

        self.cat_id = Text(self.root)
        self.cat_id.place(relx=0.38, rely=0.23, relheight=0.04, relwidth=0.19)
        self.cat_id.configure(background="white")
        self.cat_id.configure(font="TkTextFont")
        self.cat_id.configure(selectbackground="#c4c4c4")
        self.cat_id.configure(width=86)
        self.cat_id.configure(wrap=WORD)

        self.cat_name = Text(self.root)
        self.cat_name.place(relx=0.38, rely=0.32, relheight=0.04, relwidth=0.43)
        self.cat_name.configure(background="white")
        self.cat_name.configure(font="TkTextFont")
        self.cat_name.configure(selectbackground="#c4c4c4")
        self.cat_name.configure(width=196)
        self.cat_name.configure(wrap=WORD)

        self.save = Button(self.root)
        self.save.place(relx=0.91, rely=0.43, height=36, width=117)
        self.save.configure(activebackground="#d9d9d9")
        self.save.configure(text='''Save''')

        self.back = Button(self.root, command=self.show_main)
        self.back.place(relx=0.58, rely=0.43, height=36, width=117)
        self.back.configure(activebackground="#d9d9d9")
        self.back.configure(text='''Back''')

        self.Label3 = Label(self.root)
        self.Label3.place(relx=0.53, rely=0.07, height=68, width=126)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="#00ac00")
        self.Label3.configure(background="#34acd9")
        self.Label3.configure(borderwidth="10")
        self.Label3.configure(foreground="#59f9ce")
        self.Label3.configure(text='''Add Category''')


    def show_customer(self):

        self.clear_screen()
        
        self.cu_id = Entry(self.root)
        self.cu_id.place(relx=0.31, rely=0.22, relheight=0.03, relwidth=0.14)
        self.cu_id.configure(background="white")
        self.cu_id.configure(font="TkFixedFont")
        self.cu_id.configure(selectbackground="#c4c4c4")

        self.Label1 = Label(self.root)
        self.Label1.place(relx=0.16, rely=0.22, height=18, width=77)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#34acd9")
        self.Label1.configure(text='''Customer id''')

        self.cu_name = Entry(self.root)
        self.cu_name.place(relx=0.31, rely=0.26, relheight=0.03, relwidth=0.41)
        self.cu_name.configure(background="white")
        self.cu_name.configure(font="TkFixedFont")
        self.cu_name.configure(selectbackground="#c4c4c4")

        self.Label2 = Label(self.root)
        self.Label2.place(relx=0.13, rely=0.26, height=18, width=100)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#34acd9")
        self.Label2.configure(text='''Customer name''')

        self.cat_list = Listbox(self.root)
        self.cat_list.place(relx=0.31, rely=0.32, relheight=0.03, relwidth=0.4)
        self.cat_list.configure(background="white")
        self.cat_list.configure(font="TkFixedFont")
        self.cat_list.configure(selectbackground="#c4c4c4")
        self.cat_list.configure(width=274)
        for item in ["one", "two", "three", "four"]:
            self.cat_list.insert(END, item)
#        self.cat_list.configure(listvariable=[1,2,3,4]) #list variable

        self.Label3 = Label(self.root)
        self.Label3.place(relx=0.18, rely=0.32, height=18, width=76)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(background="#34acd9")
        self.Label3.configure(text='''Category''')


        self.Label4 = Label(self.root)
        self.Label4.place(relx=0.16, rely=0.37, height=18, width=96)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(background="#34acd9")
        self.Label4.configure(text='''Password''')

        self.password = Entry(self.root)
        self.password.place(relx=0.31, rely=0.37, relheight=0.03, relwidth=0.41)
        self.password.configure(background="white")
        self.password.configure(font="TkFixedFont")
        self.password.configure(selectbackground="#c4c4c4")

        self.Label5 = Label(self.root)
        self.Label5.place(relx=0.38, rely=0.04, height=58, width=156)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(background="#34acd9")
        self.Label5.configure(foreground="#381379")
        self.Label5.configure(text='''Add Customer''')

        self.Label6 = Label(self.root)
        self.Label6.place(relx=0.13, rely=0.44, height=28, width=116)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(background="#34acd9")
        self.Label6.configure(text='''Phone number''')

        self.Entry4 = Entry(self.root)
        self.Entry4.place(relx=0.31, rely=0.44, relheight=0.03, relwidth=0.41)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")

        self.Label7 = Label(self.root)
        self.Label7.place(relx=0.24, rely=0.51, height=28, width=36)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(background="#34acd9")
        self.Label7.configure(text='''Age''')

        self.Entry5 = Entry(self.root)
        self.Entry5.place(relx=0.31, rely=0.51, relheight=0.03, relwidth=0.41)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")

        self.Label8 = Label(self.root)
        self.Label8.place(relx=0.21, rely=0.6, height=18, width=52)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(background="#34acd9")
        self.Label8.configure(text='''Address''')

        self.Entry6 = Entry(self.root)
        self.Entry6.place(relx=0.31, rely=0.58, relheight=0.07, relwidth=0.41)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")

        self.back_cu = Button(self.root, command=self.show_main)
        self.back_cu.place(relx=0.47, rely=0.7, height=46, width=117)
        self.back_cu.configure(activebackground="#d9d9d9")
        self.back_cu.configure(text='''Back''')

        self.save_cu = Button(self.root)
        self.save_cu.place(relx=0.69, rely=0.7, height=46, width=127)
        self.save_cu.configure(activebackground="#d9d9d9")
        self.save_cu.configure(text='''Save''')



    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            


    def pdb(self):
        import pdb;pdb.set_trace()



if __name__ == '__main__':
    vp_start_gui()

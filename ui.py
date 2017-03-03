import ttk
import tkMessageBox

from Tkinter import *
from application import access_db, add_category, DuplicateEntry, validate_category, Category, Customer, validate_customer_data, add_customer,\
    show_all_category, get_data, DataError, delete_entry
from collections import OrderedDict    


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

        '''This class configurs and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        self.m_password = Entry(self.root, show="*")
        self.m_password.place(relx=0.33, rely=0.38, relheight=0.07, relwidth=0.31)
        self.m_password.configure(background="white")
        self.m_password.configure(font="TkFixedFont")
        self.m_password.configure(width=150)

        self.login_label = Label(self.root)
        self.login_label.place(relx=0.17, rely=0.38, height=48, width=96)
        self.login_label.configure(activebackground="#80ecec")
        self.login_label.configure(background="#34abd9")
        self.login_label.configure(text='''Password''')
        self.login_label.configure(width=96)

        self.login_button = Button(top, command=self.check_user)
        self.login_button.bind('<Return>', lambda x: self.check_user())
        self.login_button.place(relx=0.43, rely=0.5, height=26, width=70)
        self.login_button.configure(activebackground="#d9d9d9")
        self.login_button.configure(text='''Submit''')

    def check_user(self):
        password = self.m_password.get()
        db = access_db(password) 
        if db:
            self.show_main()
        else:
             tkMessageBox.showerror(title="Error",message="Wrong Password",parent=self.root)

    def save_category(self):
        cat_id = self.cat_id.get()
        cat_name = self.cat_name.get()
        response = validate_category(cat_id, cat_name)
        if response:
            messages = []
            for key in response:
                message = "{}:{}".format(key, response[key])
                messages.append(message)
            tkMessageBox.showerror(title="Error", message='\n'.join(messages), parent=self.root)
        else:
            try:
                add_category(cat_name, int(cat_id))
                self.show_category()
            except DuplicateEntry as e:
                tkMessageBox.showerror(title="Error", message=e.message, parent=self.root)

         
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
        self.cat_home.bind('<Return>', lambda x: self.show_category())
        self.cat_home.place(relx=0.38, rely=0.26, height=46, width=227)
        self.cat_home.configure(activebackground="#d9d9d9")
        self.cat_home.configure(text='''Add Category''')

        if show_all_category():
            self.cus_home = Button(self.root, command=self.show_customer)
            self.cus_home.bind('<Return>', lambda x: self.show_customer())
            self.cus_home.place(relx=0.38, rely=0.33, height=46, width=227)
            self.cus_home.configure(activebackground="#d9d9d9")
            self.cus_home.configure(text='''Add Customer''')
        
        self.search_home = Button(self.root, command=self.show_search) 
        self.search_home.bind('<Return>', lambda x: self.show_search())
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

        self.cat_id = Entry(self.root)
        self.cat_id.place(relx=0.38, rely=0.23, relheight=0.04, relwidth=0.19)
        self.cat_id.configure(background="white")
        self.cat_id.configure(font="TkTextFont")
        self.cat_id.configure(selectbackground="#c4c4c4")
        self.cat_id.configure(width=86)

        self.cat_name = Entry(self.root)
        self.cat_name.place(relx=0.38, rely=0.32, relheight=0.04, relwidth=0.43)
        self.cat_name.configure(background="white")
        self.cat_name.configure(font="TkTextFont")
        self.cat_name.configure(selectbackground="#c4c4c4")
        self.cat_name.configure(width=196)

        self.save_ca = Button(self.root, command=self.save_category)
        self.save_ca.bind('<Return>', lambda x: self.save_category())
        self.save_ca.place(relx=0.91, rely=0.43, height=36, width=117)
        self.save_ca.configure(activebackground="#d9d9d9")
        self.save_ca.configure(text='''Save''')

        self.back_ca = Button(self.root, command=self.show_main)
        self.back_ca.bind('<Return>', lambda x: self.show_main())
        self.back_ca.place(relx=0.58, rely=0.43, height=36, width=117)
        self.back_ca.configure(activebackground="#d9d9d9")
        self.back_ca.configure(text='''Back''')

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

        self.var = StringVar(self.root)
 
        value_list = show_all_category()
        self.var.set(value_list[0])
        self.cat_list = apply(OptionMenu, (self.root, self.var)+tuple(value_list))
        self.cat_list.place(relx=0.31, rely=0.32, relheight=0.03, relwidth=0.4)
        self.cat_list.configure(background="white")
        self.cat_list.configure(font="TkFixedFont")
        self.cat_list.configure(width=274)

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

        self.password = Entry(self.root, show='*')
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

        self.phone = Entry(self.root)
        self.phone.place(relx=0.31, rely=0.44, relheight=0.03, relwidth=0.41)
        self.phone.configure(background="white")
        self.phone.configure(font="TkFixedFont")
        self.phone.configure(selectbackground="#c4c4c4")

        self.Label7 = Label(self.root)
        self.Label7.place(relx=0.24, rely=0.51, height=28, width=36)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(background="#34acd9")
        self.Label7.configure(text='''Age''')

        self.age = Entry(self.root)
        self.age.place(relx=0.31, rely=0.51, relheight=0.03, relwidth=0.41)
        self.age.configure(background="white")
        self.age.configure(font="TkFixedFont")
        self.age.configure(selectbackground="#c4c4c4")

        self.Label8 = Label(self.root)
        self.Label8.place(relx=0.21, rely=0.6, height=18, width=52)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(background="#34acd9")
        self.Label8.configure(text='''Address''')

        self.address = Entry(self.root)
        self.address.place(relx=0.31, rely=0.58, relheight=0.07, relwidth=0.41)
        self.address.configure(background="white")
        self.address.configure(font="TkFixedFont")
        self.address.configure(selectbackground="#c4c4c4")

        self.back_cu = Button(self.root, command=self.show_main)
        self.back_cu.bind('<Return>', lambda x: self.show_customer())
        self.back_cu.place(relx=0.47, rely=0.7, height=46, width=117)
        self.back_cu.configure(activebackground="#d9d9d9")
        self.back_cu.configure(text='''Back''')

        self.save_cu = Button(self.root, command=self.save_customer)
        self.save_cu.bind('<Return>', lambda x: self.save_customer())
        self.save_cu.place(relx=0.69, rely=0.7, height=46, width=127)
        self.save_cu.configure(activebackground="#d9d9d9")
        self.save_cu.configure(text='''Save''')

    def search_entry(self):
        search_result = OrderedDict()
        if  self.rad_var.get() == 1:
            category = True
        else:
            category = False

        value = self.search_box.get()
        try:
            int(value)
        except ValueError:
            tkMessageBox.showerror(title="Error", message='Id must be number', parent=self.root)            
            self.show_search()
        try:
            self.result = get_data(int(value), category)
            if category:
                search_result['Category id'] = self.result.category_id
                search_result['Category name'] = self.result.category_name
            else:
                search_result['Customer id'] = self.result.customer_id
                search_result['Customer name'] = self.result.customer_name
                search_result['Category name'] = self.result.category.category_name
                search_result['Phone'] = self.result.phone
                search_result['Password'] = 8*'*'
                search_result['Age'] = self.result.age
                search_result['Address'] = self.result.address
            self.show_search(data=search_result)
        except DataError as e:
            tkMessageBox.showerror(title="Error", message=e.message, parent=self.root)            
            self.show_search()

    def delete_object(self):
        if  self.rad_var.get() == 1:
            category = True
            id = self.result.category_id
        else:
            category = False
            id = self.result.customer_id
        
        delete_entry(id, category)
        self.show_search()
    
    def show_search(self, data=None):

        if not data:
            self.clear_screen()
        
        self.head = Label(self.root)
        self.head.place(relx=0.29, rely=0.01, height=78, width=156)
        self.head.configure(activebackground="#f9f9f9")
        self.head.configure(background="#34abd9")
        self.head.configure(text='''Search''')

        self.search_box = Entry(self.root)
        self.search_box.place(relx=0.2, rely=0.23, relheight=0.03, relwidth=0.32)
        self.search_box.configure(background="white")
        self.search_box.configure(font="TkFixedFont")
        self.search_box.configure(selectbackground="#c4c4c4")

        self.rad_var = IntVar()
        self.rad_var.set(1)
        self.cat_rad = Radiobutton(self.root, variable=self.rad_var, value=1)
        self.cat_rad.place(relx=0.13, rely=0.14, relheight=0.03, relwidth=0.2)
        self.cat_rad.configure(activebackground="#d9d9d9")
        self.cat_rad.configure(background="#34acd9")
        self.cat_rad.configure(borderwidth="0")
        self.cat_rad.configure(justify=LEFT)
        self.cat_rad.configure(text='''Category''')

        self.cus_rad = Radiobutton(self.root, variable=self.rad_var, value=2)
        self.cus_rad.place(relx=0.4, rely=0.14, relheight=0.03
                , relwidth=0.2)
        self.cus_rad.configure(activebackground="#d9d9d9")
        self.cus_rad.configure(background="#34acd9")
        self.cus_rad.configure(borderwidth="0")
        self.cus_rad.configure(justify=LEFT)
        self.cus_rad.configure(text='''Customer''')

        self.id_label = Label(self.root)
        self.id_label.place(relx=0.11, rely=0.23, height=18, width=36)
        self.id_label.configure(activebackground="#f9f9f9")
        self.id_label.configure(background="#34acd9")
        self.id_label.configure(text='''Id''')

        self.search = Button(self.root, command=self.search_entry)
        self.search.bind('<Return>', lambda x: self.search_entry())
        self.search.place(relx=0.58, rely=0.22, height=26, width=68)
        self.search.configure(activebackground="#d9d9d9")
        self.search.configure(text='''Search''')

        if data:
            messages = []
            for key in data:
                message = "{}:{}".format(key, data[key])
                messages.append(message)

            self.delete = Button(self.root, command=self.delete_object)
            self.delete.bind('<Return>', lambda x: self.delete_object())
            self.delete.place(relx=0.64, rely=0.78, height=26, width=64)
            self.delete.configure(activebackground="#d9d9d9")
            self.delete.configure(text='''Delete''')

            self.back_se = Button(self.root, command=self.show_main)
            self.back_se.bind('<Return>', lambda x: self.show_main())
            self.back_se.place(relx=0.2, rely=0.78, height=26, width=55)
            self.back_se.configure(activebackground="#d9d9d9")
            self.back_se.configure(text='''Back''')

            self.Label3 = Label(self.root)
            self.Label3.place(relx=0.11, rely=0.32, height=298, width=346)
            self.Label3.configure(activebackground="#f9f9f9")
            self.Label3.configure(background="#34acd9")
            self.Label3.configure(text='\n'.join(messages))

    def save_customer(self):
        cu_id = self.cu_id.get()
        cu_name= self.cu_name.get()   
        category = self.var.get()
        password = self.password.get()
        age = self.age.get()
        address = self.address.get()
        phone = self.phone.get()
        
        response = validate_customer_data(cu_id, cu_name, category, age, phone, address, password)
        if response:
            messages = []
            for key in response:
                message = "{}:   {}".format(key, response[key])
                messages.append(message)
            tkMessageBox.showerror(title="Error", message='\n'.join(messages), parent=self.root)
        else:
            try:
                add_customer(cu_id, cu_name, category, age, phone, address, password)
            except DuplicateEntry as e:
                tkMessageBox.showerror(title="Error", message=e.message, parent=self.root)
        self.show_customer() 

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            


    def pdb(self):
        import pdb;pdb.set_trace()



if __name__ == '__main__':
    vp_start_gui()


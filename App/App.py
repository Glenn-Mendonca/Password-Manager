#Dependencies
import os, sys
from re import S
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import CENTER, END 
import pyperclip as pc
import Cryptography
import hashlib
import ctypes
import json

#Output higher res windows
ctypes.windll.shcore.SetProcessDpiAwareness(2)

#Data Directories
DIRS = ["User", "Data", "Images"]

#Create User and Data Directories
def init_directories():
    path_prefix = os.path.split(sys.argv[0])[0]
    if path_prefix != "":
        for indx, dir in enumerate(DIRS):
            DIRS[indx] = os.path.join(os.getcwd(), path_prefix, dir) 

    for dir in DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)

#Create file at specified path to store json data
def create_json_file(path, filename):
    if not os.path.exists(os.path.join(path, filename)):
        with open(os.path.join(path, filename), 'w') as file:
            json.dump({},file)

#Main App Class
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        #Root Window
        self.title('Password_M')
        self.geometry('710x400')
        self.resizable(0,0)

        #Variables
        self.Name = tk.StringVar()
        self.Pwd = tk.StringVar()
        self.Email = tk.StringVar()

        #Data window vars
        self.Site = tk.StringVar()
        self.SitePassword = tk.StringVar()

        #Icon
        icon = tk.PhotoImage(file=os.path.join(DIRS[2], "icon.png"))
        self.iconphoto(False,icon)

        #Background
        self.canvas = tk.Canvas(self,width=710,height=400,borderwidth=0)
        self.background = tk.PhotoImage(file=os.path.join(DIRS[2], "home.png"))
        self.canvas.create_image(0,0,anchor='nw',image=self.background)

        #Create User Password file if doesn't exist
        create_json_file(DIRS[0], "users.json")

        #User data 
        self.user_data = None
        self.loggedin = False

        #Load Startup Screen
        self.main()

    #Main Startup Screen
    def main(self):
        self.clearCanvas()
        uname = tk.Entry(self.canvas,textvariable=self.Name,font=("Arial", 10),justify='center')
        pwd = tk.Entry(self.canvas,textvariable=self.Pwd,font=("Arial", 10),justify='center')
        self.btn1 = tk.Button(text='Sign In',padx=10,font=("Arial", 10, "bold"),border=0,command=self.check)
        self.btn2 = tk.Button(text='Register',padx=10,font=("Arial", 10, "bold"),border=0,command=self.register)
        self.curved_rectangle(133, 75, 577, 325, fill='#fc9803', r=50,tags="interface")
        self.canvas.create_text(350, 100, text= "Login",fill="black",font=('Prompt 14 bold'),tags="interface")
        self.canvas.create_line(133, 120, 577, 120, fill='white',tags="interface")
        self.canvas.create_text(250, 155, text= "Username:",fill="black",font=('Prompt 12 bold'),tags="interface")
        self.canvas.create_window(410,155,window=uname,width=200,height=30,tags="interface")
        self.canvas.create_text(250, 200, text= "Password:",fill="black",font=('Prompt 12 bold'),tags="interface")
        self.canvas.create_window(410,200,window=pwd,width=200,height=30,tags="interface")
        self.btn1.place(x=310,y=230)
        self.canvas.create_text(305, 290, text= "New here? ",fill="black",font=('Prompt 12 bold'),tags="interface")
        self.btn2.place(x=365,y=275)
        self.canvas.create_text(660, 390, text= "© Glenn_M",fill="white",font=('Prompt 9 bold'),tags="interface")
        self.canvas.pack()

    #Registration Window
    def register(self):
        self.clearCanvas()
        uname = tk.Entry(self.canvas,textvariable=self.Name,font=("Arial", 10),justify='center')
        email = tk.Entry(self.canvas,textvariable=self.Email,font=("Arial", 10),justify='center')
        pwd = tk.Entry(self.canvas,textvariable=self.Pwd,font=("Arial", 10),justify='center')
        self.btn3 = tk.Button(text='Sign Up',padx=10,font=("Arial", 10, "bold"),border=0,command=self.add_user)
        self.curved_rectangle(133, 75, 577, 325, fill='#fc9803', r=50,tags="register")
        self.canvas.create_text(350, 100, text= "Register",fill="black",font=('Prompt 14 bold'),tags="register")
        self.canvas.create_line(133, 120, 577, 120, fill='white',tags="register")
        self.canvas.create_text(250, 155, text= "Username:",fill="black",font=('Prompt 12 bold'),tags="register")
        self.canvas.create_window(410,155,window=uname,width=200,height=30,tags="register")
        self.canvas.create_text(250, 200, text= "Email:",fill="black",font=('Prompt 12 bold'),tags="register")
        self.canvas.create_window(410,200,window=email,width=200,height=30,tags="register")
        self.canvas.create_text(250, 245, text= "Password:",fill="black",font=('Prompt 12 bold'),tags="register")
        self.canvas.create_window(410,245,window=pwd,width=200,height=30,tags="register")
        self.btn3.place(x=310,y=275)
        self.canvas.create_text(660, 390, text= "© Glenn_M",fill="white",font=('Prompt 9 bold'))
        self.canvas.pack()

    #After Login Successful
    def pass_window(self):
        self.clearCanvas()
        site = tk.Entry(self.canvas,textvariable=self.Site,font=("Arial", 10),justify='center')
        pwd = tk.Entry(self.canvas,textvariable=self.SitePassword,font=("Arial", 10),justify='center')
        self.canvas.create_text(180, 53, text= "App/Site:",fill="white",font=('Prompt 11 bold'),tags="register")
        self.canvas.create_window(340,53,window=site,width=200,height=30,tags="register")
        self.canvas.create_text(180, 93, text= "Password:",fill="white",font=('Prompt 11 bold'),tags="register")
        self.canvas.create_window(340,93,window=pwd,width=200,height=30,tags="register")
        addbtn = tk.Button(text='Update/Add',height=1,padx=10,font=("Arial", 10, "bold"),border=0,command=self.update_data)
        addbtn.place(x=460,y=40)
        delbtn = tk.Button(text=' Delete ',height=1,padx=10,font=("Arial", 10, "bold"),border=0,command=self.delete_data)
        delbtn.place(x=475,y=80)
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading',background='#fc9803')
        columns = ('#1', '#2')
        self.tree = ttk.Treeview(self.canvas, columns=columns, show='headings')
        self.tree.bind('<Double-1>', self.copy_password)
        self.tree.heading('#1', text='App/Site', anchor=CENTER)
        self.tree.heading('#2', text='Password', anchor=CENTER)
        self.loggedin = True
        self.get_data(self.Name.get(), self.Pwd.get())
        self.update_data()
        self.canvas.create_window(345,250,window=self.tree,width=600,height=215)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        self.canvas.create_window(655,250,window=scrollbar,height=215,width=20)
        self.canvas.create_text(660, 390, text= "© Glenn_M",fill="white",font=('Prompt 9 bold'))
        
        self.canvas.pack()

    #Curved Rectangle
    def curved_rectangle(self,x1, y1, x2, y2, r=25, **kwargs):    
        points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
        return self.canvas.create_polygon(points, **kwargs, smooth=True)
    
    #Add New Users to json file
    def add_user(self):
        if(self.Name.get() == ''):
            messagebox.showerror('Incomplete Credentials','Error: Username cannot be empty')
            return
        if(self.Email.get() == ''):
            messagebox.showerror('Incomplete Credentials','Error: Email cannot be empty')
            return
        if(self.Pwd.get() == ''):
            messagebox.showerror('Incomplete Credentials','Error: Password cannot be empty')
            return
        with open(os.path.join(DIRS[0], "users.json")) as f:
            file = json.load(f)
            if(self.Name.get() in file):
                messagebox.showerror('Incomplete Credentials','Error: Username is already taken')
                return
        dict = {self.Name.get() : {"Email":self.Email.get(),"Password":(hashlib.sha256(self.Pwd.get().encode())).hexdigest()}}
        create_json_file(DIRS[1], f'{self.Name.get()}.txt')

        #Encrypt file contents with user password
        with open(os.path.join(DIRS[1], f'{self.Name.get()}.txt'), "r+") as file:
            enc_data = Cryptography.encrypt(self.Pwd.get(), file.read())
            file.seek(0)
            file.write(enc_data)

        self.write_json(dict)
        self.main()

    #Fetch user data
    def get_data(self, username, password):
        with open(os.path.join(DIRS[1], f'{username}.txt'),'r') as file:
            enc_data = file.read()
            dec_data = Cryptography.decrypt(password, enc_data)
            try:
                self.user_data = json.loads(dec_data)
                return True
            except (ValueError, ):
                return False

    #Encrypt and save user data       
    def save_data(self):
        if self.loggedin:
            with open(os.path.join(DIRS[1], f'{self.Name.get()}.txt'),'w') as file:
                json_data = json.dumps(self.user_data)
                enc_data = Cryptography.encrypt(self.Pwd.get(), json_data)
                file.write(enc_data)
        self.destroy()

    #Authorise User
    def check(self):
        with open(os.path.join(DIRS[0], "users.json")) as f:
            file = json.load(f)
            if(self.Name.get() in file.keys()):
                if(hashlib.sha256(self.Pwd.get().encode()).hexdigest() == file[self.Name.get()]["Password"]):
                    self.pass_window()
                else:
                    messagebox.showerror("Incorrect Credentials","Error: Username and Password don't match")
            else:
                messagebox.showerror('Incorrect Credentials',f"No user found with Username : {self.Name.get()}")
        
    #Copy data to clipboard
    def copy_password(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            pc.copy(item['values'][1])
            messagebox.showinfo("Copied", f"Password for {item['values'][0]} copied")

    #Update table data
    def update_data(self):
        self.tree.delete(*self.tree.get_children())
        if(self.Site.get()!="" and self.SitePassword.get()!=""):
            self.user_data[self.Site.get()] = self.SitePassword.get()
            self.Site.set("")
            self.SitePassword.set("")
        for site in self.user_data.keys():
            detail = (site, self.user_data[site])
            self.tree.insert('', index='end', values=detail )

    #Delete table data
    def delete_data(self):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            del self.user_data[item['values'][0]]
            messagebox.showinfo("Deleted", f"{item['values'][0]} data deleted")
        self.update_data()

    #Add User to JSON file
    def write_json(self,new_data):
        with open(os.path.join(DIRS[0], "users.json"),'r+') as file:
            file_data = json.load(file)
            file_data.update(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
            file.close()

    #Clear Window
    def clearCanvas(self):
        try:
            self.canvas.delete("interface")
            self.canvas.delete("register")
            self.btn1.place_forget()
            self.btn2.place_forget()
            self.btn3.place_forget()
        finally:
            return

if(__name__ == '__main__'):
    init_directories()
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.save_data)
    app.mainloop()
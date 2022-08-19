#Dependencies
import os, sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import CENTER, END 
from tkinter.messagebox import showinfo
from Cryptography import *
import hashlib
import ctypes
import json

#Output higher res windows
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#Data Directories
DIRS = ["User", "Data", "Images"]

def init_directories():
    path_prefix = os.path.split(sys.argv[0])[0]
    if path_prefix != "":
        for indx, dir in enumerate(DIRS):
            DIRS[indx] = os.path.join(os.getcwd(), path_prefix, dir) 

    for dir in DIRS:
        if not os.path.exists(dir):
            os.makedirs(dir)

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

        #Icon
        icon = tk.PhotoImage(file=os.path.join(DIRS[2], "icon.png"))
        self.iconphoto(False,icon)

        #Background
        self.canvas = tk.Canvas(self,width=710,height=400,borderwidth=0)
        self.background = tk.PhotoImage(file=os.path.join(DIRS[2], "home.png"))
        self.canvas.create_image(0,0,anchor='nw',image=self.background)

        #Create User Password file if doesn't exist
        if not os.path.exists(os.path.join(DIRS[0], "users.json")):
            with open(os.path.join(DIRS[0], "users.json"), 'w') as file:
                json.dump({},file)
        
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
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview.Heading',background='#fc9803')
        columns = ('#1', '#2')
        tree = ttk.Treeview(self.canvas, columns=columns, show='headings')
        tree.heading('#1', text='App/Site', anchor=CENTER)
        tree.heading('#2', text='Password', anchor=CENTER)
        details = []
        for n in range(1, 100):
            details.append((f'first {n}', f'last {n}'))
        for detail in details:
            tree.insert('', index='end', values= tuple(detail))
        self.canvas.create_window(345,250,window=tree,width=600,height=215)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        self.canvas.create_window(655,250,window=scrollbar,height=215,width=20)
        self.canvas.create_text(660, 390, text= "© Glenn_M",fill="white",font=('Prompt 9 bold'))

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
        self.write_json(dict)
        self.main()

    #Fetch user data
    def get_data(Username, data, filename=os.path.join(DIRS[0], "users.json")):
        details = ''
        with open(filename,'r') as file:
            file_data = json.load(file)
            details = file_data[Username]["temp"]

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
    app.mainloop()
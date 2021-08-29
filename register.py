#Dependencies
from tkinter import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

#App Creation
app = Tk()
app.geometry('710x400')
app.resizable(0,0)
app.title('Password_M Register') 

#Variables
Name = StringVar()
Pwd = StringVar()
Email = StringVar()


#Icon
image = PhotoImage(file="images/icon.png")
app.iconphoto(False,image)

#Background
BG = Canvas(app,width=710,height=400,borderwidth=0)
bg = PhotoImage(file="images/home.png")
BG.create_image(0,0,anchor=NW,image=bg)

def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):    
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return BG.create_polygon(points, **kwargs, smooth=True)

#Wigits
round_rectangle(133, 75, 577, 325, fill='#fc9803', r=50)
BG.create_text(350, 100, text= "Register",fill="black",font=('Prompt 14 bold'))
BG.create_line(133, 120, 577, 120, fill='white')
BG.create_text(250, 155, text= "Username:",fill="black",font=('Prompt 12 bold'))
uname = Entry(BG,textvariable=Name,font=("Arial", 10),justify='center').place(x=310,y=140,width=200,height=30)

BG.create_text(250, 200, text= "Email:",fill="black",font=('Prompt 12 bold'))
email = Entry(BG,textvariable=Email,font=("Arial", 10),justify='center').place(x=310,y=185,width=200,height=30)

BG.create_text(250, 245, text= "Password:",fill="black",font=('Prompt 12 bold'))
pwd = Entry(BG,textvariable=Pwd,font=("Arial", 10),justify='center').place(x=310,y=230,width=200,height=30)

Button(text='Sign Up',padx=10,font=("Arial", 10, "bold"),border=0,command='').place(x=310,y=275)
BG.create_text(660, 390, text= "© Glenn_M",fill="white",font=('Prompt 9 bold'))
BG.pack()

#Apploop
app.mainloop()
from tkinter import *

from numpy import sign

primary_color = "#2E86AB"
background_color = "#080808"

home_window = Tk()

def signup():
    home_window.destroy()
    signup_window = Tk()
    signup_window.geometry("1280x720")
    signup_window.title("Uni=Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    signup_window.iconphoto(True,icon)
    signup_window.config(background=background_color)

def home():
    home_window.geometry("1280x720")
    home_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    home_window.iconphoto(True,icon)
    home_window.config(background=background_color)

    title = Label(home_window,text="Uni-Pass",font=("Comic Sans",100,"bold"),fg=primary_color,bg=background_color)
    title.place(x=360,y=140)

    subtitle = Label(home_window,text="~The only password you'll need",font=("Comic Sans",20,"bold"),fg=primary_color,bg=background_color)
    subtitle.place(x=560,y=300)

    signup_button = Button(home_window,command=signup,text="Sign-Up",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    signup_button.place(x=460,y=400)

    login_button = Button(home_window,text="Login",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    login_button.place(x=760,y=400)

    home_window.mainloop()

home()
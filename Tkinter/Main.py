from tkinter import *
from tkinter import filedialog

primary_color = "#2E86AB"
background_color = "#080808"

home_window = Tk()

def signup():
    home_window.destroy()
    signup_window = Tk()
    signup_window.geometry("1280x720")
    signup_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    signup_window.iconphoto(True,icon)
    signup_window.config(background=background_color)

    usernametk = Label(signup_window,text="Choose your username",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    usernametk.place(relx=0.5,y=80,anchor = CENTER)

    username_entry = Entry(signup_window,width=20,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)   
    username_entry.place(relx=0.5,y=160,anchor = CENTER)

    passwordtk = Label(signup_window,text="Enter your password",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    passwordtk.place(relx=0.5,y=280,anchor = CENTER)

    password_entry = Entry(signup_window,width=20,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')   
    password_entry.place(relx=0.5,y=360,anchor = CENTER)

    path = None
    def get_path():
        global path
        path = filedialog.askdirectory()

    pathtk = Label(signup_window,text="Enter the path to store your key",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    pathtk.place(relx=0.5,y=480,anchor = CENTER)
    
    path_entry = Entry(signup_window,width=20,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)
    path_entry.place(relx=0.5,y=560,anchor = CENTER)

    browse_button = Button(signup_window,text="Browse",command=get_path,font=("Comic Sans",10,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    browse_button.place(relx=0.65,y=560,anchor = CENTER)

    def button_click():
        global path
        username = username_entry.get()
        print(username)
        password = password_entry.get()
        print(password)
        # path = path_entry.get()
    enter_button = Button(signup_window,command=button_click,text="Submit",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    enter_button.place(relx=0.5,y=680,anchor = CENTER)

def home():
    home_window.geometry("1280x720")
    home_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    home_window.iconphoto(True,icon)
    home_window.config(background=background_color)

    title = Label(home_window,text="Uni-Pass",font=("Comic Sans",100,"bold"),fg=primary_color,bg=background_color)
    title.place(relx=0.5,y=240,anchor = CENTER)

    subtitle = Label(home_window,text="~The only password you'll need",font=("Comic Sans",20,"bold"),fg=primary_color,bg=background_color)
    subtitle.place(relx=0.7,y=340,anchor = CENTER)

    signup_button = Button(home_window,command=signup,text="Sign-Up",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    signup_button.place(relx=0.35,y=450,anchor = CENTER)

    login_button = Button(home_window,text="Login",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    login_button.place(relx=0.65,y=450,anchor = CENTER)

    home_window.mainloop()

home()
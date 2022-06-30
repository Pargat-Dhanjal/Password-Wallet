from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
import main

obj = main.PasswordWallet()

primary_color = "#2E86AB"
background_color = "#080808"

final_username = None

counter = 0

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

    username_entry = Entry(signup_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)   
    username_entry.place(relx=0.5,y=160,anchor = CENTER)

    passwordtk = Label(signup_window,text="Enter your password",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    passwordtk.place(relx=0.5,y=280,anchor = CENTER)

    password_entry = Entry(signup_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')   
    password_entry.place(relx=0.5,y=360,anchor = CENTER)

    path = None
    def get_path():
        global path
        path = filedialog.askdirectory()

    pathtk = Label(signup_window,text="Enter the path to store your key",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    pathtk.place(relx=0.5,y=480,anchor = CENTER)
    
    path_entry = Entry(signup_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)
    path_entry.place(relx=0.5,y=560,anchor = CENTER)

    browse_button = Button(signup_window,text="Browse",command=get_path,font=("Comic Sans",10,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    browse_button.place(relx=0.65,y=560,anchor = CENTER)

    def goback():
        signup_window.destroy()
        home()
    
    def button_click():
        global path
        username = username_entry.get()
        # print(username)
        password = password_entry.get()
        # print(password)
        path = path_entry.get()
        # print(path)
        obj.addUsr(username, password, path)
        obj.createPassFile(username)
        goback()

    enter_button = Button(signup_window,command=button_click,text="Submit",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    enter_button.place(relx=0.5,y=680,anchor = CENTER)

    back_button = Button(signup_window,command=goback,text="Back",font=("Comic Sans",15,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    back_button.place(relx=0.1,rely=0.1,anchor = CENTER)

def login():
    global login_window
    home_window.destroy()
    login_window = Tk()
    login_window.geometry("1280x720")
    login_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    login_window.iconphoto(True,icon)
    login_window.config(background=background_color)

    usernametk = Label(login_window,text="Enter your username",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    usernametk.place(relx=0.5,y=180,anchor = CENTER)

    username_entry = Entry(login_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)   
    username_entry.place(relx=0.5,y=260,anchor = CENTER)

    passwordtk = Label(login_window,text="Enter your password",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    passwordtk.place(relx=0.5,y=380,anchor = CENTER)

    password_entry = Entry(login_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')   
    password_entry.place(relx=0.5,y=460,anchor = CENTER)

    def goback():
        login_window.destroy()
        home()

    def checker():
        global final_username
        username = username_entry.get()
        password = password_entry.get()
        keypath = obj.loginUsr("usr/usrFile.txt", username, password)+".key"
        if(keypath == False):
                print("Wrong Username or Password")
        else:
            obj.loadKey(keypath)
            final_username = username
            login_window.destroy()
            user()
            # print("You are now Logged in!\n")

    enter_button = Button(login_window,command=checker,text="Submit",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    enter_button.place(relx=0.5,y=580,anchor = CENTER)

    back_button = Button(login_window,command=goback,text="Back",font=("Comic Sans",15,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    back_button.place(relx=0.1,rely=0.1,anchor = CENTER)

def saved_passwords():
    # obj.showPass()
    user_window.destroy()
    savedpass_window = Tk()
    savedpass_window.geometry("1280x720")
    savedpass_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    savedpass_window.iconphoto(True,icon)
    savedpass_window.config(background=background_color)

def user():
    global final_username
    global user_window
    global counter
    user_window = Tk()
    user_window.geometry("1280x720")
    user_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    user_window.iconphoto(True,icon)
    user_window.config(background=background_color)

    username_display = Label(user_window,text="Welcome "+final_username,font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    username_display.place(relx=0.5,y=80,anchor = CENTER)

    def goback():
        user_window.destroy()
        home()
    
    logout_button = Button(user_window,command=goback,text="logout",font=("Comic Sans",15,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    logout_button.place(relx=0.1,rely=0.1,anchor = CENTER)

    new_button = Button(user_window,command=new_password,text="store new password",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    new_button.place(relx=0.5,rely=0.25,anchor = CENTER)

    button = Button(user_window,command=saved_passwords,text="View saved Passwords",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    button.place(relx=0.5,rely=0.45,anchor = CENTER)

def new_password():
    global new_password
    user_window.destroy()
    newpass_window = Tk()
    newpass_window.geometry("1280x720")
    newpass_window.title("Uni-Pass")

    icon = PhotoImage(file=r'Assets\images\logo.png')
    newpass_window.iconphoto(True,icon)
    newpass_window.config(background=background_color)

    sitetk = Label(newpass_window,text="Enter site name",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    sitetk.place(relx=0.5,y=180,anchor = CENTER)

    site_entry = Entry(newpass_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)   
    site_entry.place(relx=0.5,y=280,anchor = CENTER)

    passtk = Label(newpass_window,text="Enter Password",font=("Comic Sans",30,"bold"),fg=primary_color,bg=background_color)
    passtk.place(relx=0.5,y=380,anchor = CENTER)

    pass_entry = Entry(newpass_window,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show="*")   
    pass_entry.place(relx=0.5,y=480,anchor = CENTER)
    
    def enter_new_pass():
        site = site_entry.get()
        password = pass_entry.get()
        obj.addPass(site,password)
        newpass_window.destroy()
        user()

    enter_button = Button(newpass_window,command=enter_new_pass,text="Submit",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    enter_button.place(relx=0.5,y=580,anchor = CENTER)

def home():
    global home_window
    home_window = Tk()
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

    login_button = Button(home_window,command=login,text="Login",font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
    login_button.place(relx=0.65,y=450,anchor = CENTER)

    home_window.mainloop()

home()
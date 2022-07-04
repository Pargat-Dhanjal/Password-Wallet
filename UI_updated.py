from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
from cv2 import destroyWindow
from main import PasswordWallet

obj = PasswordWallet()

primary_color = "#2E86AB"
background_color = "#080808"

class operations():
    def draw_window():
        global window_name
        window_name = Tk()
        window_name.geometry("1280x720")
        window_name.title("Uni-Pass")

        icon = PhotoImage(file=r'Assets\images\logo.png')
        window_name.iconphoto(True,icon)
        window_name.config(background=background_color)
    
    def destroy_window():
        window_name.destroy()
    
    def text(content,size,x,y):
        title = Label(window_name,text=content,font=("Arial",size,"bold"),fg=primary_color,bg=background_color)
        title.place(relx=x,rely=y,anchor = CENTER)

    def button(task,content,size,x,y):
        signup_button = Button(window_name,command=task,text=content,font=("Comic Sans",size,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
        signup_button.place(relx=x,rely=y,anchor = CENTER)

class Window:
    def home():
        operations.draw_window()
        operations.text("Uni-Pass",100,0.5,0.3)
        operations.text("~The only password you'll ever need",20,0.7,0.45)

        operations.button(Window.login,"Login",20,0.4,0.7)
        operations.button(Window.sign_up,"Sign-up",20,0.6,0.7)

        window_name.mainloop()
    
    def test():
        print("gg")
    
    def sign_up():
        operations.destroy_window()
        operations.draw_window()

        operations.text("Enter your username",30,0.5,0.2)
        username_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)
        username_entry.place(relx=0.5,rely=0.3,anchor = CENTER)
        operations.text("Enter your password",30,0.5,0.4)
        password_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')
        password_entry.place(relx=0.5,rely=0.5,anchor = CENTER)

        def get_path():
            path = filedialog.askdirectory()
        
        operations.text("Select key path",30,0.5,0.6)
        path_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')
        path_entry.place(relx=0.5,rely=0.7,anchor = CENTER)

        def enter_button():
            username = username_entry.get()
            password = password_entry.get()
            path = path_entry.get()
            obj.addUsr(username, password, path)
            obj.createPassFile(username)
            operations.destroy_window()
            Window.home()
        
        operations.button(get_path,"Browse",15,0.68,0.7)
        operations.button(lambda:[operations.destroy_window(),Window.home()],"Back",15,0.2,0.2)
        operations.button(enter_button,"Enter",20,0.5,0.8)
    

    def login():
        operations.destroy_window()
        operations.draw_window()

        operations.text("Enter your username",30,0.5,0.3)
        username_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)
        username_entry.place(relx=0.5,rely=0.4,anchor = CENTER)
        operations.text("Enter your password",30,0.5,0.6)
        password_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')
        password_entry.place(relx=0.5,rely=0.7,anchor = CENTER)
        def checker():
            global finalusername
            username = username_entry.get()
            password = password_entry.get()
            keypath = obj.loginUsr("usr/usrFile.txt", username, password)+".key"
            if(keypath == False):
                    print("Wrong Username or Password")
            else:
                obj.loadKey(keypath)
                obj.loadPassFile(username)
                finalusername = username
                operations.destroy_window()
                Window.user()
        operations.button(lambda:[operations.destroy_window(),Window.home()],"Back",15,0.2,0.2)
        operations.button(checker,"Enter",15,0.5,0.8)

    def user():
        operations.draw_window()
        operations.text("Welcome "+ str(finalusername),30,0.5,0.2)

        def logout():
            operations.destroy_window()
            Window.home()
        operations.button(logout,"logout",15,0.8,0.1)

        operations.button(Window.addpass,"Add a new password",15,0.5,0.3)
        operations.button(Window.viewsite,"View all passwords",15,0.5,0.4)
    
    def addpass():
        operations.destroy_window()
        operations.draw_window()

        operations.text("Enter Site Name",30,0.5,0.2)
        site_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)   
        site_entry.place(relx=0.5,rely=0.3,anchor = CENTER)
        operations.text("Enter Password",30,0.5,0.5)
        pass_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)   
        pass_entry.place(relx=0.5,rely=0.6,anchor = CENTER)

        operations.button(lambda:[operations.destroy_window(),Window.user()],"Back",15,0.2,0.2)

        def new_site():
            site = site_entry.get()
            password = pass_entry.get()
            obj.addPass(site,password)
            operations.destroy_window()
            Window.user()
        
        operations.button(new_site,"Enter",15,0.5,0.7)
    
    def viewsite():
        operations.destroy_window()
        operations.draw_window()
        
        sitelist = obj.showPass()
        operations.button(lambda:[operations.destroy_window(),Window.user()],"Back",15,0.1,0.1)

        for x in sitelist:
            Button(window_name,text=x,font=("Comic Sans",20,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0).place(relx=0.5,rely=[(sitelist.index(x)+1)/8],anchor = CENTER)
    
    def viewpass(name):
        operations.destroy_window()
        operations.draw_window()

        operations.button(lambda:[operations.destroy_window(),Window.user()],"Exit",15,0.5,0.6)

        password = obj.getPass(name)
        operations.text(password,30,0.5,0.5)
Window.home()
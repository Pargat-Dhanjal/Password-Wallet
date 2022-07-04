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
    
    def checker(username,password):
        global finalusername
        keypath = obj.loginUsr("usr/usrFile.txt", username, password)+".key"
        if(keypath == False):
                print("Wrong Username or Password")
        else:
            obj.loadKey(keypath)
            obj.loadPassFile(username)
            finalusername = username
            operations.destroy_window
            Window.home()
    
    def text(content,size,x,y):
        title = Label(window_name,text=content,font=("Arial",size,"bold"),fg=primary_color,bg=background_color)
        title.place(relx=x,rely=y,anchor = CENTER)

    def button(task,content,size,x,y):
        signup_button = Button(window_name,command=task,text=content,font=("Comic Sans",size,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0)
        signup_button.place(relx=x,rely=y,anchor = CENTER)

    def entry(size,x,y,show):
        if show == 0:
            entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*')
        else:
            entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1)
        
        entry.place(relx=x,rely=y,anchor = CENTER)
        
        print(entry.get())
        return entry.get()
class Window:
    def home():
        operations.draw_window()
        operations.text("Uni-Pass",100,0.5,0.3)
        operations.text("~The only password you'll ever need",20,0.7,0.45)

        operations.button(Window.login,"Login",20,0.4,0.7)
        operations.button(Window.login,"Sign-up",20,0.6,0.7)

        window_name.mainloop()
    
    def test():
        print("gg")
    
    def sign_up():
        operations.destroy_window()
        operations.draw_window()
    def login():
        operations.destroy_window()
        operations.draw_window()
        operations.text("Enter your username",30,0.5,0.3)
        username = operations.entry(20,0.5,0.4,1)
        operations.text("Enter your password",30,0.5,0.6)
        password = operations.entry(20,0.5,0.7,0)
        operations.button(lambda:[operations.destroy_window(),Window.home()],"Back",15,0.2,0.2)
        operations.button(lambda:[operations.destroy_window(),operations.checker(),Window.home()],"Enter",15,0.5,0.8)
    

Window.home()
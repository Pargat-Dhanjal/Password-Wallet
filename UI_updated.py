from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet
from main import PasswordWallet

obj = PasswordWallet() #Adding the password wallet-class from main.py

primary_color = "#2E86AB" # primary color (blue)
background_color = "#080808" #secondary (black)

class operations():
    def draw_window(): 
        global window_name
        window_name = Tk() #Creates a blank window
        window_name.geometry("1280x720") # Defined window geometry
        window_name.title("Uni-Pass") # Defined  window title

        icon = PhotoImage(file=r'Assets\images\logo.png') #imported window logo from its saved location
        window_name.iconphoto(True,icon) # added window logo 
        window_name.config(background=background_color) # set the background color to the window
    
    def destroy_window():
        window_name.destroy() # destorys the current window
    
    def text(content,size,x,y):
        title = Label(window_name,text=content,font=("Arial",size,"bold"),fg=primary_color,bg=background_color) # addes a text widget
        title.place(relx=x,rely=y,anchor = CENTER) # places the text widget in place

    def button(task,content,size,x,y):
        signup_button = Button(window_name,command=task,text=content,font=("Comic Sans",size,"bold"),bg=primary_color,fg=background_color,activeforeground=primary_color,activebackground=background_color,borderwidth=0) # addes a button widget
        signup_button.place(relx=x,rely=y,anchor = CENTER) # places the button widget in place

class Window:
    def home(): # The main home function (gets called at the start)
        operations.draw_window()
        operations.text("Uni-Pass",100,0.5,0.3) # adds title
        operations.text("~The only password you'll ever need",20,0.7,0.45) # adds subtitle

        operations.button(Window.login,"Login",20,0.4,0.7) # login button
        operations.button(Window.sign_up,"Sign-up",20,0.6,0.7) # signup button

        window_name.mainloop() # mainloop for the code to run (v-imp)
    
    def sign_up():
        operations.destroy_window() # destroys the home window
        operations.draw_window() # draws a window for signup

        operations.text("Enter your username",30,0.5,0.2) # adds text
        username_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1) # adds entry widget
        username_entry.place(relx=0.5,rely=0.3,anchor = CENTER) # places entry widget
        operations.text("Enter your password",30,0.5,0.4) # adds text
        password_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*') # adds entry widget
        password_entry.place(relx=0.5,rely=0.5,anchor = CENTER) # places entry widget 

        def get_path():
            path = filedialog.askdirectory() # opens up file explorer to browse 
        
        operations.text("Select key path",30,0.5,0.6) # adds text
        path_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*') # adds entry widget 
        path_entry.place(relx=0.5,rely=0.7,anchor = CENTER) # places entry widget

        # IF ENTER BUTTON PRESSED
        def enter_button(): 
            username = username_entry.get() # gets the value entered in username entry
            password = password_entry.get() # gets the value entered in password entry
            path = path_entry.get() # gets the path entered 
            obj.addUsr(username, password, path) # creates a new user login
            obj.createPassFile(username) # Grenerates a password file name with format username.txt in usr/usrdata folder
            operations.destroy_window() # destroys the signup window 
            Window.home() # navigates back to home 
        
        operations.button(get_path,"Browse",15,0.68,0.7) # adds browse button
        #IF BACK BUTTON PRESSED
        operations.button(lambda:[operations.destroy_window(),Window.home()],"Back",15,0.2,0.2)
        operations.button(enter_button,"Enter",20,0.5,0.8) # adds enter button
    

    def login():
        operations.destroy_window() # destroys the home window 
        operations.draw_window() # draws the sign-up window

        operations.text("Enter your username",30,0.5,0.3) # adds text
        username_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1) # adds an entry widget 
        username_entry.place(relx=0.5,rely=0.4,anchor = CENTER) # places the entry widget
        operations.text("Enter your password",30,0.5,0.6) # adds text
        password_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1,show='*') #adds an entry widget
        password_entry.place(relx=0.5,rely=0.7,anchor = CENTER) # places the entry widget
        def checker():
            global finalusername
            username = username_entry.get() # gets the value entered in the username entry widget
            password = password_entry.get() # gets the value entered in the password entry widget
            keypath = obj.loginUsr("usr/usrFile.txt", username, password)+".key"  # Checks if the user exists or not. If yes then returns the location of keypath. Else returns False
            if(keypath == False):
                    print("Wrong Username or Password") # prints wrong username or password in the terminal 
            else:
                obj.loadKey(keypath) # Loads the key in program memory
                obj.loadPassFile(username) # Loads the password file in program memory
                finalusername = username # temorarily stores the username in a variable
                operations.destroy_window() # destorys the login window 
                Window.user() # takes the user the the user window
        # IF BACK BUTTON IS PRESSED 
        operations.button(lambda:[operations.destroy_window(),Window.home()],"Back",15,0.2,0.2)
        # IF ENTER BUTTON IS PRESSED 
        operations.button(checker,"Enter",15,0.5,0.8)

    def user():
        operations.draw_window() # Draws a new user window
        operations.text("Welcome "+ str(finalusername),30,0.5,0.2) # adds customized text

        def logout():
            operations.destroy_window() # destorys window
            Window.home() # takes you back to home 
        # IF LOGOUT BUTTON IS PRESSES
        operations.button(logout,"logout",15,0.8,0.1) # adds logout button

        operations.button(Window.addpass,"Add a new password",15,0.5,0.3) # adds , add a new password button
        operations.button(Window.viewsite,"View all passwords",15,0.5,0.4) # adds view password button
    
    def addpass():
        operations.destroy_window() # destroys the user window 
        operations.draw_window() # draws a new window

        operations.text("Enter Site Name",30,0.5,0.2) # adds text
        site_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1) # adds an entry widget
        site_entry.place(relx=0.5,rely=0.3,anchor = CENTER) # places the entry widget
        operations.text("Enter Password",30,0.5,0.5) # adds test
        pass_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1) # adds an entry widget
        pass_entry.place(relx=0.5,rely=0.6,anchor = CENTER) # places the entry widget

        operations.button(lambda:[operations.destroy_window(),Window.user()],"Back",15,0.2,0.2) # adds the back button

        def new_site():
            site = site_entry.get() # gets the value entered in site name 
            password = pass_entry.get() # gets the value entered in password
            obj.addPass(site,password) # adds new password to the username.txt file
            operations.destroy_window() # destroys the addpass window 
            Window.user() # navigates back to the user window
        
        operations.button(new_site,"Enter",15,0.5,0.7) # Adds the enter button
    
    def viewsite():
        operations.destroy_window() # destorys the user window 
        operations.draw_window() # creates a new blank window

        operations.text("Enter Site Name",30,0.5,0.2) # adds text
        site_entry = Entry(window_name,width=20,insertbackground=primary_color,font=("Comic Sans",20,"bold"),bg = background_color,fg = primary_color,borderwidth=1) # adds an entry widget
        site_entry.place(relx=0.5,rely=0.3,anchor = CENTER) # places the entry widget

        def viewpass():
            website = site_entry.get()
            operations.destroy_window() # destorys the viewsite window
            operations.draw_window() # draws a blank window

            operations.button(lambda:[operations.destroy_window(),Window.user()],"Exit",15,0.5,0.6) # adds the exit button

            password = obj.getPass(website) # returns the decrypted passwords of given site name
            operations.text(password,30,0.5,0.5) # adds the password text

        operations.button(viewpass,"Enter",15,0.5,0.4) # adds the enterbutton button
        
        sitelist = obj.showPass() # saves the saved passowrds in a list
        operations.button(lambda:[operations.destroy_window(),Window.user()],"Back",15,0.1,0.1) # adds the back button

        for x in sitelist:
            operations.text(x,15,0.5,[(sitelist.index(x)+4)/8]) # adds a button for each element in the sitelist one below the other
Window.home()
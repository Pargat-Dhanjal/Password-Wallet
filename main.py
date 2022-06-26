from cryptography.fernet import Fernet


class PasswordWallet:
    def __init__(self):
        self.key = None
        self.usrFile = "usr/usrFile.txt"  # Location where users are stored
        self.usrDic = {}
        self.passFile = None
        self.passDict = {}
        # local encryption key to encrypt users
        self.localkey = open("usr/users.key", "rb").read()

    def loadKey(self, keypath):
        fp = open(keypath, "rb")
        self.key = fp.read()
        fp.close()

    def addUsr(self, usrname, password, keypath):
        # Generating and Creating a unique key
        self.key = Fernet.generate_key()
        fp = open(keypath+".key", "wb")
        fp.write(self.key)
        fp.close()
        # Creating a new user login
        self.usrDic[usrname] = keypath
        if self.usrFile is not None:
            fp = open(self.usrFile, 'a+')
            epass = Fernet(self.localkey).encrypt(password.encode())
            ekeypath = Fernet(self.localkey).encrypt(keypath.encode())
            fp.write(usrname+": "+epass.decode()+": "+ekeypath.decode()+"\n")

    def loginUsr(self, usrpath, username, userpass):
        self.usrFile = usrpath
        fp = open(usrpath, 'r')
        for line in fp:
            usrname, epass, ekeypath = line.split(": ")
            dpass = Fernet(self.localkey).decrypt(epass.encode()).decode()
            dkeypath = Fernet(self.localkey).decrypt(
                ekeypath.encode()).decode()
            if username == usrname and dpass == userpass:
                self.usrDic[usrname] = dkeypath
                return dkeypath
        return False

    def createPassFile(self, path, initial=None):
        self.passFile = "usr/usrdata/"+path+".txt"
        if initial is not None:
            for key, value in initial.items():
                self.addPass(key, value)

    def loadPassFile(self, path):
        self.passFile = "usr/usrdata/"+path+".txt"
        fp = open(self.passFile, 'r')
        for line in fp:
            site, encrypted = line.split(": ")
            self.passDict[site] = Fernet(self.key).decrypt(
                encrypted.encode()).decode()

    def addPass(self, site, password):
        self.passDict[site] = password
        if self.passFile is not None:
            fp = open(self.passFile, 'a+')
            encrypted = Fernet(self.key).encrypt(password.encode())
            fp.write(site+": "+encrypted.decode()+"\n")

    def getPass(self, site):
        return self.passDict[site]
    
    def showPass(self):
        for i in self.passDict.keys():
            print(i)

def seprator():
    print("\n#########################\n")

def viewPass(obj):
    cond = True
    while cond:
        print("""Select an Option
          (1) Store a New Password
          (2) View Existing Passwords
          (b) Go Back""")
        seprator()
        n = input("Enter choice here: ")
        seprator()
        if n == "1":
            seprator()
            site = input("Enter Site Name: ")
            password = input("Enter password: ")
            seprator()
            obj.addPass(site, password)
            seprator()
        elif n == "2":
            seprator()
            obj.showPass()
            seprator()
            site = input("Enter site name to  get password: ")
            seprator()
            print("Password:", obj.getPass(site))
            seprator()
        elif n == "b":
            cond = False
            seprator()
        else:
            print("Kindly enter a correct option only!")
            seprator()


def loadFiles(obj):
    cond = True
    while cond:
        print("""Select an Option
          (1) Create New Password File
          (2) Load Existing Password File
          (b) Go Back""")
        seprator()
        n = input("Enter choice here: ")
        seprator()

        if n == "1":
            path = input("Enter password file name: ")
            seprator()
            obj.createPassFile(path)
            print("Succesfully created a new Password file!")
            seprator()
            viewPass(obj)

        elif n == "2":
            path = input("Enter a file name to load: ")
            seprator()
            obj.loadPassFile(path)
            print("Succesfully loaded the password file!")
            viewPass(obj)

        elif n == "b":
            cond = False
            seprator()

        else:
            print("Kindly enter a correct option only!")
            seprator()


def main():
    obj = PasswordWallet()
    cond = True
    while cond:
        print("""Select an Option
        (1) Add a new User
        (2) Login to an existing User
        (e) Exit""")
        seprator()
        n = input("Enter choice here: ")
        seprator()

        if n == "1":
            usrname = input("Enter username: ")
            password = input("Enter Password: ")
            keypath = input("Enter a secure key path to store key: ")
            seprator()
            # obj.createKey(keypath)
            obj.addUsr(usrname, password, keypath)
            print("Succesfully Created a new User!")
            seprator()

        elif n == "2":
            usrname = input("Enter username: ")
            password = input("Enter Password: ")
            keypath = obj.loginUsr("usr/usrFile.txt", usrname, password)+".key"
            if(keypath == False):
                print("Wrong Username or Password")
                seprator()
            else:
                obj.loadKey(keypath)
                print("You are now Logged in!\n")
                loadFiles(obj)
                seprator()

        elif n == "e":
            cond = False
            print("Buh Bye!")
            seprator()

        else:
            print("Kindly enter a correct option only!")
            seprator()


main()

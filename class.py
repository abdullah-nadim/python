class user:
    name =" "
    email = ""
    password= " "
    login= False

    def __init__(self, name , email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        email= input("Enter email ")
        password = input("Enter password ")

        if email == self.email and password == self.password:
            login= True
            print("Login Succesfull")

        else:
            print("Login Failed")

    def logout(self):
        login= False
        print("Logged out")

    def isloggedin(self):
        if self.login:
            return True
        else:
            return  False

    def profile(self):
        if self.isloggedin():
            print(self.name, '\n', self.email)
        else:
            print("user is not logged in")

user1= user("Nadim","nadim.111@gmail.com","123456")
user2= user('Adam', "adam.111@gmail.com", "123456")

user1.login()
user1.profile()
hello = input()


class user:
    name = " "
    email = " "
    password= " "
    DOT = " "
    gender = " "
    login = False

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email == self.email and password == self.password:
            login = True
            print("Login successfull ")

        else:
            login = False
            print("Login failed")

    def logout(self):
        login= False
        print("logged out")

    def isloggedin(self):
        if self.login:
            return True
        else:
            return  False

    def profile(self):
        if self.isloggedin():
            print(self.name ,'\n', self.DOT, '\n' , self.gender)

        else:
            print("User is not logged in.")


user1 = user()

user1.name= "Nure Alam Nadim"
user1.DOT = "8th Octobor"
user1.gender= "male"
user1.email= "nadim.soft.111@gmail.com"
user1.password= "12345678"

user1.login()
user1.profile()
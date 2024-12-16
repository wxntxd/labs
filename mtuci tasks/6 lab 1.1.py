class UserAccaaunt:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self,new_password):
        if new_password:
            self.password = new_password
        else:
            print("Enter smth")
    def check_password(self,password):
        if password:
             return self.password == password
user = UserAccaaunt("Amal", "amalmamedow80@gmail.com", 12345)
user.set_password("qwerty")
print(user.check_password(12345)) # first password
print(user.check_password("qwerty")) # new password
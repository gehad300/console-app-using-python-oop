import re
import sub_menue

class users:
 def __init__(self,first_name,last_name,email,password,phone_number):

     self.first_name=first_name
     self.last_name=last_name
     self.email=email
     self.password=password
     self.phone_number=phone_number

 @staticmethod
 def register():       
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    phone_regex = '^01[0-2,5]{1}[0-9]{8}$'
    first_name = str(input("please enter yout first name: \n"))
    while not first_name.isalpha():
        first_name = str(input("please enter a valid name: \n"))
    last_name = str(input("please enter your last name : \n"))
    while not last_name.isalpha():
        last_name = str(input("please enter a valid name : \n"))
    email = input("please enter your email : \n")
    file=open("users.txt",'r')
    for user in file:
        data_validation=user.split(":")
        while  email==data_validation[2]:
          print("==========================")  
          print("This email is already exists:")
          print("=============================")
          email=input("please enter your email")
    while not re.search(regex, email):
        email = input("please enter a valid email : \n")
    password = input("please enter a password : \n")
    while len(password) < 8:
        password = input("password must be more than 8 character \n")
    confirm_password = input("please re-type password : \n")
    while password != confirm_password:
        password = input("wrong password ")

    phone_number = input("please enter your phone number :")
    while not re.search(phone_regex, phone_number):
         print("invalid phone number")
         phone_number= input("enter your phone number: ")
    new_user = users(first_name,last_name,email,password,phone_number)
    new_user.store_data()

 def store_data(self):

      f = open("users.txt", "a")
      f.write(self.first_name+':'+self.last_name+':'+self.email+':'+self.password+':'+self.phone_number+'\n')
      f.close()

 def login(self):
      
    is_found=False
    self.email = input(" please Enter your email: ")
    self.password = input(" please Enter your password: ")
    try:
        users=open('users.txt','r')
        for user in users:
            user_data=user.split(":")
            if user_data[2]==self.email and user_data[3]==self.password:
                is_found=True
    except FileNotFoundError:
        print("file not found",FileNotFoundError)
        open("users.txt",'w')

    if is_found:
        print("successfully login")
        sub_menue.sub_menue(self.email)
    else:
        print( "========invalid login!========")



   
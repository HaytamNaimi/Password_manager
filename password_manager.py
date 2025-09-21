import json
import string
import random

def get_user_choice():
     print("------Welcome to password manager!--------\nMENU: \n1.Enter a new account or update existing one \n2.Retrieve existing account \n3.Exit ")
     try:
         choice = int(input("Enter your choice : "))
     except ValueError:
         choice= int(input("Please enter a valid choice : "))
     return choice

def get_password():
    while True:
     password_choice=int(input("---Do you want to?:---\n1.Enter your password manually\n2.Generate a random password\n your choice: "))
     if password_choice==1:
        account_password=input("Enter your password: ")
        return account_password

     elif password_choice==2:
         password_length=int(input("Enter your password length: "))
         char=string.ascii_letters+string.digits+string.punctuation
         account_password="".join(random.choice(char) for i in range(password_length))
         print("passsword generated successfully, your password is:", account_password)

         return account_password
     else:
         print("Invalid choice, please try again.")



def new_account():
    #get account infos
    account_name = input("Enter your account name: ").lower()
    account_username=input("Enter your account username: ")
    account_password=get_password()

    #creating a new the dict
    new_entry = {
      account_name:{
        "Username":account_username,
        "Password":account_password
      }
    }

    #opening json file and converting it into a dict
    try :
        with open("passwords.json","r") as f:
          data=json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
      data={}

    #updating data
    data.update(new_entry)

    #update the json file with the new data
    with open("passwords.json","w") as f:
        json.dump(data,f,indent=4)


def existing_account():
        retrieve=input("enter account name please:").lower()
        try:
            with open("passwords.json","r") as f:
                data=json.load(f)
        except json.JSONDecodeError:
            print("No account found.")
            return
        if retrieve in data :
          account_info=data[retrieve]
          print("Account found")
          print(f"Your account infos are :\n Username:{account_info['Username']}\n Password:{account_info['Password']}")
        else:
            print("No account found.")



def determine_choice(choice):
    if choice == 3:
        print("THANK YOU FOR USING PASSWORD MANAGER")
        return True
    elif choice == 1:
        new_account()
        print("Your account has been created successfully.")
    elif choice == 2:
        existing_account()
        return False


def main():
 print("------------------PASSWORD MANAGER---------------")
 while True:
  choice=get_user_choice()
  if determine_choice(choice): break

main()





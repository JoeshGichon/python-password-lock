from passwordLoker import User,Credentials

def create_user(o_name,u_name,p_word): 
    new_user = User(o_name,u_name,p_word)
    return new_user

def create_credentials(account,account_u_name,account_p_word): 
    new_credential = Credentials(account,account_u_name,account_p_word)
    return new_credential

def save_user_details(user): 
    user.save_user()
  
def save_credentials_details(credentials): 
    credentials.save_credentials()

def find_account(password_input):
    return User.find_by_password(password_input)
  
def find_credential(account_name_input):
    return Credentials.find_credential(account_name_input)

def delete_credential(to_delete): 
    return Credentials.delete_credential_account(to_delete)


def main(): 
    print("Hello there, Welcome to password Locker application")
    print("\n")

    while True:
        print("To create an account and or login to your account, use: cr - To create a new account, str - To store existing credentials, crn- To create new account credentials, displ - To display account credentials, delt - To delete credentials account, ext - To exit application")

        userInput = input().lower()

        if userInput == "cr": 
            print("\n")
            print("Account Creation")

            print("Enter Your Official Name: ")
            o_name = input()
            
            print("Enter Username: ")
            u_name = input()
            
            print("Enter Password:")
            p_word = input()
            print("Confirm password")
            test_password = input()

            if p_word == test_password: 
                print("\n")
                save_user_details(create_user(o_name,u_name,p_word))
                print(f"Congratulations {o_name}, For successfully creating an account.")
                print('\n')

            else: 
                print("Password miss match,Try again")
                print("\n")

        elif userInput == "str":
            try:
                print("\n")
                print(f"{o_name},store your existing accounts Details.") 
                
                print("Enter Account name:")
                acc_name = input()
                
                print("Enter Account username")
                acc_username = input()
                
                print("Enter Account password:")
                acc_password = input()

                print("\n")
                save_credentials_details(create_credentials(acc_name,acc_username,acc_password))
                print(f"Successfully saved details of your {acc_name} account.")
                print("\n")

            except UnboundLocalError: 
                message = print("First Create An Account")
                return message

        elif userInput == "crn":
            try:
                print("\n")
                print(f"Welcome back:") 
                print("Create new account credentials")
                print("\n")
                
                print("Enter account you wish to create:e.g twitter")
                new_account = input()
                
                print("Enter your username:")
                new_username = input()
                
                print("Would you like the application to generate a password for you?(Y/N)")
                user_preference = input().upper()
                if user_preference == "Y": 
                    new_password = f"0246{new_account}"
                    print("\n")
                    print(f"Your {new_account} password is: {new_password}")
                else: 
                    print("Enter password of your choice:")
                    new_password = input()
                    print("\n")
                    print(f"Your {new_account} password is: {new_password}")
                    
                print("\n")
                save_credentials_details(create_credentials(new_account,new_username,new_password))
                print(f"Successfully created your new {new_account} account credentials.")
                print("\n")
            except UnboundLocalError: 
                message = print("Create an account with us first.")
                return message

        elif userInput == "displ": 
            print("\n")
            print("Enter password to login and view account credentials:")
            password_input = input()
            if find_account(password_input): 
                print("Enter account type to view:")
                account_to_find = input()
                if find_credential(account_to_find): 
                    outcome = find_credential(account_to_find)
                    print("\n")
                    print("Account Details:")
                    print("-"*20)
                    print(f"Account name: {outcome.account}")
                    print(f"Username: {outcome.username}")
                    print(f"Password: {outcome.password}")
                    print("\n")
                else: 
                    print("No credential account found")
                    print("\n")
          
            else: 
                print("Incorrect password.")
                print("\n")

        elif userInput == "dlt": 
            print("\n")
            print("Enter account name to delete.e.g instagram")
            account_to_delete = input()
            if delete_credential(account_to_delete): 
                print("\n")
                print(f"Successfully deleted your {account_to_delete} account credential.")
                print("\n")
            else: 
                print("Cannot delete the credential account that you inputted.")
                print("\n")

        elif userInput == 'ext': 
            print("Thank you for using your application.")
            break
    
        else: 
            print("Unknown command,Enter the available input:")


if __name__ == '__main__': 
    main()



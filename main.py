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
        print("To create an account and or login to your account, use: cr - create a new account, str - store existing credentials, crn- create new account credentials, displ - display account credentials, delt - delete credentials account, ext - exit")

        nameInput = input().lower()

        if nameInput == "cr": 
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


if __name__ == '__main__': 
    main()



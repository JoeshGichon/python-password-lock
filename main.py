from passwordLoker import User,Credentials

def create_user(o_name,u_name,p_word): 
    new_user = User(o_name,u_name,p_word)
    return new_user

def create_credentials(account,account_u_name,account_p_word): 
    new_credential = Credentials(account,account_u_name,account_p_word)
    return new_credential



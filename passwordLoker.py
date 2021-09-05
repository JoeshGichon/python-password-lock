class User: 
  
  users_list = []
  
  def save_user(self): 
    
    User.users_list.append(self)
  
  @classmethod
  def find_by_password(cls,password_input): 
    
    for found in cls.users_list:
      if found.password == password_input:
        return found
  
  def __init__(self,o_name,u_name,p_word):
    
    self.official_name = o_name
    self.username = u_name
    self.password = p_word


class Credentials: 
  
  credentials_list = [] 
  
  def save_credentials(self): 
    
    Credentials.credentials_list.append(self)
    
  @classmethod
  def find_credential(cls,account_name_input): 
    
    for found in cls.credentials_list:
      if found.account == account_name_input:
        return found
  
  @classmethod
  def delete_credential_account(self,to_delete): 
    
    for indeletion in self.credentials_list:
      if indeletion.account == to_delete:
        return Credentials.credentials_list.remove(indeletion)
    
  
  def __init__(self,account,u_name,p_word):
    
    self.account = account
    self.username = u_name
    self.password = p_word


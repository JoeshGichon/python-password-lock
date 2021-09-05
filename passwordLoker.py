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



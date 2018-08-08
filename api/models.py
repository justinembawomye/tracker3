

class Requests:
   def __init__(self):
       self.client_name = client_name
       self.email = email
       self.request_title = request_title
       self.description = description
       self.department = department

    def __repr__(self):
        return "Requests: {}". format(self.request_title)
requests = []
    
class User:
   def __init__(self):
       self.name = name
       self.email = email
       self.username = username   
       self.password = password

    def __repr__(self):
        return f"User: {username}"
users = []    





from werkzeug.security import safe_str_cmp

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
users = [
    User(1, "shivam", '1234'),
    User(2, "amit", "12345")
]   
 
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    print(payload)
    return userid_table.get(user_id, None)




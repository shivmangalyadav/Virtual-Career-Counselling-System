"""
DAL: Database Abstraction Layer
"""

from .models import User

def user_signup(user: User) -> bool:
    pass

def user_signin(loginId: str, password: str) -> bool:
    pass

def get_user_info(systemUserId: int) -> User:
    print(User)
    return "nff"

def users_list() -> list:
    pass


name = get_user_info(1)
print(name)
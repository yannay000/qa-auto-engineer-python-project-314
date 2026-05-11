import random

def generate_user_params() -> tuple:
    user_number = random.randint(1, 1000000)
    email = f"test{user_number}@test.ru"
    first_name = f"first_name{user_number}"    
    last_name = f"last_name{user_number}"
    return email, first_name, last_name
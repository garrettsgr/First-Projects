import string
import random

def generate_password(length:  int = 14):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

password = generate_password()
print(f'Password is: {password}')

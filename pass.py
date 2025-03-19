import random
import string

pass_length = int(input("Enter the length of the password: "))


def gen_password(length):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    num = string.digits
    symbols = string.punctuation
    
    password = [
            random.choice(upper),
            random.choice(lower),
            random.choice(num),
            random.choice(symbols)
        ]

    todos = upper + lower + num + symbols
    
    for _ in range(length - 4):
        password.append(random.choice(todos))

    random.shuffle(password)
    return "".join(password)  

print(gen_password(pass_length))



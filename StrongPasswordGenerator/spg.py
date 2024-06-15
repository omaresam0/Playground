# Strong PW that contains digits, punctuations(,.), upper and lower case
# 100% of password chars: 60% letters (30% upper and lower case, 20% digits, 20% punctuations

import random
import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
dig = list(string.digits)
punc = list(string.punctuation)

pw_length = 10
pw_length = int(pw_length)

def shuffle(lower,upper,dig,punc):
    random.shuffle(upper)
    random.shuffle(lower)
    random.shuffle(dig)
    random.shuffle(punc)

shuffle(lower,upper,dig,punc)
letters = round(pw_length * (30/100))
DigPunc = round(pw_length * (20/100))

password = [] # Storing pw to be generated

for i in range(letters):
    password.append(upper[i]) # 3 letters from uppercase letters
    password.append(lower[i]) # 3 letters from lowercase letters

for i in range(DigPunc):
    password.append(dig[i])
    password.append(punc[i])

password = "".join(password[0:])

print(password)
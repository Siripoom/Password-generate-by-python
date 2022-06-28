#import module
from functools import update_wrapper
import random
import string
from unittest import result

print("Would you link to generate password?")
#input length of password
length = int(input("\n Enter your length password :"))
#or define length
length = 16
#define data
upper = string.ascii_uppercase
lower = string.ascii_lowercase
number = string.digits
symbols = string.punctuation

#combine
all = upper + lower + number + symbols

ran = random.sample(all,length)

password = "".join(ran)

print("Password:",password)
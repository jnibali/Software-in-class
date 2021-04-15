import string
import random

N = int(input("length: "))

res = ''.join(random.choices(string.ascii_letters+
string.digits, k=N))

print("Random password : ",res)


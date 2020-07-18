import random
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
pwdlen=16
pwd="".join(random.sample(s,pwdlen))
print(pwd)
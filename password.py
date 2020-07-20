import random
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
pwdlen=int(input("Enter the length of the password dynamically"))
pwd="".join(random.sample(s,pwdlen))
print(pwd)

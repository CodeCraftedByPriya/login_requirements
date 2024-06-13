p = input("Enter your password:")
l = 0
u = 0
d = 0
s = 0
if len(p) >= 8:
    print("Password is strong enough!")
    for i in p:
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
        if i.isdigit():
            d+=1
        if (i == '@' or i == '$' or i == '_' or i == '!'):
            s+=1

if (l>=1 and u>=1 and d>=1 and s>=1):
    print("Valid Password")
else:
    print("Invalid password, it should contain atleast one digit, capital letter, @, $, _, !")

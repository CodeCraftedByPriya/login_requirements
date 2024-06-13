import random
def generate_captcha(n):
    c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha = ""
    while (n):
        captcha += c[random.randint(1, 1000) % 62]
        n -= 1
    return captcha

def check_captcha(captcha,i):
    if captcha == i:
        print("Verified!")
        return(True)
    
captcha = generate_captcha(9)
print(captcha)        

p = input("Enter the CAPCHA:")
if (check_captcha(captcha,p)):
    print("CAPTCHA Matched")
else:
    print("CAPTCHA Not Matched")

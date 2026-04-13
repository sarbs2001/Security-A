def Analyzer(password):
    chars = list(password)
    
    length = 0
    uppercase_char = 0
    lowercase_char = 0

    for char in chars:
        length += 1
        if char.isupper():
            uppercase_char += 1
        if char.islower():
            lowercase_char += 1

    if length >= 8:
        print("Password length is good. OK")
    else:
        print("Password length is short: NOT RECOMMENDED")
    if uppercase_char > 0:
        print("Password has atleast one uppercase letter. OK")
    else: 
        print("Does not have atleast one uppercase letter. NOT RECOMMENDED")
    if lowercase_char > 0:
        print("Password has atleast one lowercase letter. OK")
    else:
        print("Does not have atleast one lowercase letter. NOT RECOMMENDED")
    

password = str(input("Enter the password here: (Password should be atleast 8 characters with atleast one uppercase, lowercase, number, and special character.)"))
Analyzer(password)
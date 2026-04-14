def Analyzer(password):
    chars = list(password)
    
    length = 0
    uppercase_char = 0
    lowercase_char = 0
    num = 0
    special = 0

    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    special_character = ("!", "@", "#", "$", "%", "&", "-", "_", "+", "<", ">", "?", "/", "~")

    for char in chars:
        length += 1
        if char.isupper():
            uppercase_char += 1
        if char.islower():
            lowercase_char += 1
        if char in numbers:
            num +=1
        if char in special_character:
            special += 1

    if length >= 8:
        print(f"Password is {length} characters: GOOD")
    else:
        print(f"Password length short by {8 - length} characters: NOT RECOMMENDED")
    if uppercase_char > 0:
        if uppercase_char > 1:
            print(f"Has {uppercase_char} uppercase letters: GOOD")
        else:
            print(f"Has {uppercase_char} uppercase letter: GOOD")
    else: 
        print(f"Has 0 uppercase letters: NOT RECOMMENDED")
    if lowercase_char > 0:
        if lowercase_char > 1:
            print(f"Has {lowercase_char} lowercase letters: GOOD")
        else:
            print(f"Has {lowercase_char} lowercase letter: GOOD")
    else:
        print("Has 0 lowercase letters: NOT RECOMMENDED")
    if num > 0:
        if num > 1:
            print(f"Has {num} numbers: GOOD")
        else:
            print(f"Has {num} number: GOOD")
    else: 
        print("Has 0 numbers: NOT RECOMMENDED")
    if special > 0:
        if special > 1:
            print(f"Has {special} special characters: GOOD")
        else:
            print(f"Has {special} special character: GOOD")
    else:
        print("Has 0 special characters: NOT RECOMMENDED")
    

password = str(input("Enter the password here: (Password should be atleast 8 characters with atleast one uppercase, lowercase, number, and special character.)"))
Analyzer(password)
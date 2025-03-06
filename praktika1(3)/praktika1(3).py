def indicate_passwords(passwords):
    right_passwords = []
    
    for password in passwords:
        if len(password) >= 8:
            print(password)
            has_digitl = False
            has_upperl = False
            
            for char in password:
                if char.isdigit():
                    has_digitl = True
                if char.isupper():
                    has_upperl = True
                
                if has_digitl and has_upperl:
                    right_passwords.append(password)
                    break
    
    return right_passwords

passwords = ["Qwerty112oooo", "wAord22kklkk", "8803330605", "praktika3"]
working_password = indicate_passwords(passwords)
print("Working password is:", working_password)
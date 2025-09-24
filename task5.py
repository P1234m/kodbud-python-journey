#Task 5: Password Strength Checker
'''Explanation:
•
Ask user to input a password
•
Check for:
o
Minimum length
o
At least 1 number, 1 special character, 1 uppercase letter
•
Print "Strong" or "Weak"
Learn: String manipulation and re (regex) module.'''

import re

def password_checker():
    password=input("Set password: ")

    #check the input password against provided rules and return whether "Weak" or "Strong"
    if len(password)<8:
        return "Weak"
    if not re.search(r"\d",password):
        return "Weak"
    if not re.search(r"[A-Z]",password):
        return "Weak"
    if not re.search(r"[!@#$^&*(),.%?\":{}|<>]",password):
        return "Weak"
    return "Strong"


#Call the function
while True: 
    strength=password_checker()
    if strength=="Strong":
        print("Password strength: Strong")
        break
    else :
        print("Password strength: Weak")
        print("Reset a strong password")
        
    

#password strength checker

score = 0
specialcharacters = ['$', '#', '@', '!', '*']
password = input("Input your password: ")

#check for numbers
numbers = any(char.isdigit() for char in password)
if numbers:
    numbers = True
    score = score+1
else:
    numbers = False
    score = score-1

#check password length
length = len(password)
if length <= 8:
    length = False
    score = score-1
else:
    length = True
    score = score+1

#check for special characters
special = any(char in specialcharacters for char in password)
if special:
    special = True
    score = score + 1
else:
    special = False
    score = score - 1

if score >= 2:
    print("Password strength: Strong")
elif score == 1:
    print("Password strength: Moderate")
    if special == False:
        print("Consider adding special characters for better strength.")
    if length == False:
        print("Consider increasing password length for better strength.")
    if numbers == False:
        print("Consider adding numbers for better strength.")
else:
    print("Password strength: Weak")
    if special == False:
        print("Consider adding special characters for better strength.")
    if length == False:
        print("Consider increasing password length for better strength.")
    if numbers == False:
        print("Consider adding numbers for better strength.")





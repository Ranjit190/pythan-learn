import random

print("Password generator:")
uppercaseChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercaseChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upAndLow = uppercaseChars+lowercaseChars
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '/\\/', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '~', '`']

enterCh = int(input("Enter number of character in your password:\n"))
enterNum = int(input("Enter number of number in your password:\n"))
EnterSpecialCh = int(input("Enter number of special character in  your password:\n"))
passwordList = []
for ch in range(0, enterCh+1):
    passwordList.append(random.choice(upAndLow))
for ch in range(0, enterNum+1):
    passwordList.append(str(random.choice(numbers)))
for ch in range(0, EnterSpecialCh+1):
    passwordList.append(random.choice(specialChars))
random.shuffle(passwordList)
password = ''
for st in passwordList:
    password = password+st
print(password)

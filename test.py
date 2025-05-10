# print("Hello"[1])
#
# print(type("12"))
# print(type(12))
# print(type(12.78999))
# print(type(True))
# name = input("Enter your name?\n")
# length = len(name)
# print(type(name))
# print(type(length))
# print("Enter string length is: "+str(length))
# print(3//2)
# print(4**2)
# print(3*3+3/3-3)
# score =2
# isMake = True
# print(f"Your score is {score}, and is it maked {isMake}")

print("Welcome to tip calculater!")
totalBill = input("What is the total bill? $")
tips = input("How much tips would you like to give? 10, 12 or 15?")
numberOfPeople = input("How many people to split the bill?")
tipsPercent = float(tips)/100
calculation = ((float(totalBill)*float(tipsPercent)) + float(totalBill)) / int(numberOfPeople)
print(f"Each person should to pay: ${round(calculation,2)}")
import random
word_list = ["Dog", "baboon","camel"]
random_word = random.choice(word_list)
print(random_word+'\n')
result = ""
correct_letter=[]
count = 6
while result !=random_word:
    latter = input("Enter letter: ")
    st = ""
    check = False
    for char in random_word:
        if char == latter:
            st = st + char
            correct_letter.append(char)
            check=True
        elif char in correct_letter:
            st = st + char
        else:
            st = st + "_"
    if check == False:
        count -=1
        print("You have "+str(count)+" live left.")
        if count == 0:
            print("You lose the Game")
            result = random_word
            break
    else:
        check = False

    print(st)
    result =st

if count !=0:
    print("Final: "+result)







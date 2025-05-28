print("Welcome to python Pizza Deliveries!!")
size = input("What your Pizza size do you want? S, M,L: ")
st=''
if size == 'S':
    st ='Add pepperoni for small Pizza? Y or N: '
elif size == 'M':
    st = 'Add pepperoni for medium Pizza? Y or N: '
else:
    st = 'Add pepperoni for large Pizza? Y or N: '
pepperoni = input(st)

extra_chees = input("Do you want to extra chees? Y or N: ")

calculate = 0
if size =='S':
    calculate= calculate+15
elif size == 'M':
    calculate = calculate + 20
else:
    calculate = calculate + 25


if pepperoni == 'Y' and size == 'S':
    calculate = calculate+2
elif pepperoni == 'Y' and size == 'M':
    calculate = calculate+3
elif pepperoni == 'Y' and size == 'L':
    calculate = calculate + 4

if extra_chees == 'Y':
    calculate+=1
print('Your final bill is '+str(calculate))
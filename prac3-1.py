import random

your_number = input("Please enter the integer number you guess it is :  (0 to 100)")
your_number = int(your_number)
system_number = random.randint(0,100)
while your_number != system_number:
    if your_number> system_number and your_number<=system_number*10:
        print("You guess high!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
    elif your_number> system_number*10:
        print("You guess too much high!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
    elif your_number < system_number and your_number>= system_number/10:
        print("You guess low!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
    elif your_number < system_number/10:
        print("You guess too much low!")
        your_number = input("Please enter another number you guess closer:")
        your_number = int(your_number)
if system_number == your_number:
    print("You guess correctly! Congratulations!")
print("The number is : "+str(system_number))

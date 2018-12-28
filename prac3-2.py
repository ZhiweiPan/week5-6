import random

print("There are 3 numbers, please Guess what it is.")
print("The clue I gave is:")
print("When I say:  \t                 It means:")
total_error = "Error"
right_number = "Only the number is correct"
correct = "Absolutely right"
print(total_error +"\t                         The 3 numbers are not in the mystical numbers")
print(right_number +"\t     The number is correct but the position is not")
print(correct + "\t             Numbers are right and positions are too")
print("Now there are 3 numbers, you have 10 chance to guess it.")
print()
print()
number = random.sample(range(1,10),3)

your_number = input("Please enter 3 different numbers together:")
while len(your_number)!= 3 or your_number[0]== your_number[1] or your_number[1] == your_number[2] or your_number[0] == your_number[2]:
    your_number = input("Error!! Please enter 3 different number:")

anser = []
for i in range(len(your_number)):
    if int(your_number[i]) == number[i]:
        anser.append(correct)

    elif int(your_number[i]) in number and int(your_number[i])!= number[i]:
      anser.append(right_number)
    elif int(your_number[i]) not in number:
      anser.append(total_error)
n = 0
while n < 10:
    if anser != [correct,correct,correct]:
        print(anser)
        your_number = input("You answer is not correct please reenter one:")
        while len(your_number) != 3 or your_number[0] == your_number[1] or your_number[1] == your_number[2] or \
                your_number[0] == your_number[2]:
            your_number = input("Error!! Please enter 3 different number:")
        anser = []
        for i in range(len(your_number)):
            if int(your_number[i]) == number[i]:
                anser.append(correct)

            elif int(your_number[i]) in number and int(your_number[i]) != number[i]:
                anser.append(right_number)
            elif int(your_number[i]) not in number:
                anser.append(total_error)
        n += 1
    else:

        print("Correct! Congratulations!")
        print(number)
        break
if n >= 10 :
    print("You are defeated. Sorry! The answer is :")
    print(anser)
print("Try again? (yes or no)")
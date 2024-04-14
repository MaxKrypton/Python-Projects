import random

random_number = random.randint(1,10)

my_number = 0

while my_number != random_number:
    
    my_number = int(input("What is the number you are thinking of? "))
    if my_number < random_number:
        print("The guess was too low")
    elif my_number > random_number:
        print("The guess was too high")
print(f"your have guessed the number {random_number}")
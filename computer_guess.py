import random
guess = random.randint(1, 10)

my_response = " "

while my_response != "correct":
    if my_response == "low":
         print(f"My number was {guess}, is it the number you were lookiing for?")
         my_response = input("Write your answer in here: ")
         guess += 1
         print(f"Is this the number you were looking for {guess}")
print("Well Done!")

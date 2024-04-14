import re

email = input("What is your email? ")

if re.search(r"^\w+@\w+\.(com|org|net|edu)$", email, re.IGNORECASE):
    print ("Valid")
else:
    print("Invalid")
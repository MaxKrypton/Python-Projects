with open("name.csv", "r") as file:
    for line in file:
        Name, Location = line.rstrip().split(",")
        print(f"{Name} is from {Location}")
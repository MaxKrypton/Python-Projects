def main():
    print("Welcome to McQuint Calculator")
    
    name = input("What is Your Name? ").strip().title()
    
    print("...............")
    
    print(f"Your name is {name}, You have a wonderful name")

    print("-----------------------------------")
    while True:
        print(f"What is the operation you would like to do, {name}?\n 1. Addtion \n 2. Substration\n 3. Multiplication\n 4. Division")
        # Defining Operation Functions
        def addition(n,m):
            return n + m

        def substraction(n,m):
            return n - m

        def multiplication(n,m):
            return n * m

        def division(n,m):
            return n / m

        print("------------------------")

        try:
            choice = int(input("> Choose [1/2/3/4] "))
            
            # Addittion Operation

            if choice == 1:
                print("Welcome to the addition operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = addition(x,y)
                
                print(f"The Sum of {x} and {y} is {answer:,}")
                
            # Substraction Operation
            
            elif choice == 2:
                print("Welcome to the substration operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = substraction(x,y)
                
                print(f"The Substraction of {x} and {y} is {answer:,}")
                
            # Multiplication Operation
                
            elif choice == 3:
                print("Welcome to the multiplication operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = multiplication(x,y)
                
                print(f"The Multiplication of {x} and {y} is {answer:,}")
                
            # Division Operation

            elif choice == 4:
                print("Welcome to the division operation\n")
                
                x = int(input("What is your first number? "))
                print("...........")
                y = int(input("What is your second number? "))
                print("...........")
                answer = division(x,y)
                
                print(f"The Divion of {x} and {y} is {answer:,}")
            else:
                print('..............')
                print("ERROR:Please Enter a number between 1 and 4")

        except ValueError:
            print("...............")
            print("Wrong Input: Enter a Valid Number")
            
            
if __name__=="__main__":
    main()
        
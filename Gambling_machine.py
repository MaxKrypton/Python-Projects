MAX_LINES = 3
MAX_AMOUNT = 100
MIN_AMOUNT = 1
def deposit():
    
    while True:
        money = input("What is your deposit: ")
        if money.isdigit():
            money = int(money)
            if money > 0:
                break
            else:
             print("The number should be higher than 0")
        else:
            print("Please Enter a Valid Number...")
    return money

def get_number_of_lines():
    while True:
        line = input("Choose a number of line betwee 1 - " + str(MAX_LINES) + "? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
             print("The lines should be between 1 and 3")
        else:
            print("Please Enter a Valid Number...")
    return line

def get_bet():
    
    while True:
        money = input("What is your bet: ")
        if money.isdigit():
            money = int(money)
            if MIN_AMOUNT <= money <= MAX_AMOUNT:
                break
            else:
             print(f"The number should be between {MIN_AMOUNT} - {MAX_AMOUNT}")
        else:
            print("Please Enter a Valid Number...")
    return money

def main():
 balance = deposit()
 lines = get_number_of_lines()
 bets = get_bet()
 print(lines)
 print(balance)
 print(bets)

main()
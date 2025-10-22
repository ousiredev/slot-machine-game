# Python Slot Machine Game
import random

def bet(balance):
    bet_amount = int(input(f"Your balance: ${balance}\nEnter a bet: $"))
    if bet_amount <= balance:
        balance -= bet_amount
        return bet_amount, balance
    else:
        print("Not enough funds. Try again")
        return 0, balance

def spin_reels():
    symbols = ['🍒', '🍋', '🔔', '💎', '🍀']
    result = [random.choice(symbols) for _ in range(3)]
    return result

def check_win(result):
    if result[0] == result[1] == result[2]:
        return True
    return False

def main():
    balance = int(input("How much money do you have ?: $"))
    while balance > 0:
        bet_amount, balance = bet(balance)

        if bet_amount == 0:
            continue

        print("Spinning the reels... 🎰")

        result = spin_reels()
        print(" | ".join(result))

        if check_win(result):
            balance = balance + bet_amount * 2
            print(f"JACKPOT 🎉")
            
        else:
            print("No win. Try again!")
        
        if balance <= 0:
            print("Game over! You're out of funds")
            break
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

    print(f"Your new balance is: ${balance}")

        

if __name__ == '__main__':
    main()


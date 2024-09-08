import random

class LotteryGame:
    def __init__(self):
        self.coins = 1000
        print("Welcome to the Lottery Game!")
        print(f"You start with {self.coins} coins.")
        
    def play_lottery(self):
        if self.coins < 5:
            print("Not enough coins to play. Game over!")
            return False
        
        # Deduct 5 coins for playing
        self.coins -= 5
        
        # Player inputs their number
        try:
            player_number = int(input("Enter a number between 1 and 1000: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return True

        if player_number < 1 or player_number > 1000:
            print("Number out of range. Please enter a number between 1 and 1000.")
            return True

        # Randomly generate a number
        winning_number = random.randint(1, 1000)

        # Check if the player wins
        if player_number == winning_number:
            self.coins += 1000
            print(f"Congratulations! You guessed the correct number {winning_number} and won $1000!")
        else:
            print(f"Sorry, the winning number was {winning_number}. Better luck next time!")
        
        print(f"Remaining coins: {self.coins}")
        return True

    def start_game(self):
        while True:
            print("\nPress 'L' to play the lottery, or 'Q' to quit the game.")
            user_input = input("Your choice: ").strip().upper()
            
            if user_input == 'L':
                if not self.play_lottery():
                    break
            elif user_input == 'Q':
                print(f"You ended the game with {self.coins} coins. Thanks for playing!")
                break
            else:
                print("Invalid choice. Please press 'L' to play or 'Q' to quit.")

if __name__ == "__main__":
    game = LotteryGame()
    game.start_game()

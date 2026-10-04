import random
from enum import Enum
from typing import Optional

# 1. ENUMS FOR TYPE SAFETY
# This prevents typos like typing "scisor" instead of "scissor" anywhere in the code.
class Move(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3

class GameResult(Enum):
    WIN = "You Win!"
    LOSS = "Computer Wins!"
    DRAW = "Game Draw!"

# 2. SCALABLE GAME ENGINE
class RockPaperScissors:
    # Defining winning rules here makes it infinitely scalable. 
    # Want to add "Lizard" and "Spock"? Just update this dictionary.
    WIN_RULES = {
        Move.ROCK: [Move.SCISSORS],
        Move.SCISSORS: [Move.PAPER],
        Move.PAPER: [Move.ROCK]
    }

    def __init__(self, max_rounds: int = 5):
        self.max_rounds = max_rounds
        self.user_score = 0
        self.computer_score = 0

    def play_round(self, user_move: Move) -> GameResult:
        """Processes a single round, updates scores, and returns the result."""
        computer_move = random.choice(list(Move))
        
        print(f"\n> Your Choice: {user_move.name}")
        print(f"> Computer Choice: {computer_move.name}")

        if user_move == computer_move:
            self.user_score += 1
            self.computer_score += 1
            return GameResult.DRAW
            
        elif computer_move in self.WIN_RULES[user_move]:
            self.user_score += 1
            return GameResult.WIN
            
        else:
            self.computer_score += 1
            return GameResult.LOSS

    def display_final_score(self):
        """Calculates and prints the final outcome of the match."""
        print("\n" + "="*30)
        if self.user_score == self.computer_score:
            print(" FINAL RESULT: GAME DRAW")
        elif self.user_score > self.computer_score:
            print(" FINAL RESULT: YOU WIN THE SERIES!")
        else:
            print(" FINAL RESULT: COMPUTER WINS THE SERIES!")
        
        print(f" Your Score: {self.user_score}")
        print(f" Computer Score: {self.computer_score}")
        print("="*30 + "\n")


# 3. ROBUST UI CONTROLLER
def get_valid_int(prompt: str, valid_options: list[int]) -> int:
    """Safely gets integer input from the user without crashing."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            print("❌ Invalid selection. Please choose a valid number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number, not text.")

def main():
    while True:
        print("\n--- ROCK, PAPER, SCISSORS ---")
        start_choice = get_valid_int("1. Start Game\n2. Exit\nChoose an option: ", [1, 2])
        
        if start_choice == 2:
            print("Thanks for playing! Goodbye.")
            break

        # Initialize a new game instance for each full match
        game = RockPaperScissors(max_rounds=5)
        
        for round_num in range(1, game.max_rounds + 1):
            print(f"\n--- ROUND {round_num} ---")
            move_choice = get_valid_int(
                "1. Rock\n2. Scissors\n3. Paper\nYour move: ", 
                [1, 2, 3]
            )
            
            # Convert user integer input to Enum
            user_move = Move(move_choice)
            
            # Play round and get result
            result = game.play_round(user_move)
            print(f"Result: {result.value}")

        game.display_final_score()

if __name__ == "__main__":
    main()
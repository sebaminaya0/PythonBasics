import random

class Game:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.tie = 0

    def play(self):
        while True:
            player = self.get_player_choice()
            computer = self.get_computer_choice()
            self.print_choices(player, computer)
            result = self.get_result(player, computer)
            self.print_result(result)
            self.update_scores(result)
            self.print_scores()
            if self.is_game_over():
                break

    def get_player_choice(self):
        return input("Please choose rock, paper or scissor: ").lower()

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissor"])

    def print_choices(self, player, computer):
        print(f"Player: {player.capitalize()}.")
        print(f"Computer: {computer.capitalize()}.")

    def get_result(self, player, computer):
        if player == computer:
            return "tie"
        elif (player == "rock" and computer == "scissor") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissor" and computer == "paper"):
            return "player"
        else:
            return "computer"

    def print_result(self, result):
        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("Player wins!")
        else:
            print("Computer wins!")

    def update_scores(self, result):
        if result == "tie":
            self.tie += 1
        elif result == "player":
            self.player_score += 1
        else:
            self.computer_score += 1

    def print_scores(self):
        print(f"Player wins: {self.player_score}.")
        print(f"Computer wins: {self.computer_score}.")
        print(f"Tie: {self.tie}.")

    def is_game_over(self):
        if self.player_score == 3:
            print("Player wins the game!")
            return True
        elif self.computer_score == 3:
            print("Computer wins the game!")
            return True
        else:
            return False

if __name__ == "__main__":
    game = Game()
    game.play()


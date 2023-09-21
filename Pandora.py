import random

class PandoraGame:
    def __init__(self):
        self.player_name = ""
        self.location = "Start"
        self.game_over = False

    def start_game(self):
        print("Welcome to ProjectPandora!")
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}! Your journey begins in the land of Pandora.")
        self.play()

    def play(self):
        while not self.game_over:
            self.explore_location()
            if self.location == "Exit":
                self.game_over = True
            else:
                self.choose_action()

        print("Congratulations! You've completed your journey in Pandora.")

    def explore_location(self):
        if self.location == "Start":
            print("You find yourself at the entrance of a mysterious forest.")
            print("There are two paths ahead: one leads to a dark cave, and the other to a hidden garden.")
        elif self.location == "Cave":
            print("You enter the dark cave and find a treasure chest.")
            print("Do you want to (1) open it or (2) leave it and go back?")
        elif self.location == "Garden":
            print("You enter the hidden garden and see a strange flower.")
            print("Do you want to (1) touch it or (2) leave it and go back?")
        elif self.location == "Exit":
            print("You have successfully completed your journey!")

    def choose_action(self):
        choice = input("Enter your choice (1 or 2): ")
        if self.location == "Start":
            if choice == "1":
                self.location = "Cave"
            elif choice == "2":
                self.location = "Garden"
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif self.location == "Cave":
            if choice == "1":
                print("You found a magical gem! Your journey continues...")
                self.location = "Start"
            elif choice == "2":
                self.location = "Start"
            else:
                print("Invalid choice. Please enter 1 or 2.")
        elif self.location == "Garden":
            if choice == "1":
                print("The flower grants you a special power! Your journey continues...")
                self.location = "Start"
            elif choice == "2":
                self.location = "Start"
            else:
                print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    game = PandoraGame()
    game.start_game()

# 815805
# 816000
# 815028

# SortQuest: Sorting Game
# This is a simple console-based sorting game where the player sorts a list of items.
# The game progresses through levels of increasing difficulty.

import random
import time
import os


class Sorter:
    """Class containing sorting algorithms."""

    def seletionSort(array):
        """Sorts an array using the selection sort algorithm."""
        size = len(array)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            # Swap the found minimum element with the first element
            array[i], array[min_index] = array[min_index], array[i]
        return array


class Utils:
    """Utility class containing utility functions."""

    def clear_screen():
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')


class Level:
    """Represents a level in the game."""

    def __init__(self, difficulty):
        """Initializes the level with a difficulty that determines the number of items to sort."""
        self.difficulty = difficulty
        self.items = self.generate_items()

    def generate_items(self):
        """Generates a list of random items based on the difficulty level."""
        return [random.randint(1, 100) for _ in range(self.difficulty)]

    def play(self):
        """Executes the gameplay for the level."""
        print("Current items to sort: ", end="")
        print(self.items)

        sorted_items = Sorter.seletionSort(
            self.items[:])  # Make a copy to sort
        start_time = time.time()
        user_input = input("Enter the sorted items separated by spaces: ")
        duration = time.time() - start_time

        try:
            user_sorted = list(map(int, user_input.strip().split()))
        except:
            print("Wrong Input! ", end="")
            return "retry", 0

        score = 0
        if user_sorted == sorted_items:
            score = 50

            if duration < 10:
                print(
                    f"\nExcellent Work, You completed challenge just in {duration:.2f} seconds.")
                score = 100
            elif duration > 30:
                print(f"\nYou took way too much time. {duration:.2f} seconds.")
                return "fail", 0
            else:
                print(
                    f"\nGood, You completed challenge in {duration:.2f} seconds.")
            return "pass", score
        else:
            print("\nThat's not quite right. Here's the correct order:", end="")
            print(sorted_items)
            return "fail", 0


class Game:
    """Main game class."""

    def __init__(self):
        """Initializes the game with levels and lives."""
        self.levels = [Level(difficulty) for difficulty in range(3, 7)]
        self.lives = 3
        self.score = 0

    def welcome(self):
        """Displays the welcome message and game instructions."""
        Utils.clear_screen()
        print("Welcome to SortQuest! Sort the items to progress through levels.\n\n"
              "Instructions:-\n"
              "You have to sort items into ascending order under 30 secs otherwise you will fail. \n"
              "If you solve under 10 secs, you will get 100 points; otherwise, you will get 50 points.")

    def show_stats(self, level):
        """Displays the current game statistics."""
        print(f"\nCurrent Level: {self.levels.index(level) + 1}")
        print(f"Current Score: {self.score}")
        print(f"Your Lives: {self.lives}\n")

    def start(self):
        """Starts the game and manages the game loop."""
        i = 0
        while i < len(self.levels) and self.lives > 0:
            level = self.levels[i]
            self.welcome()
            self.show_stats(level)

            result, score = level.play()
            self.score += score

            if result == "pass":
                i += 1
                input("Hooray!! You have passed the Level. Press Enter to continue...")
            elif result == "fail":
                self.lives -= 1
                input("Oops, Your Life is reduced by 1\nPress Enter to continue...")
            elif result == "retry":
                input("Press Enter To Retry...")

        print("Game Over\nThank you for playing SortQuest!")


if __name__ == "__main__":
    game = Game()
    game.start()

# 815805

# Sorting Game

import random
import time
import os


# Sorter class with a simple sorting algorithm (Bubble Sort)


class Sorter:
    def bubble_sort(items):
        n = len(items)
        for i in range(n):
            for j in range(0, n-i-1):
                if items[j] > items[j+1]:
                    items[j], items[j+1] = items[j+1], items[j]
        return items

# Level class


class Level:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.items = self.generate_items()

    def generate_items(self):
        return [random.randint(1, 100) for _ in range(self.difficulty)]

    def clear_screen():
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def play(self):
        print(f"\nCurrent Level: {self.difficulty-4}")
        print("Current items to sort: ")
        print(self.items)
        sorted_items = Sorter.bubble_sort(self.items[:])  # Make a copy to sort
        start_time = time.time()
        user_input = input("Enter the sorted items separated by spaces: ")
        duration = time.time() - start_time
        user_sorted = list(map(int, user_input.strip().split()))
        score = 0

        if user_sorted == sorted_items:
            score = 50
            input(
                f"Challenge completed in {duration:.2f} seconds. Press Enter to continue...")

            if duration < 10:
                score = 100
            if duration > 30:
                return False, 0

            return True, score
        else:
            print("That's not quite right. Here's the correct order:")
            print(sorted_items)
            return False, 0

# Game class


class Game:
    def __init__(self):
        # 5 levels, increasing difficulty
        self.levels = [Level(difficulty) for difficulty in range(5, 16)]

    def start(self):
        self.score = 0
        print("Welcome to SortQuest! Sort the items to progress through levels.\n")
        for level in self.levels:
            result, score = level.play()
            self.score += score
            print(f"\nCurrent Score: {self.score}")
            if not result:
                print(f"You Failed at Level {self.levels.index(level)+1}")
                break
        print("Thank you for playing SortQuest!")


if __name__ == "__main__":
    game = Game()
    game.start()

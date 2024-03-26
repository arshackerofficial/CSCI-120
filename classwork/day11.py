# # # # # # # # class Worker:
# # # # # # # #     def __init__(self, n, s, b=None):
# # # # # # # #         self.lname = n
# # # # # # # #         self.ssn = s
# # # # # # # #         self.boss = b


# # # # # # # # w = Worker("white", 123)
# # # # # # # # w2 = Worker("John", 1234, w)

# # # # # # # class Example:
# # # # # # #     def __init__(self, x):
# # # # # # #         self.x = x

# # # # # # #     def foo(self, y):
# # # # # # #         x = self.bar(y+1)
# # # # # # #         return x

# # # # # # #     def bar(self, y):
# # # # # # #         self.x = y-1
# # # # # # #         return self.x


# # # # # # # a = Example(3)

# # # # # # # print(a.foo(4))

# # # # # # import heapq
# # # # # # from collections import namedtuple, deque


# # # # # # class Maze:
# # # # # #     def __init__(self, width, height, start, end):
# # # # # #         self.width = width
# # # # # #         self.height = height
# # # # # #         self.start = start
# # # # # #         self.end = end
# # # # # #         self.grid = [['#'] * (2 * width + 1) for _ in range(2 * height + 1)]
# # # # # #         for x, y in (start, end):
# # # # # #             self.grid[2 * y][2 * x] = 'S' if (x, y) == start else 'E'

# # # # # #     def passable(self, cell):
# # # # # #         x, y = cell
# # # # # #         return 0 <= x < 2 * self.width and 0 <= y < 2 * self.height and self.grid[y][x] != '#'

# # # # # #     def neighbors(self, cell):
# # # # # #         x, y = cell
# # # # # #         results = set()
# # # # # #         for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
# # # # # #             nx, ny = x + dx, y + dy
# # # # # #             if self.passable((nx, ny)):
# # # # # #                 results.add((nx, ny))
# # # # # #         return results

# # # # # #     def __repr__(self):
# # # # # #         return '\n'.join(''.join(row) for row in self.grid)


# # # # # # Node = namedtuple('Node', 'f g h pos parent')


# # # # # # def bidirectional_dfs(maze):
# # # # # #     frontier_start = deque(
# # # # # #         [Node(0, 0, maze.heuristic(maze.start, maze.end), maze.start, None)])
# # # # # #     frontier_end = deque(
# # # # # #         [Node(0, 0, maze.heuristic(maze.end, maze.start), maze.end, None)])
# # # # # #     explored_start = {maze.start: None}
# # # # # #     explored_end = {maze.end: None}
# # # # # #     while frontier_start and frontier_end:
# # # # # #         path_start = search(frontier_start, explored_start, maze)
# # # # # #         path_end = search(frontier_end, explored_end, maze)
# # # # # #         if path_start and path_end:
# # # # # #             path_start.reverse()
# # # # # #             path_start.extend(path_end)
# # # # # #             return path_start

# # # # # #     return None


# # # # # # def search(frontier, explored, maze):
# # # # # #     while frontier:
# # # # # #         current = frontier.popleft()
# # # # # #         explored[current.pos] = current
# # # # # #         for neighbor_pos in maze.neighbors(current.pos):
# # # # # #             if neighbor_pos in explored:
# # # # # #                 continue
# # # # # #             tentative_g = current.g + 1
# # # # # #             neighbor = Node(tentative_g + maze.heuristic(neighbor_pos, maze.end),
# # # # # #                             tentative_g,
# # # # # #                             maze.heuristic(neighbor_pos, maze.end),
# # # # # #                             neighbor_pos,
# # # # # #                             current)
# # # # # #             if neighbor_pos not in frontier or frontier[neighbor_pos].g > tentative_g:
# # # # # #                 if neighbor_pos == maze.end:
# # # # # #                     return [neighbor_pos] + [n.pos for n in neighbor.path_to(neighbor_pos)]
# # # # # #                 frontier.append(neighbor)
# # # # # #                 frontier[neighbor_pos] = neighbor

# # # # # #     return None


# # # # # # def maze_heuristic(a, b):
# # # # # #     ax, ay = a
# # # # # #     bx, by = b
# # # # # #     return abs(ax - bx) + abs(ay - by)


# # # # # # def main():
# # # # # #     maze = Maze(10, 10, (0, 0), (19, 19))
# # # # # #     print(maze)
# # # # # #     path = bidirectional_dfs(maze)
# # # # # #     if path:
# # # # # #         print('Path found:')
# # # # # #         print(' -> '.join('(%d, %d)' % n for n in path))


# # # # # # main()
# # # # # def guess_number():
# # # # #     low, high = 1, 100
# # # # #     print("Think of a number between 1 and 100, and I'll try to guess it.")
# # # # #     while low <= high:
# # # # #         mid = (low + high) // 2
# # # # #         response = input(
# # # # #             f"Is your number {mid}? (yes/higher/lower): ").lower().strip()
# # # # #         if response == "yes":
# # # # #             print("Hooray! I've guessed your number!")
# # # # #             break
# # # # #         elif response == "higher":
# # # # #             low = mid + 1
# # # # #         elif response == "lower":
# # # # #             high = mid - 1
# # # # #         else:
# # # # #             print("Please enter 'yes', 'higher', or 'lower'.")


# # # # # guess_number()

# # # # def find_word(word_list, target):
# # # #     # Example of a linear search; for larger grids, consider more efficient search methods
# # # #     for word in word_list:
# # # #         if word == target:
# # # #             return True
# # # #     return False


# # # # word_list = ["python", "algorithm", "game", "search"]
# # # # target = input("Enter a word to find: ").lower().strip()
# # # # if find_word(word_list, target):
# # # #     print("Word found!")
# # # # else:
# # # #     print("Word not in list.")
# # # from random import shuffle


# # # def sorting_game():
# # #     numbers = list(range(1, 11))
# # #     shuffle(numbers)
# # #     print("Sort these numbers in ascending order:")
# # #     print(numbers)
# # #     # Example; in practice, implement a sorting algorithm
# # #     sorted_numbers = sorted(numbers)
# # #     user_input = list(
# # #         map(int, input("Enter the sorted numbers separated by space: ").split()))
# # #     if user_input == sorted_numbers:
# # #         print("Correct! Well done.")
# # #     else:
# # #         print("Incorrect. Try again.")


# # # sorting_game()
# # def treasure_hunt():
# #     treasure_location = (3, 3)  # Example position
# #     attempts = 0
# #     while True:
# #         attempts += 1
# #         guess = tuple(map(int, input("Enter your guess (row col): ").split()))
# #         if guess == treasure_location:
# #             print(f"Hooray! You've found the treasure in {attempts} attempts.")
# #             break
# #         else:
# #             print("Keep searching...")


# # treasure_hunt()

import random
import time
import os


# Sorter class with a simple sorting algorithm (Bubble Sort)
def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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

    def play(self):
        clear_screen()
        print(f"\nLevel Difficulty: {self.difficulty}")
        print("Current items to sort: ")
        print(self.items)
        sorted_items = Sorter.bubble_sort(self.items[:])  # Make a copy to sort
        start_time = time.time()
        user_input = input("Enter the sorted items separated by spaces: ")
        duration = time.time() - start_time
        user_sorted = list(map(int, user_input.strip().split()))

        if user_sorted == sorted_items:
            input(
                f"Challenge completed in {duration:.2f} seconds. Press Enter to continue...")
            return True
        else:
            print("That's not quite right. Here's the correct order:")
            print(sorted_items)
            return False

# Game class


class Game:
    def __init__(self):
        # 5 levels, increasing difficulty
        self.levels = [Level(difficulty) for difficulty in range(1, 6)]

    def start(self):
        print("Welcome to SortQuest! Sort the items to progress through levels.\n")
        for level in self.levels:
            if not level.play():
                print("Let's try that level again.")
                break
        print("Thank you for playing SortQuest!")


if __name__ == "__main__":
    game = Game()
    game.start()

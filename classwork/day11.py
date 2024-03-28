# # # # # # # # # # # class Worker:
# # # # # # # # # # #     def __init__(self, n, s, b=None):
# # # # # # # # # # #         self.lname = n
# # # # # # # # # # #         self.ssn = s
# # # # # # # # # # #         self.boss = b


# # # # # # # # # # # w = Worker("white", 123)
# # # # # # # # # # # w2 = Worker("John", 1234, w)

# # # # # # # # # # class Example:
# # # # # # # # # #     def __init__(self, x):
# # # # # # # # # #         self.x = x

# # # # # # # # # #     def foo(self, y):
# # # # # # # # # #         x = self.bar(y+1)
# # # # # # # # # #         return x

# # # # # # # # # #     def bar(self, y):
# # # # # # # # # #         self.x = y-1
# # # # # # # # # #         return self.x


# # # # # # # # # # a = Example(3)

# # # # # # # # # # print(a.foo(4))

# # # # # # # # # import heapq
# # # # # # # # # from collections import namedtuple, deque


# # # # # # # # # class Maze:
# # # # # # # # #     def __init__(self, width, height, start, end):
# # # # # # # # #         self.width = width
# # # # # # # # #         self.height = height
# # # # # # # # #         self.start = start
# # # # # # # # #         self.end = end
# # # # # # # # #         self.grid = [['#'] * (2 * width + 1) for _ in range(2 * height + 1)]
# # # # # # # # #         for x, y in (start, end):
# # # # # # # # #             self.grid[2 * y][2 * x] = 'S' if (x, y) == start else 'E'

# # # # # # # # #     def passable(self, cell):
# # # # # # # # #         x, y = cell
# # # # # # # # #         return 0 <= x < 2 * self.width and 0 <= y < 2 * self.height and self.grid[y][x] != '#'

# # # # # # # # #     def neighbors(self, cell):
# # # # # # # # #         x, y = cell
# # # # # # # # #         results = set()
# # # # # # # # #         for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
# # # # # # # # #             nx, ny = x + dx, y + dy
# # # # # # # # #             if self.passable((nx, ny)):
# # # # # # # # #                 results.add((nx, ny))
# # # # # # # # #         return results

# # # # # # # # #     def __repr__(self):
# # # # # # # # #         return '\n'.join(''.join(row) for row in self.grid)


# # # # # # # # # Node = namedtuple('Node', 'f g h pos parent')


# # # # # # # # # def bidirectional_dfs(maze):
# # # # # # # # #     frontier_start = deque(
# # # # # # # # #         [Node(0, 0, maze.heuristic(maze.start, maze.end), maze.start, None)])
# # # # # # # # #     frontier_end = deque(
# # # # # # # # #         [Node(0, 0, maze.heuristic(maze.end, maze.start), maze.end, None)])
# # # # # # # # #     explored_start = {maze.start: None}
# # # # # # # # #     explored_end = {maze.end: None}
# # # # # # # # #     while frontier_start and frontier_end:
# # # # # # # # #         path_start = search(frontier_start, explored_start, maze)
# # # # # # # # #         path_end = search(frontier_end, explored_end, maze)
# # # # # # # # #         if path_start and path_end:
# # # # # # # # #             path_start.reverse()
# # # # # # # # #             path_start.extend(path_end)
# # # # # # # # #             return path_start

# # # # # # # # #     return None


# # # # # # # # # def search(frontier, explored, maze):
# # # # # # # # #     while frontier:
# # # # # # # # #         current = frontier.popleft()
# # # # # # # # #         explored[current.pos] = current
# # # # # # # # #         for neighbor_pos in maze.neighbors(current.pos):
# # # # # # # # #             if neighbor_pos in explored:
# # # # # # # # #                 continue
# # # # # # # # #             tentative_g = current.g + 1
# # # # # # # # #             neighbor = Node(tentative_g + maze.heuristic(neighbor_pos, maze.end),
# # # # # # # # #                             tentative_g,
# # # # # # # # #                             maze.heuristic(neighbor_pos, maze.end),
# # # # # # # # #                             neighbor_pos,
# # # # # # # # #                             current)
# # # # # # # # #             if neighbor_pos not in frontier or frontier[neighbor_pos].g > tentative_g:
# # # # # # # # #                 if neighbor_pos == maze.end:
# # # # # # # # #                     return [neighbor_pos] + [n.pos for n in neighbor.path_to(neighbor_pos)]
# # # # # # # # #                 frontier.append(neighbor)
# # # # # # # # #                 frontier[neighbor_pos] = neighbor

# # # # # # # # #     return None


# # # # # # # # # def maze_heuristic(a, b):
# # # # # # # # #     ax, ay = a
# # # # # # # # #     bx, by = b
# # # # # # # # #     return abs(ax - bx) + abs(ay - by)


# # # # # # # # # def main():
# # # # # # # # #     maze = Maze(10, 10, (0, 0), (19, 19))
# # # # # # # # #     print(maze)
# # # # # # # # #     path = bidirectional_dfs(maze)
# # # # # # # # #     if path:
# # # # # # # # #         print('Path found:')
# # # # # # # # #         print(' -> '.join('(%d, %d)' % n for n in path))


# # # # # # # # # main()
# # # # # # # # def guess_number():
# # # # # # # #     low, high = 1, 100
# # # # # # # #     print("Think of a number between 1 and 100, and I'll try to guess it.")
# # # # # # # #     while low <= high:
# # # # # # # #         mid = (low + high) // 2
# # # # # # # #         response = input(
# # # # # # # #             f"Is your number {mid}? (yes/higher/lower): ").lower().strip()
# # # # # # # #         if response == "yes":
# # # # # # # #             print("Hooray! I've guessed your number!")
# # # # # # # #             break
# # # # # # # #         elif response == "higher":
# # # # # # # #             low = mid + 1
# # # # # # # #         elif response == "lower":
# # # # # # # #             high = mid - 1
# # # # # # # #         else:
# # # # # # # #             print("Please enter 'yes', 'higher', or 'lower'.")


# # # # # # # # guess_number()

# # # # # # # def find_word(word_list, target):
# # # # # # #     # Example of a linear search; for larger grids, consider more efficient search methods
# # # # # # #     for word in word_list:
# # # # # # #         if word == target:
# # # # # # #             return True
# # # # # # #     return False


# # # # # # # word_list = ["python", "algorithm", "game", "search"]
# # # # # # # target = input("Enter a word to find: ").lower().strip()
# # # # # # # if find_word(word_list, target):
# # # # # # #     print("Word found!")
# # # # # # # else:
# # # # # # #     print("Word not in list.")
# # # # # # from random import shuffle


# # # # # # def sorting_game():
# # # # # #     numbers = list(range(1, 11))
# # # # # #     shuffle(numbers)
# # # # # #     print("Sort these numbers in ascending order:")
# # # # # #     print(numbers)
# # # # # #     # Example; in practice, implement a sorting algorithm
# # # # # #     sorted_numbers = sorted(numbers)
# # # # # #     user_input = list(
# # # # # #         map(int, input("Enter the sorted numbers separated by space: ").split()))
# # # # # #     if user_input == sorted_numbers:
# # # # # #         print("Correct! Well done.")
# # # # # #     else:
# # # # # #         print("Incorrect. Try again.")


# # # # # # sorting_game()
# # # # # def treasure_hunt():
# # # # #     treasure_location = (3, 3)  # Example position
# # # # #     attempts = 0
# # # # #     while True:
# # # # #         attempts += 1
# # # # #         guess = tuple(map(int, input("Enter your guess (row col): ").split()))
# # # # #         if guess == treasure_location:
# # # # #             print(f"Hooray! You've found the treasure in {attempts} attempts.")
# # # # #             break
# # # # #         else:
# # # # #             print("Keep searching...")


# # # # # treasure_hunt()



# # import numpy as np
# # import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation

# # # Circle properties
# # circle_radius = 1
# # circle_center = (0, 0)

# # # Ball properties
# # ball_pos = np.array([0.5, 0.5])
# # ball_vel = np.array([0.01, 0.015])

# # # Plot limits
# # xlim = (-1.1, 1.1)
# # ylim = (-1.1, 1.1)

# # fig, ax = plt.subplots()
# # ax.set_xlim(xlim)
# # ax.set_ylim(ylim)
# # circle = plt.Circle(circle_center, circle_radius,
# #                     edgecolor='b', facecolor='none')
# # ax.add_artist(circle)

# # ball, = plt.plot([], [], 'go', markersize=10)
# # line, = plt.plot([], [], 'r-')


# # def init():
# #     ball.set_data([], [])
# #     line.set_data([], [])
# #     return ball, line


# # def update(frame):
# #     global ball_pos, ball_vel
# #     ball_pos += ball_vel

# #     # Check for collision with the circle and reflect the ball
# #     if np.linalg.norm(ball_pos) >= circle_radius:
# #         ball_vel = ball_pos / np.linalg.norm(ball_pos) * -np.abs(ball_vel)

# #     ball.set_data(ball_pos[0], ball_pos[1])
# #     line.set_data([0, ball_pos[0]], [0, ball_pos[1]])

# #     return ball, line


# # anim = FuncAnimation(fig, update, frames=range(
# #     200), init_func=init, blit=True, interval=20)
# # plt.axis('off')
# # plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Circle properties
# circle_radius = 1
# circle_center = np.array([0., 0.])

# # Ball properties
# ball_pos = np.array([0., 0.5])
# ball_vel = np.array([0.03, 0.04])  # Increased initial velocity

# # Physics
# coef_of_restitution = 0.75  # Bounce effect; 1 for elastic, <1 for inelastic

# # Plot setup
# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# ax.set_xlim(-1.1, 1.1)
# ax.set_ylim(-1.1, 1.1)
# circle = plt.Circle(circle_center, circle_radius,
#                     edgecolor='b', linewidth=2, facecolor='none')
# ax.add_artist(circle)
# ball, = plt.plot([], [], 'go', markersize=8)
# lines = []


# def init():
#     ball.set_data([], [])
#     return [ball] + lines


# def update(frame):
#     global ball_pos, ball_vel, lines
#     ball_pos += ball_vel

#     # Check for collision and update velocity and position accordingly
#     distance_from_center = np.linalg.norm(ball_pos)
#     if distance_from_center >= circle_radius:
#         # Calculate reflection
#         normal = ball_pos / distance_from_center
#         ball_vel -= 2 * np.dot(ball_vel, normal) * normal
#         # Apply the coefficient of restitution to simulate energy loss
#         ball_vel *= coef_of_restitution
#         # Correct ball position to be on the circle's edge
#         ball_pos = normal * circle_radius

#         # Create a new line for each bounce
#         new_line, = plt.plot([ball_pos[0], circle_center[0]], [
#                              ball_pos[1], circle_center[1]], 'r-')
#         lines.append(new_line)

#     ball.set_data(ball_pos[0], ball_pos[1])
#     return [ball] + lines


# anim = FuncAnimation(fig, update, frames=np.arange(
#     0, 500), init_func=init, blit=True, interval=10)
# plt.axis('off')
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Circle properties
circle_radius = 1
circle_center = np.array([0., 0.])

# Ball properties
ball_pos = np.array([0., 0.5])
ball_vel = np.array([0.03, 0.04])  # Increased initial velocity
ball_radius = 0.05  # Increased ball size

# Physics
coef_of_restitution = 0.75  # Bounce effect; 1 for elastic, <1 for inelastic

# Plot setup
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
circle = plt.Circle(circle_center, circle_radius,
                    edgecolor='b', linewidth=2, facecolor='none')
ax.add_artist(circle)
ball = plt.Circle((0, 0), ball_radius, color='g')
ax.add_artist(ball)
lines = []


def init():
    return [ball] + lines


def update(frame):
    global ball_pos, ball_vel, lines
    ball_pos += ball_vel

    # Check for collision and update velocity and position accordingly
    distance_from_center = np.linalg.norm(ball_pos)
    if distance_from_center >= circle_radius:
        # Calculate reflection
        normal = ball_pos / distance_from_center
        ball_vel -= 2 * np.dot(ball_vel, normal) * normal
        # Apply the coefficient of restitution to simulate energy loss
        ball_vel *= coef_of_restitution
        # Correct ball position to be on the circle's edge
        ball_pos = normal * circle_radius

        # Create a new line for each bounce
        new_line, = plt.plot([ball.get_center()[0], ball_pos[0]], [
                             ball.get_center()[1], ball_pos[1]], 'r-')
        lines.append(new_line)

    ball.set_center((ball_pos[0], ball_pos[1]))
    return [ball] + lines


anim = FuncAnimation(fig, update, frames=np.arange(
    0, 500), init_func=init, blit=True, interval=10)
plt.axis('off')
plt.show()

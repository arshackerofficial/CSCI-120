import os


def print2d(d):
    print("------------------\n\n")
    for i in d:
        print(i)
    print("\n\n------------------")


def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)


d = [
    ["+", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""]
]
x_vel = 1
y_vel = -1
ball_x = 0
ball_y = 0


while True:
    clear_screen()
    print2d(d)

    d[ball_y][ball_x] = ""

    ball_x += x_vel
    ball_y -= y_vel

    if ball_y < 0 or ball_y >= len(d):
        y_vel = -y_vel
        ball_y -= 2*y_vel

    if ball_x < 0 or ball_x >= len(d[ball_y]):
        x_vel = -x_vel
        ball_x += 2*x_vel

    d[ball_y][ball_x] = "+"

    inn = input().lower()
    if inn == "exit":
        break

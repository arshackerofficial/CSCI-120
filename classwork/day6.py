
# # def rotate(arr):
# #     for i in range(len(arr)):
# #         arr[0][i], arr[i][0] = arr[i][0], arr[0][i]
# #     print2d(arr)

# def print2d(arr):
#     print("\n\n-----------------------------------------------------------\n\n")
#     for i in arr:
#         print(i)


# # b = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]


# # print2d(b)
# # rotate(b)


# # d = {"Grandville" : [1100, 1110,1120 , 1130, 1140],
# #      "Surrey Central": [1100,1120,1140]
# #      }

# # for i in range(1100, 1150, 10):
# #     trainAt = []
# #     for station in d:
# #         if i in d[station]:
# #             trainAt.append(station)
# #     print(f"Current Time is: {i} {str(trainAt).replace("["," Train arrived at: ").replace("]","").replace("'","").replace(","," and")}")


def print2d(d):
    print("\n\n-----------------------------------------------------------\n\n")
    for i in d:
        print(i)


d = [
    ["+", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
]
x_vel = 1
y_vel = -1
ball_x = 0
ball_y = 0


while True:
    print2d(d)

    d[ball_y][ball_x] = ""

    ball_x += x_vel
    ball_y -= y_vel

    if ball_y < 0 or ball_y >= len(d):
        y_vel = -y_vel
        ball_y -= 2*y_vel
        pass

    if ball_x < 0 or ball_x >= len(d):
        x_vel = -x_vel
        ball_x += 2*x_vel
        pass
    d[ball_y][ball_x] = "+"

    inn = input().lower()
    if inn == "exit":
        break

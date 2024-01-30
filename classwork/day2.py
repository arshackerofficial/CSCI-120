# ------------------------LOOPS-------------------------

# Version 1

# cities = ["Vancouver", "Burnaby", "Coquitlam", "Richmond"]

# def prompt(prompt, valid):
#     i, userInput, response = 0, input(prompt), ""
#     while i < len(valid): response = "Correct" if userInput == valid[i] else "Incorrect"; i += 1
#     return response

# print(prompt("What Cites are in Metro Vancouver? ", cities))


# cities = ["Vancouver", "Burnaby", "Coquitlam", "Richmond"]

# Version 2

# def prompt(prompt, valid):
#     while (True):
#         userInput, i = input(prompt) , 0
#         while i < len(valid): 
#             if userInput == valid[i]:
#                 return "Correct" 
#             i += 1

# print(prompt("What Cites are in Metro Vancouver? ", cities))

# Version 3

# cities = ["Vancouver", "Burnaby", "Coquitlam", "Richmond", "Surrey"]

# def prompt(prompt, valid):
#     response = "Incorrect"
#     while (response == "Incorrect"):
#         userInput = input(prompt)
#         try: response = "Correct" if isinstance(valid.index(userInput), int) else "Incorrect"
#         except: response = "Incorrect"; print(response)
#     return response

# print(prompt("What Cites are in Metro Vancouver? ", cities))

# Version 4

# cities = ["Vancouver", "Burnaby", "Coquitlam", "Richmond", "Surrey"]

# def prompt(prompt, valid):
#     response = "Incorrect"
#     while (response == "Incorrect"):
#         userInput = input(prompt)
#         response = "Correct" if userInput in valid else "Incorrect"
#     return response

# print(prompt("What Cites are in Metro Vancouver? ", cities))

# ----------------------------------------------------------------------------------------------------------


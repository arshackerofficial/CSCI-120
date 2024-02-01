#Arshpreet Singh Sidhu
#815805

# Fruit Calories Program


calories = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

user_input = input("Enter a fruit: ").lower()

if user_input in calories:
    calorie_in_fruit = calories[user_input]
    print(f"Accoring to FDA's Poster, The calories in one portion of {user_input.capitalize()} are {calorie_in_fruit}.")
else:
    print("Invalid input. Please enter a valid fruit.")
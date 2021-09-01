# Unit 5: Conditionals

    # 5.1 & 5.2 - Basic Conditionals (only return a boolean [True or False])

"""
    Comparison Operators:
        == - left is equal to right
        != - left is not equal to right
        > - left is greater than right
        < - left is less than right
        >= - left is greater than or equal to right
        <= - left is less than or equal to right
"""

favorite_food = 'pizza'

print(favorite_food == 'biryani') # prints False onto the console/terminal
print(favorite_food != 'biryani') # prints True onto the console/terminal
print(10 > 5) # prints True onto the console/terminal
print(25 < 110) # prints True onto the console/terminal
print(5 <= 5) # prints True onto the console/terminal
print(229 >= 229) # prints True onto the console/terminal

"""
    Logical Operators:
        and - both of the conditions have to be true. If one of them results in being False, the entire condition is False.
        or - one of the conditions have to be true. If one of them results in being True, the entire condition is True.
        not - "flips" the condition. If it's True, it turns to False. If it's False, it turns to True
"""

print(10 < 5 and 15 > 2) # prints False onto the console/terminal even though 15 is greater than 2

favorite_game = 'minecraft'

print(favorite_game == 'roblox' or favorite_game == 'minecraft') # prints True onto the console/terminal even though favorite_game does not equal to 'roblox'

print(not favorite_game == 'minecraft') # prints False onto the console/terminal

    # 5.3 - If Statements

favorite_car = 'lamborghini'

if favorite_car == 'lamborghini':
    print(f'My favorite car is a {favorite_car}') # prints "My favorite car is lamborghini" onto the console/terminal since the condition is true

    # 5.4 - If-else Statements

if favorite_car == 'ferrari':
    print('My favorite car is a ferrari')
else:
    print(f'My favorite car is not a ferrari, it is a {favorite_car}') # prints "My favorite car is not a ferrari, it is a lamborghini" onto the console/terminal since favorite_car does not equal to "ferrari"

    # 5.4 - 5.6 - If-elif and If-elif-else Statements

most_popular_item = 'biryani'

if most_popular_item == 'mac and cheese':
    print('The most popular item on the menu is the mac and cheese')
elif most_popular_item == 'biryani':
    print(f'The most popular item on the menu is the {most_popular_item}') # prints "The most popular item on the menu is the biryani" onto the console/terminal since most_popular_item is equal to "biryani"

available_games = 'minecraft'

if available_games == '2k 21':
    print('There is only a 2k 21 game available at best buy right now')
elif available_games == 'madden 21':
    print('There is only a madden 21 game available at best buy right now')
else:
    print(f"2k 21 and madden 21 aren't available right now. There's only a {available_games} game that's available") # prints "2k 21 and madden 21 aren't available right now. There's only a minecraft game that's available" onto the console/terminal since available_games isn't equal to 2k 21 or madden 21

    # Bonus: Ternary Operators

color = 'green'

color_value = 'color is equal to green' if color == 'green' else 'color is not equal to green' # color_value will be equal to "color is equal to green" if color is equal to green. Else, it will be equal to "color is not equal to green"

print(color_value) # prints "color is equal to green" onto the console/terminal

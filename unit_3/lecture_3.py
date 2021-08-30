# Unit 3: Lists

    # 3.1 - Printing Lists & Accessing Specific Items in a List Through the Item's Index

games = ['Minecraft', 'Roblox', 'Tetris', 'Pac-Man']

print(games) # prints ['Minecraft', 'Roblox', 'Tetris', 'Pac-Man'] onto the console/terminal

print(games[0]) # prints "Minecraft" onto the console/terminal since indexes start at 0
print(games[1]) # prints "Roblox" onto the console/terminal
print(games[2]) # prints "Tetris" onto the console/terminal
print(games[3]) # prints "Pac-Man" onto the console/terminal

    # 3.2 - 3.4 - Using f Strings with List Indexes

print(f'My favorite game is {games[0]}') # prints "My favorite game is Minecraft"

    # 3.5 - 3.6 - List Methods

# Adding items onto a list

favorite_food = ['chicken', 'biryani']

favorite_food.append('pizza')

print(favorite_food) # prints ['chicken', 'biryani', 'pizza'] onto the console/terminal since .append('pizza') modified the array by adding 'pizza' onto the end of the list

favorite_food.insert(0, 'steak') # inserts "steak" at index 0

print(favorite_food) # prints ['steak', 'chicken', 'biryani', 'pizza'] onto the console/terminal

favorite_food.insert(2, 'mac and cheese') # inserts "mac and cheese" at index 2

print(favorite_food) # prints ['steak', 'chicken', 'mac and cheese', 'biryani', 'pizza'] onto the console/terminal

# Removing items from a list

classes = ['english', 'spanish', 'math', 'history', 'science', 'physical education']

classes.pop() # removes the last item from the list

print(classes) # prints ['english', 'spanish', 'math', 'history', 'science'] onto the console/terminal

classes.pop(1) # removes the item in the list whose index is 1, which is spanish

print(classes) # prints ['english', 'math', 'history', 'science'] onto the console/terminal

    # 3.7 - Sorting the Order of the List & Reversing the Order
    
# sorting the list

numbers = [3, 1, 4, 5, 2]

numbers.sort() # sorts the array

print(numbers)

other_numbers = [25, 20, 10, 15]

sorted_set_of_numbers = sorted(other_numbers) # when using the sorted() method, it needs to be stored in a variable since it doesn't modify the list itself

# reversing the list

letters = ['h', 'a', 'b', 't']

letters.sort(reverse = True) # reverse = True reverses the order of the list

print(letters) # prints ['t', 'h', 'b', 'a'] onto the console/terminal

names = ['Joe', 'John', 'Adam', 'Brock']

names.reverse() # reverses the order the array was written in

print(names) # prints names = ['Joe', 'John', 'Adam', 'Brock'] onto the console/terminal

    # Bonus - Getting a List's Length

print(len(names)) # prints 4 onto the console/terminal

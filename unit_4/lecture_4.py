# Unit 4: For Loops, Working with Lists & Other Ways of Storing Mutliple Pieces of Information

    # 4.1 - 4.2 - Using For Loops on Lists

movies = ['Avengers: End Game', 'Ralph Breaks the Internet']

for movie in movies:
    print(movie) # prints "Avengers: End Game", and "Ralph Breaks the Internet" in seperate lines onto the console/terminal

    # 4.3 - Using For Loops to "get from point A to point B"

for i in range(5, 11):
    print(i) # prints numbers 5-10 onto the console/terminal

    # 4.4 & 4.5 - Creating a List Based on Ranges

numbers = list(range(1, 6))

for num in numbers:
    print(num) # prints numbers 1-5 onto the console/terminal
print(min(numbers)) # executes after the for loop is done iterating over the list
print(max(numbers)) # executes after the print(min(numbers)) runs
print(sum(numbers)) # prints the sum of all of the numbers in the list

    # 4.6 - Finding Even or Odd Numbers in a Range

for even_num in range(0, 15, 2):
    print(even_num) # prints all the even numbers that fall between 0 (inclusive) & 15 (exclusive)

    # 4.7 - Cubing Numbers Within a Range

for cubed_num in range(10, 21):
    print(cubed_num ** 3) # prints every number ranging from 10 (inclusive) to 21 (exclusive) cubed onto the console/terminal

    # 4.8 - Printing More Than One Item From a List

candies = ['hershey', 'snickers', 'twix', 'milky way']

print(f'My favorite candies are {candies[slice(2)]}') # prints "My favorite candies are ['hershey', 'snickers']" onto the console/terminal

    # 4.9 - Using Tuples

cars = ('bmw', 'ferrari', 'lamborghini', 'volkswagen')

print(cars) # prints ('bmw', 'ferrari', 'lamborghini', 'volkswagen') onto the console/terminal

print(cars[1]) # prints "ferrari" onto the console/terminal

for car in cars:
    print(car) # prints "bmw", "ferrari", "lamborghini", "volkswagen" onto the terminal/console

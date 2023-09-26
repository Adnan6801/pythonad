myString = "This is a string."
print(myString)
print(type(myString))


print(myString + " is of the data type " + str(type(myString)))
name = input("What is your name? ")
print(name)
movie = input("Which is your favorite movie?  ")
song = input("Which is your favorite song?  ")
print("{}, you like a {} {}!".format(name,movie,song))
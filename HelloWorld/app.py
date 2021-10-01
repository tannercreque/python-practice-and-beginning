#print('Hello World') #String, obviously
#Variables are temporarily stored data. Ex:
age = 20
price = 19.95
first_name = "Tanner"  #Noticing no commas or ; between variable declaration.
is_online = True  #Booleans are the same, Capital start.

print(age) #Note to self, similar syntax to JS, variable definition is basically the same.

#Getting user input
name = input("What is your name? ") #Space between ? and " is so that there is a space between what is being asked to the user, and what is inputted by the user.
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2021 - int(birth_year)
print(age)

#My calculator solution
first = input("First: ")
second = input("Second: ")
sum = int(first) + int(second)
print(sum)

# While loops

# basic overview of while loop:

count = 0

if count < 5:
  print "Hello, I am an if statement and count is", count

while count < 10:
  print "Hello, I am a while and count is", count
  count += 1

# while loops can also use boolean values:
loop_condition = True

while loop_condition:
  print "I am a loop"
  loop_condition = False



# A common application of a while loop is to check user input to see if it is valid. 
# For example, if you ask the user to enter y or n and they instead enter 7, then you should re-prompt them for input.

# Fill in the loop condition so the user will be prompted for a choice over and over while choice does not equal 'y' and choice does not equal 'n'.
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")



# The break is a one-line statement that means "exit the current loop." 
# An alternate way to make our counting loop exit and stop executing is with the break statement.
# this example would run forever except for the 'break' statement. 
count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break



# While / else
# Something completely different about Python is the while/else construction. 
# while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False.
# This means that it will execute if the loop is never entered or if the loop exits normally. 
# If the loop exits as the result of a break, the else will not be executed.
# In this example, the loop will break if a 5 is generated, and the else will not execute. 
# Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"



# Make a game similar to the above example, allow the user to guess what a number is 3 times.

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while guesses_left > 0:
  # gather input
  guess = int(raw_input("Your guess: "))
  
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
  
else:
  print "You lose"



# Can also do loops using 'for'
print "Counting..."

for i in range(20):
  print i


# Create a for loop that prompts the user for a hobby 3 times.
# Save the result of each prompt in a hobby variable
# append each one to hobbies.
# print hobbies after your for loop
# Make sure to answer the prompts in the terminal when testing your code!

hobbies = []

for num in range(3):
  hobby =  raw_input("Tell me one of your favorite hobbies: ")
  hobbies.append(hobby)

print hobbies


# You can loop through each letter in a string:
for x in word:
  print x


# you can manipulate strings using for loops:
# Let's filter out the letter "A" from our string.
# Do the following for each character in the phrase.
# If char is an "A" or char is an "a", print "X", instead of char. Make sure to include the trailing comma.
# Otherwise (else:), please print char, with the trailing comma.

phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A":
    print "X",
  elif char == "a":
    print "X",
  else:
    print char,
#Don't delete this print statement!
print


# Lists 

# On each iteration, the variable num will be the next value in the list. 
# So, the first time through, it will be 7, the second time it will be 9, then 12, 54, 99, and then the loop will exit when there are no more values in the list.

# Write a second for loop that goes through the numbers list and prints each element squared, each on its own line.

numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
  print num

# Add your loop below!
for x in numbers:
  print x * x


# Dictionaries

# You may be wondering how looping over a dictionary would work. Would you get the key or the value?

# The short answer is: you get the key which you can use to get the value.

d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
  if d[key] == 10:
    print "This dictionary has the value 10!"

# First, we create a dictionary with strings as the keys and numbers as the values.
# Then, we iterate through the dictionary, each time storing the key in key.
# Next, we check if that key's value is equal to 10.
# If so, we print "This dictionary has the value 10!"

# On line 5, print the key, followed by a space, followed by the value associated with that key.

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print key, d[key]


# Indexing 

# A weakness of using this for-each style of iteration is that you don't know the index of the thing you're looking at. 
# Generally this isn't an issue, but at times it is useful to know how far into the list you are. 
# Thankfully the built-in enumerate function helps with this.
# enumerate works by supplying a corresponding index to each element in the list that you pass it. 
# Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. 
# It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index + 1, item
  # index +1 makes it start at 1 instead of 0, which is default.


# Multiple Lists

# It's also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.
# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
# zip can handle three or more lists as well!

# Compare each pair of elements and print the larger of the two

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print a
  else:
    print b


# For / else

# Just like with while, for loops may have an else associated with them.
# In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. 
# This code will break when it hits 'tomato', so the else block won't be executed.

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
  if f == 'tomato':
    print 'A tomato is not a fruit!' # (It actually is.)
    break
  print 'A', f
else:
  print 'A fine selection of fruits!'
  #the else isn't executed due to the 'break' above. If it is removed the else statement will be ran


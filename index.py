# from math import floor


# print("Hello World")

# #A small program to add two numbers
# num1 = 10
# num2 = 30

# #Adds the two numbers together
# sum = num1 + num2

# #Displays the sum on screen
# print("The total of your two numbers is:", sum)

# # Having fun with seconds in a function

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds

# # Because the function returns 3 items we can aslo do an assigment of 3 variables and the function will indivdually asign them based on indexing. 
 
# bleh, blah, bluh = convert_seconds(5000)
# print(bleh, blah, bluh)


# def hint_username(username):
#     if len(username) < 3 :
#         print("Username needs to be more than 3 characters long")
#     else : 
#         print("Valid username")

# hint_username("12")
# hint_username("123")

# def numcheck(number):
#     if number > 11: 
#         print(0)
#     elif number != 10:
#         print(1)
#     elif number >= 20 or number < 12:
#          print(2)
#     else:
#         print(3)

# numcheck(10)


# # Playing with modulos and interesting formats.
# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = filesize / block_size
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = full_blocks % 1
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return block_size * floor(full_blocks) + block_size
#     return block_size * floor(full_blocks)

# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192


# # Double functions
# def sum(x, y):
#         return(x+y)

# print(sum(sum(1,2), sum(3,4)))


# # A while loop, basic. 
# x = 0
# while x < 5:
#     print("Not quite there yet, x is equal to:", str(x))
#     x = x + 1
# print("X is equal to:", str(x))

# # A while loop making sure to re-asign variable prior to use. 
# x = 1
# sum = 0
# while x < 10:
#     sum = sum + x
#     x = x + 1

# product = 1
# x = 1 # X is re-asigned here so It can be properly used. 
# while x < 10:
#     product = product * x
#     x = x + 1

# print(sum, product)

#  For loop examples. 
# for x in range(5):
#     print(x)

# For loop in a function
# def printFive():
#     for x in range(5):
#         print("hi", x)

# printFive()

# An example using an array of numbers
# values = [ 23,51,64,25,99,65 ]
# sum = 0
# length = 0
# for value in values:
#     sum += value
#     length += 1
# print("Total sum: " + str(sum) +"\n Average: " + str(sum/length))


# A for loop that jumps each 10th number and uses a function
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10): # The 3rd argument here is what defined how many numbers to jump in the range of the first two arguments. 
  print(x, to_celsius(x))
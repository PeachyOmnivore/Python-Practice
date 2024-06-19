from math import floor


print("Hello World")

#A small program to add two numbers
num1 = 10
num2 = 30

#Adds the two numbers together
sum = num1 + num2

#Displays the sum on screen
print("The total of your two numbers is:", sum)

# Having fun with seconds in a function

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

# Because the function returns 3 items we can aslo do an assigment of 3 variables and the function will indivdually asign them based on indexing. 
 
bleh, blah, bluh = convert_seconds(5000)
print(bleh, blah, bluh)


def hint_username(username):
    if len(username) < 3 :
        print("Username needs to be more than 3 characters long")
    else : 
        print("Valid username")

hint_username("12")
hint_username("123")

def numcheck(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
         print(2)
    else:
        print(3)

numcheck(10)


# Playing with modulos and interesting formats.
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize / block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = full_blocks % 1
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * floor(full_blocks) + block_size
    return block_size * floor(full_blocks)

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


# Double functions
def sum(x, y):
        return(x+y)

print(sum(sum(1,2), sum(3,4)))

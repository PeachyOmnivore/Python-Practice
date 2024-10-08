# from math import floor

#--------------------------------------------------------------------------------------------------------------------------------

# print("Hello World")

#--------------------------------------------------------------------------------------------------------------------------------

# #A small program to add two numbers
# num1 = 10
# num2 = 30

# #Adds the two numbers together
# sum = num1 + num2

# #Displays the sum on screen
# print("The total of your two numbers is:", sum)

#--------------------------------------------------------------------------------------------------------------------------------

# # Having fun with seconds in a function

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds

# # Because the function returns 3 items we can aslo do an assigment of 3 variables and the function will indivdually asign them based on indexing. 
 
# bleh, blah, bluh = convert_seconds(5000)
# print(bleh, blah, bluh)

#--------------------------------------------------------------------------------------------------------------------------------

# def hint_username(username):
#     if len(username) < 3 :
#         print("Username needs to be more than 3 characters long")
#     else : 
#         print("Valid username")

# hint_username("12")
# hint_username("123")

#--------------------------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------------------------

# # Double functions
# def sum(x, y):
#         return(x+y)

# print(sum(sum(1,2), sum(3,4)))

#--------------------------------------------------------------------------------------------------------------------------------

# # A while loop, basic. 
# x = 0
# while x < 5:
#     print("Not quite there yet, x is equal to:", str(x))
#     x = x + 1
# print("X is equal to:", str(x))

#--------------------------------------------------------------------------------------------------------------------------------

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

#--------------------------------------------------------------------------------------------------------------------------------

#  # For loop examples. 
# for x in range(5):
#     print(x)

#--------------------------------------------------------------------------------------------------------------------------------

# # For loop in a function
# def printFive():
#     for x in range(5):
#         print("hi", x)

# printFive()

#--------------------------------------------------------------------------------------------------------------------------------

# # An example using an array of numbers
# values = [ 23,51,64,25,99,65 ]
# sum = 0
# length = 0
# for value in values:
#     sum += value
#     length += 1
# print("Total sum: " + str(sum) +"\n Average: " + str(sum/length))

#--------------------------------------------------------------------------------------------------------------------------------

# # A for loop that jumps each 10th number and uses a function
# def to_celsius(x):
#   return (x-32)*5/9

# for x in range(0,101,10): # The 3rd argument here is what defined how many numbers to jump in the range of the first two arguments. IMPORTANT: range doesnt include the last element. So the last number should be 1 more than intention.
#   print(x, to_celsius(x))

#--------------------------------------------------------------------------------------------------------------------------------

# # If we want to count backwards we have to use the 3rd argument to tell the for loop to look for a negative number range.
# for x in range(1, -11, -1):
#     print(x) # Prints 1 to -10

#--------------------------------------------------------------------------------------------------------------------------------

# # Lets make some dominoes
# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + "|" + str(right) + "]", end=" ") # The end argument here defines how the print function will end. By default it makes a newline. Where now we define the newline character to be a space. 
#     print()

#--------------------------------------------------------------------------------------------------------------------------------

# # Making a nested loop for pairings of names in all orders whilst not repeating same name against itself. 
# teams = [ "Pandas", "Tigers", "Bears", "Eagles"]
# for home_team in teams:
#     for away_teams in teams:
#         if home_team != away_teams:
#             print(home_team + " vs " + away_teams)

#--------------------------------------------------------------------------------------------------------------------------------

# #Some slicing using a colon
# string1 = "Greetings, Earthlings" # One long string
# print(string1[0])   # Prints “G”
# print(string1[4:8]) # Prints “ting”
# print(string1[11:]) # Prints “Earthlings”
# print(string1[:5])  # Prints “Greet”
# print(string1[-10:])  # Prints “Earthlings but counts backwards from end of string”

# # This is using :: which represents a stride
# print(string1[0::2]) # Prints “Getns atlns” Every second character starting from 0
# print(string1[::-1]) # Prints “sgnilhtraE ,sgniteerG” Prints every charcater backwards. No full range set. 
# print(string1[9::-1]) # Prints “sgniteerG” Prints every charcater backwards from index 9 

#--------------------------------------------------------------------------------------------------------------------------------

# # Some use of .join
# greetings = ["Hello", "world", "!"]
# print(" ".join(greetings)) # Prints "Hello world !" Notice the addition of the space at the end of world before !

# # We can concatonate instead
# greetingTwo = ["Hello", "world"]
# print(" ".join(greetingTwo) + "!")

#--------------------------------------------------------------------------------------------------------------------------------


# # Prints only vowels. 
# input = "Four score and seven years ago"

# for c in input:
#   if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(c)

#--------------------------------------------------------------------------------------------------------------------------------

# String methods, replacement with slice method.
# def replace_domain(email, old_domain, new_domain):
#   if "@" + old_domain in email:
#     index = email.index("@" + old_domain)
#     print(index)
#     new_email = email[:index] + "@" + new_domain
#     return print(new_email)
#   return email

# replace_domain('lad_777@mail.com', 'mail.com', 'hotmail.com')

#--------------------------------------------------------------------------------------------------------------------------------

# def create_staircase(nums):
#   while len(nums) != 0:
#     step = 1
#     subsets = []
#     if len(nums) >= step:
#       subsets.append(nums[0:step])
#       nums = nums[step:]
#       step += 1
#     else:
#       return False

#   return subsets

# print(create_staircase([1, 2, 3, 4, 5, 6, 7]))

#--------------------------------------------------------------------------------------------------------------------------------

#  An example of using enumerate, this allows us to unpack both the names in winners with its coorisponding index. 
# winners = ["Ashley", "John", "Fred"]
# for index, winner in enumerate(winners):
#     print("{} - {}".format(index+1, winner))

#--------------------------------------------------------------------------------------------------------------------------------

# # An Example of list comprehensions:
# mulitpleOfSeven = [x*7 for x in range(1,11)]
# print(mulitpleOfSeven)


# languages = ["Python", "Go", "Java", "Perl", "C"]
# lengths = [len(lang) for lang in languages]
# print(lengths)


# Prints values of 3 in a comprehension
# z = [x  for x in range(1,101) if x % 3 == 0]
# print(z)

#--------------------------------------------------------------------------------------------------------------------------------

# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   print(words)
#   for word in words:
#     # Create the pig latin word and add it to the list
#     firstChar = word[0]
#     word.remove(word[0])
#     word.append(firstChar + "lay")
#     say.append(word)
#     # Turn the list back into a phrase
#   return say
    
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun"))

#--------------------------------------------------------------------------------------------------------------------------------

#  a function that runs through a dictionary of groups and users. Then collates users to specific groups in a new dictionary. 

def groups_per_user(group_dictionary):
	user_groups = {}
	for group, users in group_dictionary.items():
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

#--------------------------------------------------------------------------------------------------------------------------------

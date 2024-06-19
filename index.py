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
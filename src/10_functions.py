# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    if (num % 2) == 0:
        print("EVEN!!!")
    else:
        print("ODD!!!")
is_even(6)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def iss_even(num):
    if (num % 2) == 0:  
        print("Even")  
    else:  
        print("Odd")
iss_even(num)
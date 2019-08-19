import math
user_name = input("What is your name? ")
# old way with concatenation:
greeting = "Hello, " + user_name + "!"
# or with string formatting:
greeting = "Hello, {0}!".format(user_name)
# new way with f-string:
greeting = f"Hello, {user_name}!"
print (greeting)
# format specification is also available:
pi_statement = f"pi is {math.pi:.4f}"
print (pi_statement)
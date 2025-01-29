"""Write a Python code to accept a string from the user and display characters present at an even index number.\
For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.\
Expected Output:

Orginal String is  PYnative
Printing only even index chars
P
n
t
v"""

user = str(input("Enter your text : "))
calc = len(user)

for i in range(0, calc-1, 2):
    print("Index[", i , "]" , user[i])


"How to Sum of the N positive Integers in python"

num = int(input("How many positive number you have :"))
p_num = []

for n in range(num):

    numbers = int(input("Enter the positive numbers : "))
    p_num.append(numbers)

print("Sum = ",sum(p_num))

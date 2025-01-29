"Write a python code to iterate first 10 numbers, and in each iteration, print the sum of the current and previous number\
output :Printing current and previous number sum in a range(10)\
        Current Number 0 Previous Number  0  Sum:  0\
        Current Number 1 Previous Number  0  Sum:  1\
        Current Number 2 Previous Number  1  Sum:  3\
        Current Number 3 Previous Number  2  Sum:  5..\
        Current Number 9 Previous Number  8  Sum:  17"

print("Printing current and previous number sum in a range(10)")
privious_num = 0

for i in range(1, 10):

    sum = privious_num + i
    print("Current Number :", i, "Privious Number : ", privious_num, "Sum = ", sum)

    privious_num = i
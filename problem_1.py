"How to find avarage of N numbers in python"
 
num = int(input("How many numbers you have for calculate avg : "))
t_num = 0

for n in range (num):
    numbers = float(input("Enter Your numbers for avg : "))
    t_num += numbers

    avg = t_num / num

print ("Avarage is : ", avg)
"Given two integer numbers, write a python code to return their product only if the product is equal to \
or lower than 1000. otherwise, return their sum"

"Given 1 : number1 = 20, number2= 30, outpur = 600 || Given 2: num1 = 40, num2 = 30, output = 70"

num1 = int(input("number1 : "))
num2 = int(input("number2 : "))

def mul_or_sum (num1 , num2):
    
    product = num1 * num2

    if product <= 1000 :
        return product
    else:
        return num1 + num2
    
print("Output : ", mul_or_sum(num1,num2))
# Given two integer numbers, write a Python program to return their product. If the product is greater
# than 1000, then return their sum. Read inputs from the user.
num1,num2=input("Type numbers: ").split(",")
print("Num1= "+ num1)
print("Num2= "+ num2)
product=int(num1)*int(num2)
if(product>1000):  
    print(f"sum = {num1+num2}")
else:
    print(f"product= {product}")
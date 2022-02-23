# Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string. N must be less than the length of the string. Read inputs from the user. Do
# not use any built-in function.
string=input("Enter string: ")
n=int(input("Enter number: "))
a=""
for i in range(0,len(string)):
    if i>=n:
        a=a+string[i]
print(a)

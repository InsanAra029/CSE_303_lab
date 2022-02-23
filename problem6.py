#Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
#number based on the following assumptions.Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1
def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("Type n: "))
print(Fibonacci(n))
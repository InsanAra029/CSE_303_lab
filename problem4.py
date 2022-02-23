# Given a positive integer N (read from the user), write a Python program to calculate the value of the
# following series. 1^2 + 2^2 + 3^2 + 4^2+ ..... + N^2
N=int(input("Type n= "))
sum=(N*(N+1)*(2*N+1))/6
print(f"sum is: {sum}")
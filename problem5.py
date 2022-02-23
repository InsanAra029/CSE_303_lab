# Given a positive integer N (read from the user), write a Python program to check if the number is
# prime or not. Define a function named as prime_find_<your-student-id> in your program.
n=29
flag = False
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
if flag:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")
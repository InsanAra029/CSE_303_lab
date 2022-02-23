#Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
#the list. Do not use any built-in function.
total = 0
l= [1, 2, 3, 4, 5]
for i in range(0, len(l)):
    total = total + l[i]
print(f"list sum: {total}")
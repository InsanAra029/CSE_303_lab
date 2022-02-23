# Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
# smallest element of the list. Define two functions largest_number_<your-student-id> and
# smallest_number_<your-student-id> in your program. Do not use any built-in function.
list = [20,19,2,60,51]
def largest_number(num):
    max=num[0]
    for i in range(len(num)):
        if num[i] > max:
            max= num[i]
    print(f"largest: {max}")
     
def smallest_number(num):
    min= num[0]
    for i in range(len(num)):
        if num[i] < min:
             min = num[i] 
    print(f"Smallest: {min}")

largest_number(list)
smallest_number(list)

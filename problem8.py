# Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
# the even-indexed elements in the list.
list=[1,2,3,4]
sum= 0
for i in range(0, len(list)):
    if(i%2==0):
        sum = sum+list[i]
print(f"Sum: {sum}")

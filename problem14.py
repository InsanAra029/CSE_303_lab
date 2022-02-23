# Given a string, write a python program to check if it is palindrome or not. Define a function named
# palindrome_checker_<your-student-id> in your program.
def palindrome_checker_029(s):
    return s == s[::-1]
 
s = "ABCCBA"
result = palindrome_checker_029(s)
 
if result:
    print("Yes")
else:
    print("No")

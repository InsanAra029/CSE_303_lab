# Given a string, display only those characters which are present at an even index number. Read inputs
# from the user.
s=input("enter s: ")
for i in range (0,len(s),1):
    if(i%2==0):
        print(s[i])
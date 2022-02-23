# Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
# built-in function.
string ='CSE303 is a data science course.'
substring = 'CSE303'
c = 0
l=len(substring)
for i in range(len(string)):
    if string[i:i+l] == substring:
        c += 1
print (c)
# Given a two list of numbers (hardcoded in the program), create a new list such that new list should
# contain only odd numbers from the first list and even numbers from the second list.
list1=[1,2,3,4] 
list2=[5,6,7,8] 
odd=[]
even=[]
for i in range (0,len(list1)):
    if(list1[i]%2!=0):
        odd.append(list1[i])
for i in range (0,len(list2)):
    if(list2[i]%2==0):
        even.append(list2[i])
print(f"list3={odd+even}")

# 1
print ("This line will be printed.")
name = "John"
age = 23
print ("%s is %d years old." % (name, age))
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f'{name} is {age} years old')

# 2
print(2**52 <= 2**56 // 10 < 2**53)

# 3
x = 4
if (x < 1):
    score = "low"
elif (x <= 4): 
    score = "medium"
else:
    score = "high"
print (score)

x = True
if x:
    print ("it worked")

# 4
veggies = ["carrots", "broccoli", "beans"]
for veggie in veggies:
    print(veggie)
for veggie in veggies:
    if veggie == "broccoli":
        break
print(veggie)
for veggie in veggies:
    if veggie == "broccoli":
        continue
print(veggie)

# 5
Creating a list
x = [3, "hello", 1.2]
print (x)
# Creating a tuple
x = (3.0, "hello")
print (x)
# Sets
text = "SDS IN PYTHON"
print (set(text))
print (set(text.split(" "))
)

# 6
# Define the function
def add_two(x):
    x += 2
    print(x)
add_two(5)

def f(*args, **kwargs):
    y = args[0]
    z = kwargs.get("y")
    print (f"y: {y}, z: {z}")
f(5, y=2)
# 7
# Indexing
x = [3, "hello", 1.2]
print ("x[0]: ", x[0])
print ("x[1]: ", x[1])
print ("x[-1]: ", x[-1]) # the last item
print ("x[-2]: ", x[-2]) # the second to last item
# Slicing
print ("x[:]: ", x[:]) # all indices
print ("x[1:]: ", x[1:]) # index 1 to the end of the list
print ("x[1:2]: ", x[1:2]) # index 1 to index 2 (not including index 2)
print ("x[:-1]: ", x[:-1]) # index 0 to last index (not including last index)
# Indexing beyond length
print (x[:100])
print (len(x[:100]))

























































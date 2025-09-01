# get the numbers
x = int(input("Enter number for x: "))
y = int(input("Enter number for y: "))
z = int(input("Enter number for z: "))

# put the numbers into a list
numbers = [x, y, z]

# sort the list
numbers.sort()

# give the sorted values back to x, y, z
x = numbers[0]
y = numbers[1]
z = numbers[2]

# print them
print("x =", x)
print("y =", y)
print("z =", z)
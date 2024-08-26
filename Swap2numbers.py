#create variables a and b to contain user input values
a = input("Enter a number: ")
b = input("Enter another number: ")

#swap the values
c = a           #c is an extra variable that holds the value of a
a = b           #assign the value of b to a
b = c           #assign the value of c to b

print("a =" + a)
print("b =" + b)

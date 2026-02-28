# Length of a string
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word")

# String as an array
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:5])# Including 0 nut not 5. Counting the string like a array
print(fruit[:5]) # That's dosn't matter blank_:n number of string
print(fruit[0:4]) 
print(fruit[:5]) # That's dosn't matter blank_:n number of string
print(fruit[1:4]) # String count on 1 to n number of array index
print(fruit[0:-3]) # Pyhon understand [0:-3] that means [0:len(fruit)-3]
print(fruit[-3:-1])

# Loops through a String
alphabates = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabates:
    print(i)

# Quick Quiz:-
nm = "Harry"
print(nm[-4:-2])
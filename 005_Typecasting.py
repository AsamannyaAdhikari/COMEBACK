# How to Typecasting work
# There are two types of typecasting
# Explicit Conversion (Explicit type casting in python).
# Implicit Conversion (Implicit type casting in python).
# Suppose
a = "1"
a1 = 1
b = "2"
b1 = 2
# Because I put "". That's why the int value change force fully. It's called Explicit Conversion.
print(a + b)
print(int(a) + int(b)) # We mention it's not a 'str', it's 'int'.
# And it's as always mention a integer value. That's why it's Implicit Conversion.
print(a1 + b1)
# Another example of implicit casting
# suppose
c = 1.2
d = 8
print(c + d) # C is a float, and D is a int value. It's autoUnderstand what the data_type we put.
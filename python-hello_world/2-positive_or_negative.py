import random
number = random.randint(-10, 10)

print("The number is:", number)

if number > 0:
     print("is positive")
elif number==0:
     print("is zero")
elif number < 0:
     print("is negative")
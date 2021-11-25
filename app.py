import random
import math         # needed for gcd
array = []          # empty list  array == list

a = -100
b = 100
x = random.randint(a, b )  # Return a random integer a <= x <= b.

j = 0
n = 25                          # size of the array
while (j < n):                  # populate the array using the while loop
    x = random.randint(a, b )   # Return a random integer  a <= x <= b.
    array.append(x)             # appends to the array
    j = j + 1

print("The array is", len(array), "and is",array)        #  Print Array and Length

d = (sum(array) / len(array))   # Takes sum and divides it by count to generate avg
print("The average of the array is", d)

e = 0                   # variable for even numbers
o = 0                   # variable for odd numbers
for num in array:       # for loop that iterates through the array and populates even and odd
    if num % 2 == 0:    # calculation to determine if a number is odd or even
        e += 1
    else:
        o+=1
print("The number of even numbers is", e, "and the number of odd numbers is", o)

h = 0
l = 0
for num in array:       # deciding which numbers are above and below 0
    if num > 0:         # greater than/less than to populate h and l
        h +=1
    elif num < 0:
        l += 1

print("The number of integers above zero is", h, "and the number of integers below zero is", l)

m = len(array)//2       # finding which value is the median of the array
print("The median of the array is", array[m])

k = 0                   # variable for finding numbers greater than or equal to the median
j = 0                   # variable for finding numbers less than the median
for num in array:       # deciding which integers through the array are equal to or greater than, and integers less than
    if num >= array[m]:
        k += 1
    else:
        j += 1

print("The number of integers greater than or equal to the median is", k, "while the numbers less than the median are", j)

u = int(input("Type a number: "))       # requesting the user to enter an integer
t = 0                                   # variable for populating the count of a number the user inputted
for num in array:                       # populating t
    if num == u:
        t +=1
print("Your chosen number shows up", t, "times!")

r = max(array)          # using the max function to determine the highest integer
s = min(array)          # using the min function to determine the lowest integer
print("The highest number in the array is", r, "and the lowest number in the array is", s)

parray = sorted(array, reverse=True)        # sorting the array and reversing it so it is in descending order
print("The array sorted and reversed in order is", parray)

z = math.gcd(r, s)
print("The GCD of", r, "and", s, "is", z)
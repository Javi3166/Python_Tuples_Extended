#Tuple: ordered, immutable, allows duplicate elements

print("\nOriginal tuple.")
myTuple = ("Max", 28, "Boston")
print(myTuple)

print("\nTuple does not need parentheses.")
myTuple = "Max", 28, "Boston"
print(myTuple)

print("\nTuple needs a comma if there's only 1 element or it will not be considered a tuple even with parentheses.")
myTuple = ("Max")
print(myTuple)
print(type(myTuple))
myTuple = (28,)
print(myTuple)
print(type(myTuple))

print("\nIt's possible to create a tuple from an iterable, such as a list, using tuple().")
myTuple = tuple(["Max", 28, "Boston"])
print(myTuple)

print("\nAccessing an item is the same as with Lists.")
item = myTuple[0]
print(item)

print("\nAccessing an item is the same as with Lists, even using negative numbers to start from the end")
item = myTuple[-1]
print(item)

print("\nIt's possible to iterate over a tuple using a for loop.")
for index in myTuple:
    print(index)

print("\nIt's not possible to change certain elements in a tuple since a tuple is immutable. However, it is possible"
      " to reuse a variable name for a brand new tuple.")

print("\nIt's possible to check whether a certain item is in a tuple.")
if "Max" in myTuple:
    print("Yes")
else:
    print("No")

myTuple = ('a', 'p', 'p', 'l', 'e')

print("\nIt is possible to find the length of a tuple using len().")
print(len(myTuple))

print("\nIt is possible to count how many times a certain element is repeated in a tuple using .count().")
print(myTuple.count('p'))

print("\nIt is possible to find the index of the first instance of a certain element using .index().")
print(myTuple.index('l'))

print("\nIt is possible to convert a tuple into a list and vise-versa very easily using list() and tuple().")
myList = list(myTuple)
print(myList)
myTuple2 = tuple(myList)
print(myTuple2)

print("\nIt is possible to use slicing with tuples.")
myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(myTuple[2:5])
print(myTuple[:5])
print(myTuple[2:])

print("\nCan use slicing to print out every 2 or more element.")
print(myTuple[::2])

print("\nCan reverse the tuple using negative numbers with slicing.")
print(myTuple[::-2])

myTuple = "Max", 28, "Boston"

print("\nIt is possible to unpack a tuple into several variables as long as the amounts match.")
name, age, city = myTuple
print(name)
print(age)
print(city)

print("\nIt is possible to unpack multiple elements into 1 variable using *, but they will be turned into a list.")
myTuple = 1, 2, 3, 4, 5
i1, *i2, i3 = myTuple
print(i1)
print(i3)
print(i2)

print("\nEven if they have the same elements, a tuple is smaller than a list.")
import sys
myTuple = 0, 1, 2, "hello", True
myList = [0, 1, 2, "hello", True]
print(sys.getsizeof(myTuple), "bytes")
print(sys.getsizeof(myList), "bytes")

print("\nA tuple is also faster to create than a list.")
import timeit
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
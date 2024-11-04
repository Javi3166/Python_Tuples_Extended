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
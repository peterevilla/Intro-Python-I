# print "Hello, world!"
print("Hello, world!")
# create an empty list
p = [] 
# create a list with some numbers
q = [10, 60, 20, 5] 
# add an element to p
p.append(77)
# print all values in each list
for e in p:
    print(e)
for (i, e) in enumerate(q):
    print(f'Element {i} is {e}') 
# using list comprehensions...
# create a new list containing the squares of all values in `numbers`
numbers = [1, 2, 3, 4, 5]
print(numbers)
squares = [num*num for num in numbers]
squares = []
for num in numbers:
    squares.append( num*num ) 
# create a new list containing only the even values of `numbers`
evens = [num for num in numbers if num % 2 == 0 ]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)
# create a new list containing only the names that start with `s` so that they are properly capitalized (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)
# create an empty dictionary
d = {}
# create a dictionary with at least two key : value pairs
e = {"foo": 12, "bar": 20}
# access & print an element in the dictionary
print(e["bar"])
# iterate through dictionary
for k in e:
    print(f'{k} is {e[k]}')
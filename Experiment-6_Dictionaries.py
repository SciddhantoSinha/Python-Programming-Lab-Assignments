# Task-1
# list into dictionary
print("=" * 100)
print("\nTask A\n")
print("\nList into Dictionary\n")

l1 = ["A", "B", "C", "D", "E"]
l2 = [1, 2, 3, 4, 5]

print("1st List is :: ", l1)
print("2nd List is :: ", l2)

res = dict(zip(l1, l2))
print("The new Dictionary formed using list 1 and 2 is :: ", res)


# dictionary to lists
print("\nDictionary to Lists\n")

x = {1: 'A', 2: 'B', 3: 'C'}
x.items()

lst = list(x.items())
print(lst)

lst1 = list(x.values())
print(lst1)

lst2 = list(x.keys())
print(lst2)


# Task 2
print("=" * 100)
print("\nTask B")

num = int(input("\nEnter Number :: "))
d = dict()

for i in range(1, num + 1):
    d[i] = i ** 2

print(
    "The dictionary with the format as key = number and value = number ** 2 :: ",
    d
)


# Task 3
print("=" * 100)
print("\nTask C\n")

movie = {
    'ABCD': '13:00',
    'EFGH': '15:00',
    'XYZ': '17:00',
    'PQRS': '21:00'
}

print(movie)

# 1. Add
print("\n1. Add")

key = str(input("\nEnter the movie you want to add (Name only):: "))
val = str(input("\nEnter the Time of the movie you want to add (in 24Hr):: "))

movie[key] = val
print(movie)


# 2. Display movies at 9pm
print("\n2. Display movies at 9pm")

dis = str(input('\nThe time at which you want to watch the movie :: '))
value = {i for i in movie if movie[i] == dis}
print(value)


# 3. Remove details of a movie
print("\n3. Remove details of a movie")

rem = str(input('\nEnter the movie you want to delete :: '))
movie.pop(rem)

print(movie)


# 4. Remove last movie
print("\n4. Remove last movie")
print('\nAfter deleting last movie in dictionary :: ')

movie.popitem()
print(movie)

# Task A
print("=" * 150)
print("\nTask A\n")

str_lst = ["MIT", "SOE", "MIT", "ADTU", "ADT", "Loni", "Design", "Food", "Technology"]
print("The list of string is :: ", str_lst)

check_str = str(input("Enter string element to check :: "))
count = 0

for x in str_lst:
    if x == check_str:
        count += 1

print("{} has occurred {} times in the given list ".format(check_str, count))


# Task B
print("=" * 150)
print("\nTask B\n")

int_lst = [100, 35, 23, 100, 45, 89, 90]
print("The list of integer is :: ", int_lst)

check_int = int(input("Enter integer element to check :: "))
count_int = 0

for y in int_lst:
    if y == check_int:
        count_int = count_int + 1

print("{} has occurred {} times in the given list ".format(check_int, count_int))


# Task C
print("=" * 150)
print("\nTask C\n")

def test(lst):
    if len(lst) <= 10:
        print("List length is not more than 10")
    elif lst.count(lst[2]) >= 2:
        print(
            "List has length more than 10 and {} occurs 2 or more times".format(
                lst[2]
            )
        )
    else:
        print("ERROR!!")

lst = []
n = int(input("Number of elements in array :: "))
lst = []

for i in range(0, n):
    enter = int(input("Enter List Contents :: "))
    lst.append(enter)

print("Original list :: ")
print(lst)

print(
    "Check whether the length of the said list is 10 and third element occurs twice in the said list. :: "
)
print(test(lst))


# Task D
print("=" * 150)
print("\nTask D\n")

int_lst.sort()
print("The sorted list of integers is :: ", int_lst)

print("=" * 150)
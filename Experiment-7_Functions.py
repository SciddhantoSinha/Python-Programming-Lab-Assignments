# 1. Find the max of three numbers
def max_of_3():
    a = int(input("Enter the value of a"))
    b = int(input("Enter the value of b"))
    c = int(input("Enter the value of c"))

    if a > b and a > c:
        print("a is greater")
    elif b > a and b > c:
        print("b is greater")
    elif c > a and c > b:
        print("c is greater")
    else:
        print("All three numbers all equal")


def list_mul():
    n = int(input("Enter the number of element you want in the list :: "))
    i = 0
    l1 = []

    for i in range(0, n):
        element = int(input("Enter the element:"))
        l1.append(element)

    print("List entered by you is: ")
    print(l1)

    mult = 1
    for i in range(0, n):
        mult = mult * l1[i]

    print("Multiplication of the elements of the List is ", mult)


def even_num():
    l2 = []

    for i in range(19, 89):
        if i % 2 == 0:
            l2.append(i)

    print("Even numbers between 19 and 88 are :")
    print(l2)


def date_time():
    import datetime
    current_time = datetime.datetime.now()
    print("date and time are:", current_time)

    import sys
    print("Python version: ", sys.version)


def menu():
    print(
        "1.Max of three numbers \n"
        "2. Multiply numbers within a list\n"
        "3.Make a list of all even numbers between 18 and 88 \n"
        "4.Print current time date and version of python \n"
        "0.Exit"
    )


menu()
option = int(input("Enter the option number :"))

while option != 0:

    if option == 1:
        max_of_3()

    elif option == 2:
        list_mul()

    elif option == 3:
        even_num()

    elif option == 4:
        date_time()

    menu()
    option = int(input("Enter the option number :"))

print("Exiting. ........... ")

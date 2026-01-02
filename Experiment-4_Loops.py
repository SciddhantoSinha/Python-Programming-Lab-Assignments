a = []
b = []
c = []
d = []
prime = []

n1 = int(input("Min number :: "))
n2 = int(input("Max number :: "))

inputnum = int(input("""
Enter 2 for displaying the Array,
Enter 3 for finding if array is divisible by both 5 & 9,
Enter 4 for Getting Even and Odd numbers from the array,
Enter 5 for getting Prime numbers from the array
:: """))

if inputnum == 2:
    for i in range(n1, n2):
        a.append(i)
    print("The array between min to max value is :: ", a)

elif inputnum == 3:
    for j in range(n1, n2):
        if j % 45 == 0:
            b.append(j)
    print("Elements from array divisible by 5 & 9 are :: ", b)

elif inputnum == 4:
    for k in range(n1, n2):
        if k % 2 == 0:
            c.append(k)
        else:
            d.append(k)
    print("even number are ", c)
    print("odd number are ", d)

elif inputnum == 5:
    for num in range(n1, n2):
        if num > 1:
            for chk in range(2, num):
                if num % chk == 0:
                    break
            else:
                prime.append(num)
    print("List of prime numbers are :: ", prime)

else:
    print("Invalid Choice")


b = []
c = []
d = []
prime = []

def menu():
    print()
    print("==================================================================================")
    print("Enter 1 for Inputting max & min")
    print("Enter 2 for displaying the Array")
    print("Enter 3 for finding if array is divisible by both 5 & 9")
    print("Enter 4 for Getting Even and Odd numbers from the array")
    print("Enter 5 for getting Prime numbers from the array")
    print("Enter 0 to Exit")
    print("==================================================================================")
    print()

menu()
choice = int(input("Enter Your Choice :: "))

while choice != 0:

    if choice == 1:
        n1 = int(input("Min number :: "))
        n2 = int(input("Max number :: "))

    elif choice == 2:
        a = []
        for i in range(n1, n2):
            a.append(i)
        print("The array between min to max value is :: ", a)

    elif choice == 3:
        b = []
        for j in range(n1, n2):
            if j % 45 == 0:
                b.append(j)
        print("Elements from array divisible by 5 & 9 are :: ", b)

    elif choice == 4:
        c = []
        d = []
        for k in range(n1, n2):
            if k % 2 == 0:
                c.append(k)
            else:
                d.append(k)
        print("even number are :: ", c)
        print("odd number are :: ", d)

    elif choice == 5:
        prime = []
        for num in range(n1, n2):
            if num > 1:
                for chk in range(2, num):
                    if num % chk == 0:
                        break
                else:
                    prime.append(num)
        print("List of prime numbers are :: ", prime)

    else:
        print("Invalid Choice")

    menu()
    choice = int(input("Enter Your Choice :: "))

print("Exiting!!!!!!!!")

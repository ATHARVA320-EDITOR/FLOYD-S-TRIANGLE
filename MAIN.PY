height = int(input("Enter the height of triangle: "))
number = 1
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number = number + 1
    print()

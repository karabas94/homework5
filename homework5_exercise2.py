height = int(input("Enter altitude of triangle:"))

print("Triangle 2")
for h in range(height):                    # перебор строк
    for i in range(h):                     # печать пробелов в строке
        print(" ", end=" ")
    for j in range(h, height):             # печать звездочек в строке
        print("*", end=" ")
    for w in range(h, height-1):           # печать пробелов в строке
        print("*", end=" ")
    print()                                # окончание строки
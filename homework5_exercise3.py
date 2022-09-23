height = int(input("Enter altitude of triangle:"))

print("Triangle 3")
for h in range(height):               # перебор строк
    for i in range(h, height):
        print(" ", end=" ")           # печать пробелов в строке
    for j in range(h):
        print("*", end=" ")           # печать звездочек в строке
    print()                           # окончание строки
for h in range(height):               # перебор строк
    for j in range(h):
        print(" ", end=" ")           # печать пробелов в строке
    for i in range(h, height):
        print("*", end=" ")           # печать звездочек в строке
    print()                           # окончание строки
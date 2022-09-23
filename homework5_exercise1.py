height = int(input("Enter altitude of triangle:"))

print("Triangle 1")
for h in range(height):              # перебор строк
    for i in range(h):               # печать звездочек в строке
        print("*", end=" ")
    print()                          # окончание строки
for h in range(height):              # перебор строк
    for j in range(h, height):       # печать звездочек в строке
        print("*", end=" ")
    print()                          # окончание строки
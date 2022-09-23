height = int(input("Enter altitude of triangle: "))

print("Triangle A")
for h in range(height):                           # перебор строк
    for i in range(h, height-1):
        print(" ", end=" ")                       # печать пробелов в строке
    for w in range(h):
        if w + h == h or h == height - 1:
            print("*", end=" ")                   # печать звездочек в строке через условие
        else:
            print(" ", end=" ")                   # печать пробелов в строке (в треугольнике)
    for j in range(h + 1):
        if h == j or h == height - 1:
            print("*", end=" ")                   # печать звездочек в строке через условие
        else:
            print(" ", end=" ")                   # печать пробелов в строке (в треугольнике)
    print()                                       # окончание строки
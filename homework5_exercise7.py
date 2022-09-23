height = int(input("Enter altitude of triangle: "))

print("Double triangle С")
for h in range(height):                      # перебор строк
    for i in range(h, height - 1):
        print(" ", end=" ")                  # печать пробелов в строке
    for w in range(h + 1):
        print("*", end=" ")                  # печать звездочек в строке
    for j in range(h):
        print("*", end=" ")                  # печать звездочек в строке
    print()                                  # окончание строки
for h in range(height):                      # перебор строк
    for i in range(h + 1):
        print(" ", end=" ")                  # печать пробелов в строке
    for w in range(h, height - 1):
        if w == h:
            print("*", end=" ")              # печать звездочек в строке через условие
        else:
            print(" ", end=" ")              # печать пробелов ввнутри треугольника
    for j in range(h, height - 2):
        if j == height - 3:
            print("*", end=" ")              # печать звездочек в строке через условие
        else:
            print(" ", end=" ")              # печать пробелов ввнутри треугольника
    print()                                  # окончание строки

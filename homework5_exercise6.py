height = int(input("Enter altitude of triangle: "))

print("Triangle B")
for h in range(height):                      # перебор строк
    for i in range(h, height-1):
        print(" ", end=" ")                  # печать пробелов в строке
    for w in range(h):
        print("*", end=" ")                  # печать звездочек в строке
    for j in range(h + 1):
        print("*", end=" ")                  # печать звездочек в строке
    print()                                  # окончание строки
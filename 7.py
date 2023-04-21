def draw_tree(level):
    for i in range(1, level + 1):  
        for j in range(level - i):
            print(" ", end = "")

        for j in range(2 * i - 1):
            print("*", end="")
            # Move to the next line

        print()
    print('   |')

LEVEL = 4
number = int(input("Введите число елок: "))
for i in range(number):
    draw_tree(LEVEL)
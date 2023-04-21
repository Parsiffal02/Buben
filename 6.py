number=int(input())
numbers = [int(input()) for i in range(number)]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
print("Максимальное число в списке:", max_number)
print("Номер элемента максимального числа в списке:", *[i+1 for i in range(len(numbers)) if numbers[i]==max_number] if [i for i in range(len(numbers)) if numbers[i]==max_number] else '')

#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
counter = 1
number_list = []
while counter < 11:
    number_list.append(int(input("Write a number")))
    counter = counter + 1
print(number_list)
highest = number_list[0]
for number in number_list:
    if number > highest:
        highest = number

print("The highest number is:", highest)
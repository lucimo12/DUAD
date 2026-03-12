#Intente accesar a una variable global desde una función y cambiar su valor.

number_sum = 9

def number():
    global number_sum
    number_sum = 4
    print("The total is:", number_sum)

number()
print(number_sum)
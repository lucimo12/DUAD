
#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
name = input("What's your name?")
last_name = input("What's your last name?")
age = int(input("What's your age?"))
if (age < 5 ):
    print("Baby")
elif (age < 12):
    print("Kid")
elif(age < 18 ):
    print("Teenager")
elif(age < 30):
    print("Young adult")
elif(age < 60):
    print("Adult")
else:
    print("Elderly")



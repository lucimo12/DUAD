#Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#“I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

text = "I love Nacion Sushi"

def string_info(text):
    upper_cases = 0 #tienen que ir como variables locales 
    lower_cases = 0
    for x in text: 
        if x.isupper():
            upper_cases += 1
        elif x.islower():
            lower_cases += 1
    print("There's",upper_cases,"upper cases and ",lower_cases,"lower cases")
string_info(text)

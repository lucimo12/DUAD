#Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”
text_original = "python-variable-funcion-computadora-monitor"

def string_order(text):
    words = text.split("-")
    order = sorted(words)
    result = "-".join(order)  
    return result

print(string_order(text_original))
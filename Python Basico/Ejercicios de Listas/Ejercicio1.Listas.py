#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]
#second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for i in range(len(first_list)): # 'i' represents the index position.The loop runs from 0 to the length of the list.
    print(f"{i}: {first_list[i]}, {second_list[i]}") #{i} prints the current index.
# {first_list[i]} prints the element of the first list at index i.
# {second_list[i]} prints the element of the second list at index i.

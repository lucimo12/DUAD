#Analice el algoritmo de bubble_sort usando la Big O Notation.

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):       #O(n2)
        for j in range(n - 1):   #2 for anidados 
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



numeros = [5, 3, 8, 2]
print(bubble_sort(numeros))


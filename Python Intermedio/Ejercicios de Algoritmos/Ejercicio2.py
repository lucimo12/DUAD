#Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr



numeros = [5, 3, 8, 2]
print(bubble_sort(numeros))
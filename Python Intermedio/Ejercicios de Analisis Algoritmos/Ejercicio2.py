#Analice los siguientes algoritmos usando la Big O Notation:

#Fijarme en el número de for anidados para saber potencia de n.
#La excepción es cuando el for tiene un límite fijo, que lo convierte en O(1).



#print_numbers_times_2

def print_numbers_times_2(numbers_list):
	for number in numbers_list: # un solo for, O(n)
		print(number * 2)

#check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b: # for dentro de for (On2)
			if element_a == element_b:
				return True
				
	return False

#print_10_or_less_elements

def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)): #numero de iteraciones es constante, no pasa de 10
		print(list_to_print[index])        #O(1)

#generate_list_trios

def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:        #tres for anidados 
			for element_c in list_c:    #O(n3)
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 
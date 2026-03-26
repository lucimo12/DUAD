#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def numbers_only(func):
    def wrapper(*args, **kwargs):
        for arg in args[1:]:  
            if not isinstance(arg, (int, float)):
                raise Exception("All parameters must be numbers")

        result = func(*args, **kwargs)
        return result

    return wrapper

class Store():
    
    def __init__(self, product, price):
        self.product = product
        self.price = price
    
    @numbers_only    
    def calculate_discount(self, price):
        if price <= 100:
            discount = 10
            total = price - 10 
        else:
            discount = 40
            total = price - 40
        return total
    
store1 = Store("Book", 30)
total = store1.calculate_discount(30)
print("The total with the discount is: ", total)
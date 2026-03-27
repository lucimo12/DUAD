#Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

def numbers_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise Exception("All parameters must be numbers")

        for value in kwargs.values():
            if not isinstance(value, (int, float)):
                raise Exception("All parameters must be numbers")

        return func(*args, **kwargs)
    return wrapper


@numbers_only
def calculate_discount(price):
    if price <= 100:
        return price - 10
    else:
        return price - 40


print("The total with the discount is:", calculate_discount(30))
#Cree un decorador que haga print de los parámetros y retorno de la función que decore.
def sugar(func):
    def wrapper(*args, **kwargs):
        print("Parameters:", args, kwargs)

        result = func(*args, **kwargs)

        print(result)
        return result

    return wrapper


class Coffee():
    def __init__(self, name):
            self.name = name


    @sugar
    def add_sugar(self):
        return f"Adding sugar to {self.name}"
        

coffee1 = Coffee("latte")
coffee1.add_sugar()


#Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def show_name():
    print("Mi nombre es Lucia")

    
def show_age():
    print("Mi edad es 24")
    show_name()
show_age()
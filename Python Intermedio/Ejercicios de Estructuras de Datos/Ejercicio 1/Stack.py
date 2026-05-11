#Cree una estructura de objetos que asemeje un Stack.
#Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node():
    def __init__(self, value):
        self.value = value
        self. next = None #apunta al siguiente nodo
        
    
class Stack():
    def __init__(self):
        self.top = None #top : primer nodo : cima
        
    
    def push(self, value):
        new_node = Node(value)
        
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top == None:
            print("Stack is empty")
            return None
        
        removed = self.top
        self.top = self.top.next
        return removed.value  
    
    def print_stack(self):
        current = self.top
        
        while current is not None:
            print(current.value)
            current = current.next
            
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:")
stack.print_stack()

print("Pop:", stack.pop())

print("Stack after pop:")
stack.print_stack()
    
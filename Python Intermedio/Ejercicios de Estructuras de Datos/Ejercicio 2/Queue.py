#Cree una estructura de objetos que asemeje un Double Ended Queue.
#Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio y al final) y pop_left y pop_right (para quitar nodos al inicio y al final).
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None #crear nodo vacío y luego conectarlo
        self.prev = None
        
class DeQueue():
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def push_left(self, value):
        new_node = Node(value)  #crear el nodo
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #el nuevo nodo apunta al head actual
            self.head.prev = new_node #el head actual apunta hacia atrás al nuevo nodo
            self.head = new_node #ahora el nuevo nodo se vuelve el nuevo head
            
    def push_right(self,value):
        new_node = Node(value)
        
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def pop_left(self): #no lleva value porque va a quitar elemento
        if self.head is None:
            print("Queue is empty")
            return None
        
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None  
        
        return removed_value
    
    def pop_right(self):
        if self.tail is None:  
            print("Queue is empty")
            return None
        
        removed_value = self.tail.value
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        return removed_value
    
    def print_dequeu(self):
        current = self.head
        
        while current is not None:
            print(current.value)
            current = current.next
            
DeQueue = DeQueue()
DeQueue.push_left(10)
DeQueue.push_left(5)
DeQueue.push_right(20)
DeQueue.push_right(30)

print("DeQueu:")
DeQueue.print_dequeu()

print("pop_left:", DeQueue.pop_left())
print("pop_right:", DeQueue.pop_right())

print("DeQueue after pops:")
DeQueue.print_dequeu()
#Cree una estructura de objetos que asemeje un Binary Tree.
#Debe incluir un método para hacer print de toda la estructura.
#No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node():
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None 
        
class BinaryTree():
    def __init__(self):
        self.root = None #primer nodo, la raiz del arbol
        
    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            print(node.value)
            self._print_tree(node.left)
            self._print_tree(node.right)
            
tree = BinaryTree()

tree.root = Node(10)
tree.root.left = Node(5)
tree.root.right = Node(20)
tree.root.left.left = Node(3)
tree.root.left.right = Node(7)
tree.root.right.right = Node(30)

tree.print_tree()
        
    
        
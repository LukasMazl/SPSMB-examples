# Vytvoř linkedlist, ve kterém půjde
#   vytvoř třídu pro uzle, ve které bude
#       obsah
#       odkaz na další node
# vytvořit třídu linkedlistu, ve kterém následně
# Vytvoříte instanci
# Po zavolání metody vloží na konec linkedlistu nový node s obsahem
# na poslední node dá odkaz na nově vytvořený
# Po zavolání metody vypíše celý obsah linkedlistu


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
    
    def add_value(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return
    
        current_node = self.root
        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
    
    def print_list(self):
        current_node = self.root

        while current_node:
            print(current_node.value)
            current_node = current_node.next

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.add_value(50)
    linked_list.add_value("pepa")
    linked_list.add_value(["ahoj"])
    linked_list.add_value({"ahoj": "pepo"})

    linked_list.print_list()
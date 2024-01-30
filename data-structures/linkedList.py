class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self) -> str:
        return str(self.data)
        
class LinkedList:
    def __init__(self):
        self.head = None         
        self.size = 0   
            
    def insertAtBegin(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, data, index):
        node = Node(data)
        
        current_node = self.head
        current_index = 0
        
        if current_index == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and current_index+1 != index):
                current_index = current_index+1
                current_node = current_node.next
 
            if current_node != None:
 
                node.next = current_node.next
                current_node.next = node
                self.size += 1
            else:
                raise IndexError("Index out of range")
        
    def append(self, data):
        self.size +=1
        node = Node(data)
        if self.head is None:
            self.head = node
            return
    
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
    
        current_node.next = node

        
    def search(self, data):
        current = self.head
        while current != None and current.data != data:
            current = current.next
        return current
    
    def remove(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        current_index = 0
        
        if current_index == index: # Removing the first element
            if self.head is None:
                    return
        
            current_node = self.head
            while(current_node.next.next):
                current_node = current_node.next
        
            current_node.next = None
            self.size -= 1
            
        else:
            while current_node != None and current_index+1 != index:
                current_index = current_index+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
                self.size -= 1
            else:
                raise IndexError("Index out of range")
    
    def __str__(self) -> str:
        res = "["
        flag = True
        
        current = self.head
        
        while current:
            if flag:
                res += str(current.data)
                flag = False
            else:
                res += ", " + str(current.data)
            current = current.next
        return res + "]"
    
    
if __name__ == '__main__':
    import rand_arr_gen
    
    random_array = rand_arr_gen.random_list(10,0,50)
    
    linked_list = LinkedList()
    for i in random_array:
        linked_list.append(i)
        
    print("Linked List:", linked_list)
    
    item = random_array[5]
    print("Search result:", linked_list.search(item))
    
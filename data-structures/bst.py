class BSTNode:
    def __init__(self, key, value) -> None:
        self.p = None
        self.l = None
        self.r = None
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"node: [key: {self.key}, value: {self.value}]"
    
class BST:
    def __init__(T):
        T.root = None

    def preorder_walk(T, x: BSTNode):
        if x != None:
            print(x)
            T.preorder_walk(x.l) # recursive call on the left
            T.preorder_walk(x.r) # recursive call on the right

    def inorder_walk(T, x: BSTNode):
        if x != None:
            T.inorder_walk(x.l) # recursive call on the left
            print(x)
            T.inorder_walk(x.r) # recursive call on the right

    def postorder_walk(T, x: BSTNode):
        if x != None:
            T.postorder_walk(x.l) # recursive call on the left
            T.postorder_walk(x.r) # recursive call on the right
            print(x)
    
    def tree_search(T, key):
        x = T.root
        while x.key != key:
            if key < x.key: x = x.l
            else: x = x.r
        return x
    
    @staticmethod
    def tree_min(x: BSTNode):
        while x.l != None:
            x = x.l
        return x

    @staticmethod
    def tree_max(x: BSTNode):
        while x.r != None:
            x = x.r
        return x
    
    @staticmethod
    def tree_successor(x: BSTNode):
        if x.r != None:
            return BST.tree_min(x.r)
        else:
            while x.p != None and x == x.p.r:
                x = x.p
            return x.p
        
    @staticmethod
    def tree_predecessor(x: BSTNode):
        if x.l != None:
            return BST.tree_max(x.l)
        else:
            while x.p != None and x == x.p.l:
                x = x.p
            return x.p    
        
    def tree_insert(T, z):
        x = T.root
        y = None
        while x != None:
            y = x
            if z.key <= x.key: x = x.l
            else: x = x.r 
        if y == None:
            T.root = z
        elif z.key <= y.key: y.l = z
        else: y.r = z
        z.p = y

    def transplant(T, u, v):
        if u.p == None: 
            T.root = v
        elif u.p.l == u:
            u.p.l = v
        else:
            u.p.r = v
        if v != None: 
            v.p = u.p 

    def tree_delete_first_approach(T, z):
        if z.l == None:
            T.transplant(z, z.r)
        elif z.r == None:
            T.transplant(z, z.l)
        else:
            y = BST.tree_successor(z)
            if y != z.r:
                T.transplant(y, y.r)
                y.r = z.r
                z.r.p = y
            T.transplant(z, y)
            y.l = z.l
            z.l.p = y

    def tree_delete_second_approach(T, z):
        if z.l != None:
            y = BST.tree_predecessor(z)
            temp = z
            z.key, z.value = y.key, y.value
            y.key, y.value = temp.key, temp.value
            T.tree_delete(y)
        elif z.r != None:
            y = BST.tree_successor(z)
            temp = z
            z.key, z.value = y.key, y.value
            y.key, y.value = temp.key, temp.value
            T.tree_delete(y)
        else:
            if z.p == None:
                T.root = None
            elif z.p.l == z:
                z.p.l = None
            else:
                z.p.r = None

    def left_rotate(T, x):
        y = x.r
        x.r = y.l
        if y.l:
            y.l.p = x
        y.p = x.p
        if x.p == None:
            T.root = y
        elif x.p.l == x:
            x.p.l = y
        else:
            x.p.r = y
        y.l = x
        x.p = y
        

    def right_rotate(T, x):
        y = x.l
        x.l = y.r
        if y.r:
            y.r.p = x
        y.p = x.p
        if x.p == None:
            T.root = y
        elif x.p.l == x:
            x.p.l = y
        else:
            x.p.r = y
        y.r = x
        x.p = y
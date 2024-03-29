import random

class TreapNode:
    def __init__(node, key, value) -> None:
        node.p = None
        node.l = None
        node.r = None
        node.key = key
        node.value = value
        node.priority = random.randint(0, 10 ** 8)

    def __str__(node) -> str:
        return f"node -> key: {node.key}, value: {node.value}, priority: {node.priority}"
    
class Treap:
    def __init__(T):
        T.root = None

    def preorder_walk(T, x: TreapNode):
        if x != None:
            print(x)
            T.preorder_walk(x.l) # recursive call on the left
            T.preorder_walk(x.r) # recursive call on the right

    def inorder_walk(T, x: TreapNode):
        if x != None:
            T.inorder_walk(x.l) # recursive call on the left
            print(x)
            T.inorder_walk(x.r) # recursive call on the right

    def postorder_walk(T, x: TreapNode):
        if x != None:
            T.postorder_walk(x.l) # recursive call on the left
            T.postorder_walk(x.r) # recursive call on the right
            print(x)
    
    def tree_search(T, key):
        x = T.root
        while x != None and x.key != key:
            if key < x.key: x = x.l
            else: x = x.r
        return x
    
    @staticmethod
    def tree_min(x: TreapNode):
        while x.l != None:
            x = x.l
        return x

    @staticmethod
    def tree_max(x: TreapNode):
        while x.r != None:
            x = x.r
        return x
    
    @staticmethod
    def tree_successor(x: TreapNode):
        if x.r != None:
            return Treap.tree_min(x.r)
        else:
            while x.p != None and x == x.p.r:
                x = x.p
            return x.p
        
    @staticmethod
    def tree_predecessor(x: TreapNode):
        if x.l != None:
            return Treap.tree_max(x.l)
        else:
            while x.p != None and x == x.p.l:
                x = x.p
            return x.p    
        
    def treap_fixup(T, z):
        if z.p != None:
            if z.priority > z.p.priority:
                if z == z.p.l:
                    T.right_rotate(z.p)
                else:
                    T.left_rotate(z.p)
                T.treap_fixup(z)
        
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
        T.treap_fixup(z)

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
            y = Treap.tree_successor(z)
            if y != z.r:
                T.transplant(y, y.r)
                y.r = z.r
                z.r.p = y
            T.transplant(z, y)
            y.l = z.l
            z.l.p = y

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

# TREAP - MAIN
T = Treap()
for i in range(5, 16):
    # Checking insertion
    T.tree_insert(TreapNode(key= i, value= i))

# Checking preorder walk
print(f"pre order traversal of the tree after inserting keys from range 1 to 10: {T.preorder_walk(T.root)}")

# Checking Min and Max
print(f"Min of the tree: {T.tree_min(T.root)}, Max of the tree: {T.tree_max(T.root)}")

# Checking Search, Predecessor, Successor
node = T.tree_search(5.5)
if node != None: print("5.5 exists in the tree")
else: print("5.5 doesn't exist in the tree")

node = T.tree_search(6)
if node != None: 
    print("6 exists in the tree")
    print(f"predecessor of 6: {Treap.tree_predecessor(node)}, successor of 6: {Treap.tree_successor(node)}")
else: print("6 doesn't exist in the tree")

# Checking Delete, Rotations, Transplant, Fixup
T.tree_delete_first_approach(node)
print(f"inorder traversal of the tree after deletion of 6: {T.inorder_walk(T.root)}") 

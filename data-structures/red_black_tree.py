class RBNode:
    def __init__(node, key, value):
        node.p = None
        node.l = None
        node.r = None
        node.key = key
        node.value = value
        node.is_red = True

    def __str__(node) -> str:
        return f"node -> key: {node.key}, value: {node.value}, is red?: {node.is_red}"
    
class RBTree:
    def __init__(T):
        T.nil = RBNode(None, None)
        T.nil.is_red = False
        T.root = T.nil

    def preorder_walk(T, x: RBNode):
        if x != T.nil:
            print(x)
            T.preorder_walk(x.l) # recursive call on the left
            T.preorder_walk(x.r) # recursive call on the right

    def inorder_walk(T, x: RBNode):
        if x != T.nil:
            T.inorder_walk(x.l) # recursive call on the left
            print(x)
            T.inorder_walk(x.r) # recursive call on the right

    def postorder_walk(T, x: RBNode):
        if x != T.nil:
            T.postorder_walk(x.l) # recursive call on the left
            T.postorder_walk(x.r) # recursive call on the right
            print(x)
    
    def tree_search(T, key):
        x = T.root
        while x != T.nil and x.key != key:
            if key < x.key: x = x.l
            else: x = x.r
        return x
    
    @staticmethod
    def tree_min(x: RBNode, nil):
        while x.l != nil:
            x = x.l
        return x

    @staticmethod
    def tree_max(x: RBNode, nil):
        while x.r != nil:
            x = x.r
        return x
    
    @staticmethod
    def tree_successor(x: RBNode, nil):
        if x.r != nil:
            return RBTree.tree_min(x.r, nil)
        else:
            while x.p != nil and x == x.p.r:
                x = x.p
            return x.p
        
    @staticmethod
    def tree_predecessor(x: RBNode, nil):
        print(f"finding pred of {x}")
        if x.l != nil:
            print(f"l is {x.l}")
            return RBTree.tree_max(x.l, nil)
        else:
            while x.p != nil and x == x.p.l:
                x = x.p
            return x.p 

    def rb_insert_fixup(T, z):
        while z.p.is_red:
            if z.p == z.p.p.l:
                y = z.p.p.r

                if y.is_red:
                    z.p.p.is_red = True
                    z.p.is_red = False
                    y.is_red = False
                    z = z.p.p
                else:
                    if z != z.p.l:
                        RBTree.left_rotate(z.p)
                        z = z.p 
                    z.p.p.is_red = True
                    z.p.is_red = False
                    RBTree.right_rotate(T, z.p.p)

            else:
                y = z.p.p.l

                if y.is_red:
                    z.p.p.is_red = True
                    z.p.is_red = False
                    y.is_red = False
                    z = z.p.p
                else:
                    if z != z.p.r:
                        RBTree.right_rotate(z.p)
                        z = z.p 
                    z.p.p.is_red = True
                    z.p.is_red = False
                    RBTree.left_rotate(T, z.p.p)
        T.root.is_red = False
        
    def tree_insert(T, z):
        x = T.root
        y = T.nil
        while x != T.nil:
            y = x
            if z.key <= x.key: x = x.l
            else: x = x.r 
        if y == T.nil:
            T.root = z
        elif z.key <= y.key: y.l = z
        else: y.r = z
        z.p = y
        z.l = T.nil
        z.r = T.nil
        T.rb_insert_fixup(z)

    def transplant(T, u, v):
        if u.p == T.nil: 
            T.root = v
        elif u.p.l == u:
            u.p.l = v
        else:
            u.p.r = v
        if v != T.nil: 
            v.p = u.p 
            
    def rb_delete_fixup(T, x):
        while x != T.root and not x.is_red:
            if x == x.p.l:
                s = x.p.r
                if s and s.is_red:
                    s.is_red = False
                    x.p.is_red = True
                    RBTree.left_rotate(T, x.p)
                    s = x.p.r
                if s and s.l and s.r and not s.l.is_red and not s.r.is_red:
                    s.is_red = True
                    x = x.p
                else:
                    if s and s.l and not s.l.is_red:
                        s.l.is_red = False
                        s.is_red = True
                        RBTree.right_rotate(T, s)
                        s = x.p.r
                    if s:
                        s.is_red = x.p.is_red
                        x.p.is_red = False
                        if s.r:
                            s.r.is_red = False
                        RBTree.left_rotate(T, x.p)
                        x = T.root
            else:
                s = x.p.l
                if s and s.is_red:
                    s.is_red = False
                    x.p.is_red = True
                    RBTree.right_rotate(T, x.p)
                    s = x.p.l
                if s and s.l and s.r and not s.l.is_red and not s.r.is_red:
                    s.is_red = True
                    x = x.p
                else:
                    if s and s.r and not s.r.is_red:
                        s.r.is_red = False
                        s.is_red = True
                        RBTree.left_rotate(T, s)
                        s = x.p.l
                    if s:
                        s.is_red = x.p.is_red
                        x.p.is_red = False
                        if s.l:
                            s.l.is_red = False
                        RBTree.right_rotate(T, x.p)
                        x = T.root
        x.is_red = False

    def tree_delete(T, z):
        print(f"deleting {z}")
        y = z
        y_original_color = y.is_red
        if z.l == T.nil:
            x = z.r
            T.transplant(z, z.r)
        elif z.r == T.nil:
            x = z.l
            T.transplant(z, z.l)
        else:
            y = RBTree.tree_min(z.r, T.nil)
            y_original_color = y.is_red
            x = y.r
            if y.p == z:
                x.p = y
            else:
                T.transplant(y, y.r)
                y.r = z.r
                y.r.p = y
            T.transplant(z, y)
            y.l = z.l
            y.l.p = y
            y.is_red = z.is_red
        if not y_original_color:
            T.rb_delete_fixup(x)

    @staticmethod
    def left_rotate(T, x):
        y = x.r
        x.r = y.l
        if y.l:
            y.l.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x.p.l == x:
            x.p.l = y
        else:
            x.p.r = y
        y.l = x
        x.p = y

    @staticmethod
    def right_rotate(T, x):
        y = x.l
        x.l = y.r
        if y.r:
            y.r.p = x
        y.p = x.p
        if x.p == T.nil:
            T.root = y
        elif x.p.l == x:
            x.p.l = y
        else:
            x.p.r = y
        y.r = x
        x.p = y

# RED BLACK TREE - MAIN
T = RBTree()
for i in range(100, 125):
    # Checking insertion
    T.tree_insert(RBNode(i, i))

# Checking inorder walk
print(f"in order traversal of the tree after inserting keys from range 1 to 10: {T.inorder_walk(T.root)}")

# Checking Min and Max
print(f"Min of the tree: {T.tree_min(T.root, T.nil)}, Max of the tree: {T.tree_max(T.root, T.nil)}")

# Checking Search, Predecessor, Successor
node = T.tree_search(5.5)
if node != None: print("5.5 exists in the tree")
else: print("5.5 doesn't exist in the tree")

node = T.tree_search(120)
if node != T.nil: 
    print("120 exists in the tree")
    print(f"predecessor of 120: {RBTree.tree_predecessor(node, T.nil)}, successor of 120: {RBTree.tree_successor(node, T.nil)}")
else: print("120 doesn't exist in the tree")

# Checking Delete, Rotations, Transplant, Fixup
T.tree_delete(node)
print(f"inorder traversal of the tree after deletion of 120: {T.inorder_walk(T.root)}") 

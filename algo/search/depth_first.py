from data_structures.binary_tree import BinaryTree


def pre_order_search( target , root):
    
    if root:
        
        if root.data == target:
            return True
        
        if pre_order_search( target , root.left ):
            return True
        
        
        if pre_order_search( target , root.right ):
            return True
        
    return False


def post_order_search( target , root):
    
    if root:
        
        if post_order_search( target , root.left ):
            return True
        
        if post_order_search( target , root.right ):
            return True
        
        if root.data == target:
            return True
        
    return False



def in_order_search( target , root):
    
    if root:
        
        if in_order_search( target , root.left ):
            return True
        
        if root.data == target:
            return True
        
        if in_order_search( target , root.right ):
            return True
        
        
    return False



def search(args):
    
    binary_tree = BinaryTree()
    print("building tree ...")
    
    binary_tree.create_from_file(args.file)
    
    print("Tree built ")
    
    
    if args.order == "pre-order":
        
        print("Searching Tree ...")

        target = args.word
        
        if pre_order_search(target , binary_tree.root):
            print("word Found")

        else:
            print("word not found ")
            
    
    if args.order == "post-order":
        print("Searching Tree ...")

        target = args.word
        
        if post_order_search(target , binary_tree.root):
            print("word Found")

        else:
            print("word not found ")
    
    
    if args.order == "in-order":
        print("Searching Tree ...")

        target = args.word
        
        if in_order_search(target , binary_tree.root):
            print("word Found")

        else:
            print("word not found ")
    else :

        print("Cannot use that impl , use Pre-order / Post-order or In-order for DFS traversal")
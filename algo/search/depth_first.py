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
        pass
    
    
    if args.order == "level-order":
        pass
    
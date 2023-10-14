from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def search(args):
    
    binary_tree = BinaryTree()
    
    print("building tree ...")
    binary_tree.create_from_file( args.file )
    print("Tree built")
    
            
    if args.order == "level-order":
        print("searching ...")
        target = args.word
        
        if binary_tree.root == target:
            print("this was the first word")
            return 
        
        queue = Queue()
        queue.enqueue(binary_tree.root)
             
        
        while queue.get_len():
            
            node = queue.dequeue()
            
            if node.left:
                if node.left.data == target:
                    print("word found ")
                    return 
                
                else:
                    queue.enqueue(node.left)
                    
                    
            if node.right:
                if node.right.data == "target":    
                    print("word found")
                    return 
                
                else:
                    queue.enqueue(node.right)
                    
        print("word not found !")
        return 
    
    print("BFS can only use level-order ")
                


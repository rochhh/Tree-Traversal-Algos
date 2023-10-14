import argparse
from search import breadth_first
from search import depth_first

def main():
    
    parser = argparse.ArgumentParser( description = "Search for a word in a file" )
    
    # word 
    
    parser.add_argument( "-w" , "--word" , required=True , help="Word to be searched for" )
    
    # file 
    parser.add_argument( "-f" , "--file" , required=True , help="File to be searched for" )
    
    # searching algo 
    parser.add_argument( "-sa" , "--search-algorithm" , choices=["binary-search" , "depth-first-search" , "breadth-first-search"] , required=True , help="Algo to be used to perform the steps" )
    
    # order 
    parser.add_argument( "-o" , "--order" , choices=["pre-order" , "post-order" , "in-order" , "level-order"] , required=True , help="the order in which we traverse the tree" )
    

    args = parser.parse_args()        

    # if args.search_algorithm == "binary-search":
    #     # binary.search(args)
    #     return
     
    if args.search_algorithm == "depth-first-search":
        depth_first.search(args)
        return
     
    if args.search_algorithm == "breadth-first-search":
        breadth_first.search(args)
        return
    
    

if __name__ == "__main__":
    main()
    
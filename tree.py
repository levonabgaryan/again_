# Tree sort  https://www.youtube.com/watch?v=n2MLjGeK7qA

class Bin_Tree():
    
    def __init__(self,item=0):
        self.key = item
        self.left = None
        self.right = None
        
tree = Bin_Tree()

tree = None
 

def insert(key):
    global tree
    tree = insertRec(tree, key)
    
def insertRec(tree,key):
    if tree == None:
        tree = Bin_Tree(key)
        return tree
    print(tree)
    print(tree.key)
    if key < tree.key:
        tree.left = insertRec(tree.left,key)
    
    elif key >= tree.key:
        tree.right = insertRec(tree.right,key)
    print(key)
    return tree
    

k = []    
    
def inorderRec(tree):
    if (tree != None):
        inorderRec(tree.left)
        k.append(tree.key)
        inorderRec(tree.right)

def treeins(arr):
    for i in range(len(arr)):
        insert(arr[i])


def sort_array_tree(arr):
    treeins(arr)
    inorderRec(tree)  
    return k

print(sort_array_tree([5, 7 ,11]))
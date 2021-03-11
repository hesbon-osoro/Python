# A O(n^2) Python3 program for construction of BST from preorder traversal  
  
# A binary tree node  
class Node(): 
      
    # A constructor to create a new node  
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
  
# constructTreeUtil.preIndex is a static variable of 
# function constructTreeUtil 
  
# Function to get the value of static variable  
# constructTreeUtil.preIndex 
def getPreIndex(): 
    return constructTreeUtil.preIndex 
  
# Function to increment the value of static variable 
# constructTreeUtil.preIndex 
def incrementPreIndex(): 
    constructTreeUtil.preIndex += 1
  
# A recurseive function to construct Full from pre[]. 
# preIndex is used to keep track of index in pre[[]. 
def constructTreeUtil(pre, low, high, size): 
      
    # Base Case  
    if( getPreIndex() >= size or low > high): 
        return None
  
    # The first node in preorder traversal is root. So take 
    # the node at preIndex from pre[] and make it root,  
    # and increment preIndex 
    root = Node(pre[getPreIndex()]) 
    incrementPreIndex() 
  
    # If the current subarray has onlye one element, 
    # no need to recur 
    if low == high : 
        return root  
  
    # Search for the first element greater than root 
    for i in range(low, high+1): 
        if (pre[i] > root.data): 
            break 
      
    # Use the index of element found in preorder to divide 
    # preorder array in two parts. Left subtree and right 
    # subtree  
    root.left = constructTreeUtil(pre, getPreIndex(),  i-1 , size)  
  
    root.right = constructTreeUtil(pre, i, high, size)  
      
    return root 
  
# The main function to construct BST from given preorder  
# traversal. This function mailny uses constructTreeUtil() 
def constructTree(pre): 
    size = len(pre)  
    constructTreeUtil.preIndex = 0 
    return constructTreeUtil(pre, 0, size-1, size) 
  
  
def printInorder(root): 
    if root is None: 
        return 
    printInorder(root.left) 
    print (root.data,)
    printInorder(root.right) 
  
  
# Driver program to test above function 
pre = [10, 5, 1, 7, 40, 50] 
  
root = constructTree(pre) 
print ("Inorder traversal of the constructed tree:")
printInorder(root) 
  
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
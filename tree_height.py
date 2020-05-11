class node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def maxDepth(node): 
	if node is None: 
		return 0 
	else : 
		lDepth = maxDepth(node.left) 
		rDepth = maxDepth(node.right)  
		if (lDepth > rDepth): 
			return lDepth+1
		else: 
			return rDepth+1
root = node(1) 
root.left = node(2) 
root.right = node(3) 
root.left.left = node(4) 
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.left.left = node(8)
root.right.left.right = node(9)
root.right.left.left.left=node(10)
print("\n")
print ("-------->>>>  %d is the height of tree" %(maxDepth(root)))  
print("\n")



#######output
#  python prg5.py


#  -------->>>>  5 is the height of tree

#....

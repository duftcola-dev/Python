# Perfect binary tree
# A perfect binary tree is a type of binary tree in
# which every internal node has exactly two child nodes
# and all the leaf nodes are at the same level.




# +++++++++++++This datastructure doesnt work properly and needs more research  +++++++++++++
class node:

	data=None 
	left=None  
	right=None  

	def __init__(self,data): 

		self.data=data  




def calculate_depth(node):

	depth=0

	while (node.left is not None):

		depth += 1
		node=node.left

	return depth
	



def IsPerfectTree(tree,depth,level=0)->bool:


	if root==None:
		return True

	if depth==level+1:

		print(f" depth : {depth} level : {level}")

		if tree.left is None and tree.right is None :

			return True

		if tree.left is not None or tree.right is not None: 

			return False	


	return (IsPerfectTree(tree.left, depth,level+1) and IsPerfectTree(tree.right, depth,level+1))








# Nodes


new_node1=node(12)
new_node2=node(11)
new_node3=node(13)
new_node4=node(14)
new_node5=node(15)
new_node6=node(20)
new_node7=node(22)



# perfect bynary tree
root=None 
root=node(10)
root.right=new_node1
root.left=new_node2




# Creating degenearate tree


root2=node(10)
root2.right=new_node1
root2.left=new_node2

root2.right.right=new_node3
root2.right.left=new_node4

root2.left.right=new_node5
root2.left.left=new_node6
root2.left.left.left=new_node7
root2.left.left.right=new_node1

root2.left.left.left.right=new_node7
root2.left.left.right.left=new_node1




print("First tree ")
d=calculate_depth(root)

if IsPerfectTree(root,d)==True:
	print("Is a perfect tree")
else:
	print("Is not a perfect tree")



print("Second tree ")
d2= calculate_depth(root2)

if IsPerfectTree(root2,d2)==True:
	print("Is a perfect tree")
else:
	print("Is not a perfect tree")

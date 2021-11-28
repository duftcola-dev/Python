#full binary tree algorythms

# A full Binary tree is a special type of binary tree
# in which every parent node/internal node has either two or no children.

# let i= number of internal nodes
# let n= total number of nodes
# let l = the total number of leaves
# let y = the number of levels

# taking into aacoutnthe previous data : 
# total number of leaves is  i+1 (it must have at leas one node children)
# total number of nodes is 2i+1 or 2l-1 (since it must have at least two child nodes + 1 leave)
# total number of internal nodes is l-1 or (n-1) / 2


# checking if a  bynary tree is a full tree : 

class node:

	data=None 
	left=None  
	right=None  

	def __init__(self,data):

		self.data = data 

# Creating a full binary tree
root= node(10)
new_nodel_l1=node(12) #level 1
new_noder_l1=node(11)

new_nodel_l2=node(24)
new_noder_l2=node(25)

root.left=new_nodel_l1
root.right=new_noder_l1
root.right.right=new_noder_l2
root.right.left=new_nodel_l2

# creating a non full binary tree ( a degenerated tree)

root2=node(1)
new_nodel_l1=node(2)
new_noder_l1=node(3)
new_noder_l2=node(4)
root2.left=new_nodel_l1
root2.right=new_noder_l1
root2.right.right=new_noder_l2




def IsFullBynaryTree(tree)->bool: 


	if tree.data==None :

		return False 

	if tree.left==None and tree.right==None :

		return True 

	if tree.left != None and tree.right !=None : 
		return (IsFullBynaryTree(tree.left) and IsFullBynaryTree(tree.right))


	return False




def CheckTreeType(tree):

	if IsFullBynaryTree(tree):
		print("Full bynary tree")
	else:
		print("IS not a full binary tree")



print("First tree ")
CheckTreeType(root)
print("Second tree ")
CheckTreeType(root2)
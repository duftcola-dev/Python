#case study of the tree datastructure. The tree is a non linear hierarchical datastructure.
# is main advantage is the ability to quicker acces to data in comparison with linear datastructures 
# like stacks , queues and linear arrays

# This is a full bynary try. I full bynary tree is which internal parent
# has 2 or none children . In this case every internal paren has 2 children

class tree:


    data=None  
    left=None 
    right=None 

    def __init__(self,data):
        self.data=data


# This are the most common methods of traversing a tree
# They are all recursive methods

def inorder(root):

    if root:
        inorder(root.left)
        print(f"data -> : {root.data}")
        inorder(root.right)


def postorder(root):

    if root:
        postorder(root.left)
        postorder(root.right)
        print(f"data -> : {root.data}")


def preorder(root):

    if root:
        print(f"data -> : {root.data}")
        preorder(root.left)
        preorder(root.right)



root_node = tree(10)

new_node0=tree(12)
new_node1=tree(2)
new_node2=tree(5)
new_node3=tree(1)
new_node4=tree(7)
new_node5=tree(8)


root_node.left=new_node0
root_node.right=new_node1
root_node.left.left=new_node2
root_node.left.right=new_node3
root_node.right.left=new_node5
root_node.right.right=new_node4



print("Inorder ->")
inorder(root_node)
print("Postorder ->")
postorder(root_node)
print("Preorder ->")
preorder(root_node)




# This is a study of the stack data structure
# The stack datastructures follows the LIFO principle . Last in first out.

class Stack:

    def __init__(self, limit: int):
        self.elements = []
        self.index = -1
        self.limit = limit-1


    def Top(self):
        if self.IsEmpty()==True:
            return None
        return self.elements[self.index]


    def Clear(self):

        self.limit=[]


    def Add(self,element):

        self.index = self.index + 1
        self.elements.append(element)


    def Pull(self):

        result=self.elements.pop(self.index)
        self.index = self.index - 1
        return result


    def IsFull(self):

        if self.index==self.limit:
            return  True
        return  False


    def IsEmpty(self):

        if self.index < 0:
            return True
        return False



# case 1 Use cases of the stack
# Use with simple int
limit=10
add_items=29
new_stack = Stack(limit)

if new_stack.IsEmpty():
    for items in range(add_items):

        if new_stack.IsFull()==True:
            print("Stack is full")
            break
        new_stack.Add(items)
        print(new_stack.Top())

if new_stack.IsFull()==True:
    print("Emptying stack")
    while(new_stack.IsEmpty()==False):
        print(new_stack.Top())
        new_stack.Pull()
    print("Stack is empty")
    print(new_stack.Top())




# case 2 A Stack of processes
# using a stack with functions and objects
def Todo():

    print("This is  task and it does things")

class TodoObject:

    def Todo(self):

        print("This is a task from an object")

objects=TodoObject()
functions=Todo

limit=10
funct_stack=Stack(limit)

print("Creating a stack of processes")
if funct_stack.IsEmpty()==True:
    for items in range(20):

        if items > 5:
            funct_stack.Add(functions)
        else:
            funct_stack.Add(objects)

        if funct_stack.IsFull()==True:
            print("FunctStack is full")
            break


print("Emptying functStack")
while(funct_stack.IsEmpty()==False):

    item=funct_stack.Top()
    if item.__class__.__name__=="TodoObject":
        item.Todo()
    else:
        item()
    funct_stack.Pull()
print("funct_stack empty")



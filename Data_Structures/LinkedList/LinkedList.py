
from collections import deque
from typing import List


class Node:

    def __init__(self,data) -> None:
        self.data=data
        self.next=None

    
    def __repr__(self) -> str:
        
        return self.data




# creating my own linked list
# The linked list only needs to store the head
class linkedlist:

    length=0

    def __init__(self,nodes=None) -> None:

        self.head=None
        

        if nodes is not None:

            self.length=len(nodes)
            node=Node(data=nodes.pop(0))
            self.head=node

            for elements in nodes:

                node.next=Node(elements)
                node=node.next


    def __repr__(self) -> str:
        
        node=self.head
        nodes=[]
        while node is not None:

            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return " ->".join(nodes)



    def __iter__(self):

        node=self.head

        while node is not None:
            yield node
            node=node.next



    def add_after(self,targe_node,new_node):

        self.IsListEmpty()
        
        for node in self:

            if targe_node==node.data:
                
                new_node.next=node.next
                node.next=new_node
                self.length+=1
                return



    def add_before(self,target_node,new_node):

        self.IsListEmpty()

        if self.head.data==target_node:
            self.add_first(new_node)

        prev_node=self.head
        for node in self:

            if target_node==node.data:
                
                new_node.next=node
                prev_node.next=new_node
                self.length+=1
                return
            
            prev_node=node



    def add_first(self,node):

        if self.head is None:
            self.head=node
            self.length+=1
        else:
            self.length+=1
            node.next=self.head
            self.head=node



    def add_last(self,node):

        if self.head is None:
            self.head=node
            self.length+=1
            return

        for nodes in self: # just traversing the list until the las node
            pass
        
        node.next=None
        nodes.next=node
        self.length+=1



    def remove(self,targe_node):

        self.IsListEmpty()

        if targe_node==self.head.data:
            self.head=self.head.next
            self.length-=1

        previous_node=self.head
        for nodes in self:

            if targe_node==nodes.data:
                previous_node.next=nodes.next
                self.length-=1
                return
            previous_node=nodes



    def get(self,item):
        
        self.IsListEmpty()
  
        for nodes in self:

            if nodes.data==item:
                return nodes.data



    def reverse(self):
        
        self.IsListEmpty()
        prev=None
        current=self.head
        next=None

        while(current is not None):
            #A
            next=current.next#B
            current.next=prev#None
            prev=current#A
            current=next#B
        self.head=prev


    def IsListEmpty(self):

        if self.head is None:
            raise Exception("List empty")
      



class Queue(linkedlist):

    def __init__(self, nodes=None) -> None:
        super().__init__(nodes=nodes)


    def Enqueue(self,element):

        new_element=Node(element)
        self.add_last(new_element)
        

    def Dequeue(self):

        result=self.head
        self.head=self.head.next
        return result


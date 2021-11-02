


from os import times


class Node:

    def __init__(self,data) -> None:
        
        self.prev=None
        self.data=data
        self.next=None

    def __repr__(self) -> str:
        
        return self.data



class DoubleLinkedList:


    def __init__(self,nodes=None) -> None:
        
        self.head=None
        self.tail=None
        self.lenght=0
        
        if nodes != None:
        
            first_item=nodes.pop(0)
            node=Node(first_item)
            self.head=node

            prev=self.head
            for elements in nodes:
                
                #A
                node.next=Node(elements)#B
                node=node.next#B
                node.prev=prev#A
                prev=node#B
                self.lenght+=1
                self.tail=prev



    def __repr__(self) -> str:
        
        self.IsListEmpty()
        node=self.head
        nodes=[]
        while node is not None:

            nodes.append(node.data)
            node=node.next

        rep="<-->".join(nodes)
        rep="None<-"+rep+"->None"
        return rep


    
    def __iter__(self):

        self.IsListEmpty()
        node=self.head
        while node is not None:

            yield node.data
            node=node.next



    def rev_iter(self):

        self.IsListEmpty()
        node=self.tail
        
        while node is not None:

            yield node.data
            node=node.prev



    def count(self,item)->int:
        
        node=self.head
        count=0

        while node is not None:

            if node.data==item:

                count=count+1
        
            node=node.next

        return count


    def search(self,item)->list:
        
        node=self.head
        result=[]

        while node is not None:

            if node.data==item:

                result.append(node.data)
                
            node=node.next

        return result



    def get(self,item):

        h_node=self.head
        t_node=self.tail
        result=None

        while h_node is not None or t_node is not None:

            if h_node.data==item:

                result= h_node.data
                break

            if t_node.data==item:

                result= t_node.data
                break

            h_node=h_node.next
            t_node=t_node.prev

        return result



    def add_last(self,item):

        self.IsListEmpty()
        new_node=Node(item)
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
        self.lenght+=1



    def add_first(self,item):

        self.IsListEmpty()
        new_node=Node(item)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
        self.lenght+=1

    


    def insert_after(self,target_node,item):

        self.IsListEmpty()
        new_node=Node(item)

        h_node=self.head
        t_node=self.tail

        while h_node is not None or t_node is not None:

            if h_node.data==target_node:

                new_node.next=h_node.next
                new_node.prev=h_node
                h_node.next=new_node
                self.lenght+=1
                break
            
            if t_node.data==target_node:

                if self.tail.data==target_node:

                    self.add_last(item)
                    self.lenght+=1
                    break

                new_node.next=t_node.next
                new_node.prev=t_node
                t_node.next=new_node
                self.lenght+=1
                break

            h_node=h_node.next
            t_node=t_node.prev




    def insert_before(self,target_node,item):

        self.IsListEmpty()
        new_node=Node(item)

        h_node=self.head
        t_node=self.tail

        right_last_node=h_node
        left_last_node=t_node

        while h_node is not None or t_node is not None:

            if h_node.data==target_node:
                
                if target_node==self.head.data:
                    
                    self.add_first(item)
                    self.lenght+=1
                    break

                new_node.prev=h_node.prev
                right_last_node.next=new_node
                h_node.prev=new_node
                new_node.next=h_node
                self.lenght+=1
                break
                
            
            if left_last_node.data==target_node:
     
                new_node.next=t_node.next
                new_node.prev=t_node
                t_node.next=new_node
                self.lenght+=1
                break

            right_last_node=h_node
            left_last_node=t_node
            h_node=h_node.next
            t_node=t_node.prev



    def remove(self,item):

        h_node=self.head
        t_node=self.tail

        result=None

        right_last_head=h_node
        left_last_tail=t_node
        while h_node is not None or t_node  is not None :

            if h_node.data==item:

                result=h_node
                h_node=h_node.next
                right_last_head.next=h_node
                h_node.prev=right_last_head
                break


            right_last_head=h_node
            left_last_tail=t_node
            h_node=h_node.next
            t_node=t_node.prev



        return result




    def IsListEmpty(self)->bool:

        if self.head == None:
            raise Exception("List is empty")

primitive=["A","B","C","D"]
dllist= DoubleLinkedList(primitive)
print(dllist)
dllist.remove("B")
print(dllist)
# This is a study of the queue datastruccture
# The queue datastructure follows the FIFO principle first in first out


class Queue:

    def __init__(self,limit) -> None:
        self.limit=limit-1
        self.queue=[]
        self.front=-1
        self.rear=-1

    def Enqueue(self,item):

        self.queue.append(item)
        self.rear=self.rear+1

    def Dequeue(self)->object:

        self.front=self.front+1
        return self.queue.pop(0)
       
    def Peek(self):

        return self.queue[self.front]

    def IsFull(self)->bool:

        if self.rear==self.limit:
            return True
        return False

    def IsEmpty(self)->bool:
        
        if self.front==self.rear:
            return True
        return False



#Use case of queue
new_queue=Queue(10)
print("Queueing elements")
count =10
while(new_queue.IsFull()==False):

    new_queue.Enqueue(count)
    count=count+1

print(new_queue.Peek())

print("Dequeueing elements")
while(new_queue.IsEmpty()==False):

    print(new_queue.Dequeue())

print("Queue is empty")
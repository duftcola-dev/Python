#Circular Queue study case


from typing import Counter, Tuple


class CircularQueue:

    def __init__(self,limit) -> None:
        
        self.limit=limit-1
        self.rear=-1
        self.front=-1
        self.items=[None] * limit


    def Peek(self):

        return self.items[self.rear]


    def Show(self):

        for item in range(self.limit):
            print(self.items[item])


    def Enqueue(self,item):

        self.rear=self.rear+1
        if self.rear > self.limit:
            self.rear=0

        self.items[self.rear]=item
       


    def Dequeue(self):

        self.front=self.front+1

        if self.front > self.limit:
            self.front=0

        return self.items[self.front]



    def IsEmpty(self)->bool:

        if self.rear==self.front:
            self.rear=-1
            self.front=-1
            return True

        return False



    def IsFull(self)->bool:

        if self.rear<self.front:
            return True
        
        if self.rear==self.limit and self.front==-1:
            return True

        return False



# Case use of circular queue /circular buffer

circular_queue=CircularQueue(10)

count=20
print("Filling queue")

while(circular_queue.IsFull()==False):

    circular_queue.Enqueue(count)
    count=count+1
    print(circular_queue.Peek())

print("Queue is full")

print("Emptying queue")

while(circular_queue.IsEmpty()==False):

    print(circular_queue.Dequeue())

print("Queue is empty")


print("Adding 3 items to queue")

for item in range(3):

    if circular_queue.IsFull()==True:
        break
    circular_queue.Enqueue(item)
    print(circular_queue.Peek())


print("removin 3 items to queue")

for item in range(3):

    circular_queue.Dequeue()



print("Adding 9 items to queue")
count=90
for item in range(9):

    count=count+1
    if circular_queue.IsFull()==True:
        break
    circular_queue.Enqueue(count)
    print(circular_queue.Peek())


print("Showing items")
circular_queue.Show()
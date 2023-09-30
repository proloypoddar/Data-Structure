class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue+=[item]
    def dequeue(self):
        if self.isempty():
            return None
        else:
            self.queue.pop()


    def isempty(self):
        if len(self.queue)==0:
            return False
    def pop(self):
        if self.isempty():
            return None
        item=self.queue[len(self.queue)-1]
        self.queue[len(self.queue)-1]=None
        return item
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue)
print(q.pop())
print(q.queue)
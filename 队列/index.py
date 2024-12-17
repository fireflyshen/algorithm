from typing import Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity  # 使用固定大小的数组表示队列
        self.rear = 0   # 队列尾部指针
        self.size = 0   # 当前队列中元素的数量

    """
        - desc: 队尾插入
        - author: firefly
    """
    def enqueue(self, val: T) -> bool:
        if self.is_full:
            self.__recapacity()
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity  # 循环移动 rear 指针
        self.size += 1
        return True

    """
        - desc: 队首删除
        - author: firefly
    """
    def dequeue(self) -> T:
        if self.is_empty:
            print("Queue is empty")
            return None
        item = self.queue[self.queue[0]] 
        self.__shift()
        self.size -= 1
        return item

    """
        - desc: 队列扩容
        - author: firefly
    """
    def __recapacity(self):
        new_capacity = self.capacity + (self.capacity >> 1)  # 扩容 1.5 倍
        new_queue = [None] * new_capacity
        
        # 将原队列元素重新排列到新队列中
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]

        self.queue = new_queue
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size  # 重新设置队尾指针

    """
        - desc: 判断队列是否满
        - author: firefly
    """
    @property
    def is_full(self) -> bool:
        return self.size == self.capacity

    """
        - desc: 判断队列是否空
        - author: firefly
    """
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    """
        - desc: 所有元素前移
        - author: firefly
    """
    def __shift(self): [self.queue.__setitem__(i,self.queue[i+1]) if i + 1 < self.size else None for i in range(self.size)]


    def __str__(self):
        result = "["  
        for i in range(self.size):
            result += str(self.queue[i]) + ","  
        if self.size > 0:
            result = result[:-1]  # 删除最后一个多余的逗号
        result += "]"
        return result

q = Queue(10)

# 插入 20 个元素
for i in range(7):
    q.enqueue(i)
print(q.queue)  # 打印队列内容
q.dequeue()
q.dequeue()

print(q.queue)  # 打印队列内容

print(q)

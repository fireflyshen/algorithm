class Solution:
    def knows(self, a: int, b: int) -> bool:
        ...
    
    def  _277_findCelebrity(self,n:int) -> int:
        candidate = 0
        for i in range(1, n):
            if self.know(candidate,i):
                candidate = i
        for i in range(n):
            if i != candidate and (self.knows(candidate,i)) or not self.knows(i,candidate):
                return -1
        return candidate
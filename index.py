from typing import List;    
    
def range_distribute(communities,n) -> int:
    # 最优解：假如有n个社区，就是有n个志愿者，那么时间就是社区中的最大值,并行。
    low = max(communities)
    # 最劣解：一个志愿者送菜，那么耗费的时间就是列表的和，相当于串行
    high = sum(communities)
    
    result = high
   
   # 以最优解和最劣解为上下限进行二分查找尝试合理分配区间 
    while low <= high:
        mid = (low + high) // 2
        if can_distribute(communities,n,mid):
            result = mid  
            high = mid - 1
        else:
            low = mid + 1
    return result

def can_distribute(communities:List[int],n:int,max_time:int):
     
    # 假设没有一个家庭需要送菜，那么所需时间就是0
    time = 0
    
    # 假设没有一个家庭需要送菜，那么所需志愿者就是0
    # v = 0
    
    # v = 0不对，即便没人送菜也要一个志愿者
    v = 1
    for f in communities:
        if time + f > max_time:
            v += 1
            time = f
            if v > n:  
                return False
        else:
            time += f
    return True


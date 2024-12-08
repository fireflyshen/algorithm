def demoMethodOne(name:str)-> None:
    print("hello",name)
    demoMethodTwo(name)
    bye()
    
def demoMethodTwo(name:str) -> None:
    print("how are you",name,"?")
    
    
def bye():
    print("ok bye")
        
        




def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x -1)
    
s = fact(3)

print(s)
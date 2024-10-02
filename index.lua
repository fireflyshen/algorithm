function hello(tab,func)
    for key, value in pairs(tab) do
        print(func(key,value))
    end
    
end



hello({h=1,a=2},function (key,value)
    return   key .. "=======" .. value
end)


function f()
    return 1,2;
end


h,i = f();


print(type(h..i))

-- 循环

-- local i = 0;
-- while i < 10 do
--     print(i);
--     i = i + 1;
-- end


for i = 1, 10, 1 do
    print(i)
end


function f(x)  
    print("function")  
    return x*2   
end  
for i=1,f(5),2 do print(i)  
end
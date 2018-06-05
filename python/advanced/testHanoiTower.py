def move(n, a, b, c):

    global count

    if n > 2:
        move(n-1,a, c, b)
    else:
        count+=1
        print(a,"=>",b)    
    
    count+=1
    print(a,"=>",c)

    if n > 2:
        move(n-1,b, a, c)
    else:
        count+=1
        print(b,"=>",c)    

count = 0
move(5,"A","B","C")
print("count = ", count)
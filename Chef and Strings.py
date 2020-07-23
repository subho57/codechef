try:
    t=int(input())
    while t:
        add=0
        inp=[]
        size=int(input())
        inp=input().split()
        temp=int(inp[0])
        for i in inp[1:size]:
            if temp!=int(i):
                add+=abs(temp-int(i))-1
            temp=int(i)
        print(add)
except:
    pass

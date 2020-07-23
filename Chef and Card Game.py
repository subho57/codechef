try:
    t=int(input())
    while(t):
        n=int(input())
        c,m=0,0
        while(n):
            temp=input().split()
            chef=int(temp[0])
            morty=int(temp[1])
            if chef>9:
                temp=[int(i) for i in str(chef)]
                chef=sum(temp)
            if morty>9:
                temp=[int(i) for i in str(morty)]
                morty=sum(temp)
            if chef>morty:
                c+=1
            elif morty>chef:
                m+=1
            else:
                m+=1
                c+=1
            n-=1
        if c>m:
            print(0, c)
        elif m>c:
            print(1, m)
        else:
            print(2, c)
        t-=1
except:
    pass

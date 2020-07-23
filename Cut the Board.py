try:
    T=int(input())
    while T:
        n,m=input().split()
        print(((int(n)-1)*(int(m)-1)))
        T=T-1
except:
    pass

def sum(n,s):
    res=0
    for i in s:
        res+=i
    return res
n=int(input())
s=list(map(int,input().split()))
total=sum(n,s)
print(total)

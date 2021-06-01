def evenodd(n,s):
    ec=0
    oc=0
    for i in range(n):
        if s[i]%2==0:
            ec=ec+i
            return ec
        else:
            oc=oc+i
    return oc

n=int(input())
s=list(map(int,input().split()))
total=evenodd(n,s)
print(total)

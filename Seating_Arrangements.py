n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
k='True'
for i in range(n-1):
    for j in range(len(l[i])):
        if l[i][j]>l[i+1][j]:
            k='False'
            break
print(k)

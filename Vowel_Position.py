l=['a','e','i','o','u']
t=[]
res=[]
n=input()
for i in range(len(n)):
    if n[i] in l:
        t.append(i)
for i in range(len(n)):
    m=abs(i-t[0])
    for j in range(1,len(t)):
        m=min(m,abs(i-t[j]))
    res.append(m)
print(res)

def myfunc():
    n=[]
    for _ in range(int(input())):
        n.append(input())
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            if n[i]==n[j][:len(n[i])]:
                print('No,there is a collision with',n[i])
                return
    else:
        print('Yes,it is consistent for',len(n),'numbers')
myfunc()

def compact(com):
    start=0
    store=[]
    for i in range(len(com)):
        if com[i]!=com[start]:
            store.append((start,i-1,com[start]))
            start=i
    store.append((start,len(com)-1,com[start]))
    for t in store:
        print(str(t[1]-t[0]+1)+t[2],end='')
A='BWWWWWBWWWW'
compact(A)


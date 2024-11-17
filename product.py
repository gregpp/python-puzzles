l = [-1,2,2,3,6]
#l = list(set(l))
s = set()
ln = len(l)
for i in range(ln-1):
    #print("i=",i)
    for j in range(i+1, ln):
        #print("j=",j)
        s.add(l[i]*l[j])
print (s)
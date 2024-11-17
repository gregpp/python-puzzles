#This script finds all unique products for given list of integers
l = [-1,2,2,3,6]
s = set()
ln = len(l)
for i in range(ln-1):
    for j in range(i+1, ln):
        s.add(l[i]*l[j])
print (s)

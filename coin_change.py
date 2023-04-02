import sys

def coinChange (coins, V):
    l = len (coins)
    if l == 0:
        return 0
    for i in range (0,l-1):
        if not isinstance(coins[i],int):
            return -1
    chg = [sys.maxsize] * (V + 1)
    chg[0] = 0
    for i in range (1,V+1):
        for j in range(l):
            if coins[j] <= i:
                cc = chg[i - coins[j]]
                if cc != sys.maxsize and cc + 1 < chg[i]:
                    chg[i] = cc + 1
    if chg[V] == sys.maxsize:
        return -1
    else:
        return chg[V]
print(coinChange([1,2,5,10,20],77))

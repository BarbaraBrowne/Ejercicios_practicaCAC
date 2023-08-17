#MCD El numero mas grande que divide dos numeros

def mcd(x,y):
    mcd=1
    
    if y % y == 0:
        return y
    
    for k in range(int(y/2), 0, -1):
        if x % k ==0 and y % k ==0:
            mcd = k
            break
        
    return mcd

print(mcd(12,8))
print(mcd(15,7))
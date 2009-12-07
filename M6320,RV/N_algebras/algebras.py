
phi = set()

def powerset( X ):
    n = len(X)
    P = set()
    
    for k in range(0,2**n):
        p = set()
        for j in range(0,2**n):
            if ( (k >> j) & 1 ):
                p.add(X[j] )
        P.add(p)
            
    return P






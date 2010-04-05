


from discrete_markov import *

alpha = 0.5
values = array([0,1])
distribution = array([1-alpha,alpha])
T = lambda : random_variable( distribution, values )

N = 5

len_path = 20
n_paths = 2000

X_paths = [ zeros(len_path) for n in range(n_paths) ]

for X in X_paths:
    
    R = lambda : random.randint(0,N-1)
    
    Z = zeros(N, int )
    Z[ R() ] = 1
    X[0] = 0
    
    for k in range(1,len_path):
        n1 = R()
        n2 = R()
        if ( Z[n1] != Z[n2] ):
            t = random.random()
            
            if t <= alpha:
                Z[n1] = 1
                Z[n2] = 1
        
        X[k] = sum(Z)-1


p = transition_matrix( X_paths, N  )

q = zeros((N,N))

for i in range(N):
    for j in range(N):
        if i == j:
            q[i,j] = 1-(float(j+1)/N)*(1-float(j+1)/N)*alpha*2
        if i == j+1:
            q[i,j] = (float(j+1)/N)*(1-float(j+1)/N)*alpha*2

for k in range(1,2):
    print around(p[k],2), '\n'  

print around(q,2), '\n' 



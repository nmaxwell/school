


from discrete_markov import *

alpha = 0.1

values = array([0,1])
distribution = array([1-alpha,alpha])
T = lambda : random_variable( distribution, values )

N = 5

len_path = 30
n_paths = 2000

X_paths = [ zeros(len_path, int ) for n in range(n_paths) ]


for X in X_paths:
    
    R = lambda : random.randint(0,N-1)
    
    Z = zeros(N, int )
    Z[ R() ] = 1
    X[0] = 1
    
    for k in range(1,len_path):
        n1 = R()
        n2 = R()
        
        if ( Z[n1] != Z[n2] ):
            if T() == 1:
                Z[n1] = 1
                Z[n2] = 1
        
        X[k] = sum(Z)


p = transition_matrix( X_paths, N, state_map = lambda x: x-1 )

q = zeros((N,N))

for i in range(N):
    for j in range(N):
        if i == j:
            q[i,j] = 1.0-(float(j+1)/N)*(1-float(j+1)/N)*2.*alpha
        if i == j+1:
            q[i,j] = (float(j+1)/N)*(1-float(j+1)/N)*2.*alpha


print 'computed transition matrix: \n', around(p[1],2), '\n'  

#print print ' transition matrix: \n', around(q,2), '\n' 
#print q , '\n' 

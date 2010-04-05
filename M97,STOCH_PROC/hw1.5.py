


from discrete_markov import *





a = 0.1
b = 0.2

P0 = array([[a,1.-b],[1.-a,b]])

len_path = 20
n_paths = 8000

X_paths = [ sample_path( 0, len_path, P0)  for n in range(n_paths/2) ]
X_paths.extend( [ sample_path( 1, len_path, P0)  for n in range(n_paths/2) ] )


Z_paths = []
for X in X_paths:
    Z = []
    for n,x in enumerate(X):
        if n>=1:
            Z.append( (X[n-1],X[n]) )
    Z_paths.append(Z)

def state_map(X):
    if X == (0,0):
        return 0
    if X == (1,0):
        return 1
    if X == (0,1):
        return 2
    if X == (1,1):
        return 3

#Z_paths = [ [ state_map(z) for z in Z ] for Z in Z_paths ]


p = transition_matrix( Z_paths, 4, state_map )


for k in range(1,2):
    print around(p[k],2), '\n'  





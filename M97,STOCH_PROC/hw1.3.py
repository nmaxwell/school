


from discrete_markov import *


values = array([0,1,2,3])
distribution = array([0.1,0.3,0.2,0.4])

Z = lambda : random_variable( distribution, values )


len_path = 20
n_paths = 20000

X_paths = [ zeros(len_path) for n in range(n_paths) ]

for X in X_paths:
    X[0] = 0
    for k in range(1,len_path):
        X[k] = max( Z(), X[k-1] )


p = transition_matrix( X_paths, 4 )


for k in range(1,2):
    print around(p[k],2), '\n'  





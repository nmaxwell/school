
import numpy
from numpy import *
import random


def random_variable( distribution, values ):
    w = random.random()*sum(distribution)
    s = 0
    for k in range(len(distribution)):
        s += distribution[k]
        if w<=s:
            return values[k]
    
    print error
    return values[-1]


def sample_path( X0, len_path, P ):
    
    X = zeros(len_path, int )
    N = range(len(P[0]))
    
    X[0] = X0
    for k in range(1,len_path):
        X[k] = random_variable( P[:,X[k-1]], N )
    
    return X


def transition_matrix( sample_paths, n_states, state_map= lambda x: x ):
    
    n_paths = len(sample_paths)
    len_path = len(sample_paths[0])
    
    p = zeros(( len_path, n_states, n_states ))
    
    for X in sample_paths:
        for k in range(1,len_path):
            for l in range(0,k):
                p[k-l][ state_map(X[k]) ][ state_map(X[l]) ] += 1
    
    for k in range(len_path):
        for i in range(n_states):
            s = sum(p[k][:,i])
            if s>1E-14:
                p[k][:,i] /= s
        
    return p





def mat_power(A, n):
    
    def mat_power_recurr(B, n ):
        if n==0:
            return eye(len(B))
        if n==1:
            return B
        
        return mat_power_recurr( dot(A,B), n-1)
    
    return mat_power_recurr( A, n)





if __name__ == "__main__":
    
    
    Pij = transpose( array([[0.01,0.01,0.98],[0.8,0.1,0.1],[0.05,.9,0.05]]) )
    
    
    X0 = 1
    v = zeros(3)
    v[X0] = 1
    
    n_paths = 5000
    len_path = 20
    
    print v
    
    X = [ sample_path( 1, len_path, Pij)  for n in range(n_paths) ]
    
    p = transition_matrix( X, 3  )
    
    print Pij, '\n','\n'
    
    for k in range(1,5):
        print around(p[k],2), '\n'
    
    print '\n','\n'
    
    for k in range(1,5):
        print around( mat_power(Pij, k ) ,2),'\n'
    
    
    

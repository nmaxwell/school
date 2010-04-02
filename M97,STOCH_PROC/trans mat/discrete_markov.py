
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
    
    X = arange(len_path)*0
    N = range(len(P[0]))
    
    X[0] = X0
    for k in range(1,len_path):
        X[k] = random_variable( P[X[k-1]], N )
    
    return X



def transition_matrix( sample_paths, n_states ):
    
    n_paths = len(sample_paths)
    len_path = len(sample_paths[0])
    
    p = zeros(( len_path, n_states, n_states ))
    
    for X in sample_paths:
        
        for k in range(1,len_path):
            j = X[k]
            
            for l in range(0,k):
                i = X[l]
                
                p[k-l][i][j] += 1
    
    for k in range(len_path):
        for i in range(n_states):
            s = sum(p[k][i])
            if s>1E-14:
                p[k][i] /= sum(p[k][i])
    
    return p




def mat_power(A, n):
    if n==0:
        return eye(len(A))
    if n==1:
        return A
    
    B = A
    for k in range(n):
        B = dot(A,B)
    return B





if __name__ == "__main__":
    

    
    
    Pij = array([[0.01,0.01,0.98],[0.8,0.1,0.1],[0.05,.9,0.05]])
    #Pij = array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]])
    
    X0 = 2
    v = zeros(3)
    v[X0] = 1
    
    n_paths = 5000
    len_path = 5
    
    print v
    
    X = [ sample_path( 2, len_path, Pij)  for n in range(n_paths) ]
    
    p = transition_matrix( X, 3  )
    
    print Pij, '\n'
    
    for k in range(1,len(p)-1):
        
        #p[k] = numpy.round(p[k],2)
        print k, dot(p[k],v), '\n', dot(mat_power(Pij, k ),v),'\n\n\n'
    
    
    
    #   , '\n', [ sum(p[k][i]) for i in range(len(p[k])) ]
    
    
    
    """
    import pylab as p
    
    for k in range(3):
        p.plot( X[k] )
    
    p.show()
    """


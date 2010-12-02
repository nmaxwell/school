
#includes
import numpy
import random
import matplotlib
matplotlib.use('macosx')
import matplotlib.pyplot as plt

#default global norm is l2-norm for any vetor type data
norm = numpy.linalg.norm


#defining some general functions:

def operator_powers_convergence(P, eps=1E-6, max_iterations=1000):
    """
    try to take limit of P^n as n goes to infinity
    stop at 'max_iterations' number of iterations,
    or when the norm difference between subsequent 
    powers is less than 'eps'
    """
    
    A = P.copy()
    B = P
    iters = 0
    while iters < max_iterations:
        iters += 1
        A *= P
        dist = norm(A-B)
        if dist < eps:
            break
        B = A.copy()
    
    return A, dist, iters

def vector_round(M, places=3):
    """
    return M, with all its entries rounded to 'places' number of decimal places
    """
    
    return numpy.round((M)*10**places)/(10**places)

def set_matrix(mat, function):
    """
    set the entries in the matrix, according to the function
    """
    n,m = numpy.shape(mat)
    for i in range(n):
        for j in range(m):
            mat[i,j] = float(function(i,j))
    return mat

def matrix(rows, cols, initializer=None):
    """
    construct and return a matrix
    """
    A = numpy.matrix(numpy.zeros((rows, cols)))
    if initializer is not None:
        set_matrix(A, initializer)
    return A

class pdf_sampler:
    def __init__(self, pdf, ):
        self.length = len(pdf)
        self.pdf = [pdf[k]/sum(pdf) for k in range(self.length)]
        self.cdf = self.pdf
        for k in range(1,self.length):
            self.cdf[k] += self.cdf[k-1]
        
        self.n_breaks = 10
        self.break_points = [ ]
        for k in range(self.n_breaks):
            self.break_points.append(self.invert(float(k)/self.n_breaks))
    
    def sample(self, ):
        x = random.random()
        bin = int(x*self.n_breaks)
        for k in range(self.break_points[bin], self.length):
           if x <= self.cdf[k]:
                return k 
        return self.length-1
    
    def invert(self, x):
        
        for k in range(self.length):
            if x <= self.cdf[k]:
                return k
        return self.length-1



def cumulative_transitions(P):
    """
    turn a transition probablity matrix 'P' into a
    list of pdf samplers, according to the pdfs
    that are the columns of P
    """
    return [pdf_sampler(p) for p in numpy.array(P.transpose())]







def check():
    p = [0.2, 0.1, 0.2, 0.4, 0.1]
    sampler = pdf_sampler(p)
    
    n = 10000
    d = [0 for k in range(len(p))]
    for k in range(n):
        d[sampler.sample()] += 1
        
    print [float(d[k])/sum(d) for k in range(len(d))]

def hitting_time(cumulative_P, target, initial, max_count=10000):    
    X = initial
    count = 0
    while count < max_count:
        count += 1
        X = sample(cumulative_P[X])
        if X == target:
            return count


def sample_hitting_times(samples, P, target, initial, max_count=10000):
    cum_P = cumulative_transitions(P)
    
    return [hitting_time(cum_P, target, initial, max_count) \
                for k in range(samples)]

def distribution(values ):
    m = max(values)
    dist = [0 for k in range(m+1)]
    for v in values:
        dist[v] += 1
    return [float(p)/sum(dist) for p in dist]














from discrete_markov import *

def Z():
    return float( random.random() >= 0.5 )


N_values = [1,2,3,4]
N_distribution = [0.5,0.1,0.2,0.2]

N = lambda : random_variable(N_distribution, N_values )


def X_n(n):
    return sum([ Z() for k in range(n)])


def sig_m(X):
    xm = mean(X)
    return sqrt(sum([ (xi - xm)**2 for xi in X ])/(len(X)*(len(X)-1)))


if __name__ == "__main__":
    
    n_samples = 200000
    
    samples = [X_n(N()) for k in range(n_samples) ]
    
    print 'E[X]= ', mean(samples), '+\-', sig_m(samples)
    
    


"""


    def sig_m(X):
        xm = mean(X)
        return sqrt(sum([ (xi - xm)**2 for xi in X ])/(len(X)*(len(X)-1)))



    def trial(n_runs):
        runs = [ N() for k in range(n_runs) ]
        return ( mean(runs), sig_m(runs) )
    
    ps = range(4,16)
    trials = [  trial( 2**p ) for p in ps ]
    means = [ trial[0] for trial in trials  ]
    sigms = [ trial[1] for trial in trials  ]
    
    gradient, intercept, r_value, p_value, std_err =  stats.linregress(ps, [ log2(sigm) for sigm in sigms ])
    
    Y = [ gradient*p + intercept for p in ps ]
    
    
    print "\n"
    print "Result: ", means[-1], "+/-", sigms[-1]
    print "Convergence: error(N) ~ C*N^a, C=", 2**intercept, "a=", gradient
"""

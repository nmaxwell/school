
import random
from numpy import *
from scipy import stats

def Z():
    return float( random.random() >= 0.5 )

def X_n(n):
    return sum([ Z() for k in range(n)])

def N():
    x = random.random()
    if x<0.5:
        n=1
    else:
        if x<.6:
            n = 2
        else:
            if x<.8:
                n = 3
            else:
                n = 4
    
    return X_n( n )


def sig_m(X):
    xm = mean(X)
    return sqrt(sum([ (xi - xm)**2 for xi in X ])/(len(X)*(len(X)-1)))



if __name__ == "__main__":
    
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

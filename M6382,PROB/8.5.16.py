
import numpy
import random
import matplotlib
matplotlib.use('macosx')
import matplotlib.pyplot as plt

norm = numpy.linalg.norm

def convergence(P, eps=1E-6, max_iterations=1000):
    
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

def mat_round(M, places=3):
    return numpy.round((M)*10**places)/(10**places)


def sample(cum_dist ):
    n = len(cum_dist)
    x = random.random()
    for k in range(n):
#        print k, x
        if x <= cum_dist[k]:
            return k
    return n-1

def cumulative_distribution(distribution ):
    n = len(distribution)
    cd = [distribution[k]/sum(distribution) for k in range(n)]
    for k in range(1,n):
        cd[k] += cd[k-1]
    return cd

def check():
    p = [0.2, 0.1, 0.2, 0.4, 0.1]
    cd = cumulative_distribution(p)
    
    n = 10000
    d = [0 for k in range(len(p))]
    for k in range(n):
        d[sample(cd)] += 1
        
    print [float(d[k])/sum(d) for k in range(len(d))]


def cumulative_transitions(P):
    return [cumulative_distribution(p) \
                for p in numpy.array(P.transpose())]


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


P = numpy.matrix([[0,2.0/3,1.0/3],[0.25,0,0.75],[0.8,0.2,0.0]]).transpose()


print P
n_samples = 100000
samples = sample_hitting_times(n_samples, P, 0, 0 )

tau_dist = distribution(samples)

print "\nhitting time:"
print "number of samples: ", n_samples
print "distribution:"
for k in range(len(tau_dist)):
    print k, tau_dist[k]

#plt.plot(tau_dist, 'ro')
#plt.show()

print "mean return time:"
print numpy.mean(samples)

(limP, dist, iterations) = convergence(P, 1E-15)

print "transition matrix: \n", mat_round(P)
print "converged P^n: \n", mat_round(limP,6)
print "error: ", dist
print "number of powers: ", iterations















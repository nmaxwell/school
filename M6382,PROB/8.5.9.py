
import numpy

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


P = numpy.matrix([[0.5, 2.0/3.0, 0.0, 1.0],[0.5,0,0,0],[0,0,4.0/5,0.0],[0.0, 1.0/3, 1.0/5, 0]])

(limP, dist, iterations) = convergence(P, 1E-18)


print "Part a:"
print "transition matrix: \n", mat_round(P)
print "converged P^n: \n", mat_round(limP)
print "error: ", dist
print "number of powers: ", iterations


P = numpy.matrix( \
    [[1.0, 0,0,0,0,0,0], \
     [0.5,0.0,0.5, 0,0,0,0], \
     [0, 0.2, 0.8, 0,0,0,0], \
     [0,0, 1.0/3, 1.0/3, 1.0/3, 0,0], \
     [0.1, 0, 0,0, 0.7, 0, 0.2 ], \
     [0,0,0,0,0,0,1], \
     [0,0,0,0,0,1,0]]).transpose()

(limP, dist, iterations) = convergence(P, 0.1)

print "\n Part b:"
print "transition matrix: \n", mat_round(P)
print "converged P^n: \n", mat_round(limP)
print "error: ", dist
print "number of powers: ", iterations


print "powers of P:\n"
for k in range(100,103):
    print "P^" + str(k) +":\n", mat_round(P**k)






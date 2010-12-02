
from preliminaries import *

# python indexes arrays, matrices from 0, not 1.

# number of states
N = 300
# fitness
s = 0.02
r = 1.0+s

# initial state
initial_state = 1


#construct transition probability matrix

def Q_function(i,j):
    # p_{i,j} = Prob( X_{t+1} = i | X_t = j)

    if j == 0:
        # in this case, there are zero A's, 
        # so there remain zero A's
        return i == 0
    
    if j == N:
        # in thise case, all individuals are A's
        # so ther remain zero B's
        return i == N
    
    if i == j+1:
        # in this case, one B dies, and one A is born
        # death of B is with probability (N-i)/N
        # birth of A is with probability r*i/(r*i+N-i)
        return (r*j/(r*j+N-j)) * (N-j)/N
    
    if i == j-1:
        # in this case, one A dies, and one B is born
        # death of A is with probability i/N
        # birth of B is with probability (N-i)/(r*i+N-i)
        return (float(N-j)/(r*j+N-j) ) * j/N
    
    if j == i:
        # in this case, the population doesn't change, 

        # so either one A dies and one A is born, or 
        # one B dies and one B is born.
        # this must occur with opposite probability to 
        # A -> B or B -> A
        
        return 1.0 -(r*j/(r*j+N-j))*(N-j)/N -(float(N-j)/(r*j+N-j) )*j/N
    
    # else:
    return 0.0

print('constructing transition matrix')
Q = matrix(N+1,N+1, Q_function)

print('computing transition cdfs')
cumulative_Q = cumulative_transitions(Q)

#print vector_round(Q)
#print [1.0-numpy.sum(Q[:,k]) for k in range(N+1)]


print('running simulation')

# run simulation

max_iterations = 10000

def sample_final_state():
    state = initial_state
    for k in range(max_iterations):
        state = cumulative_Q[state].sample()
        if state == 0 or state == N:
            break
    return state

def sample_path():
    X = [initial_state ]
    for k in range(max_iterations):
        X.append(cumulative_Q[X[-1]].sample())
        if X[-1] == 0 or X[-1] == N:
            break
    return X


def run():
    n_samples = 1000
    sum = 0.0
    for k in range(n_samples):
        sum += float(sample_final_state())/(N)
    
    print sum/n_samples, 1.0-1.0/r

run()
#check()

#plt.plot(X, 'b*')
#plt.show()





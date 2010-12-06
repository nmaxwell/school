
from preliminaries import *
    

n_samples = 10000
t = 3.0
P = PoissonProcess(Lambda = 2.0)

Bins1 = [0,  ]
for k in range(n_samples):
    N = P.one_time(t)
    while len(Bins1)<N+1:
        Bins1.append(0)
    Bins1[N] += 1.0/n_samples

Bins2 = [0]
for k in range(n_samples):
    P.new_sample()
    N = P.sample_path(t)
    while len(Bins2)<N+1:
        Bins2.append(0)
    Bins2[N] += 1.0/n_samples


plt.plot(Bins1, 'ro')
plt.plot(Bins2, 'bo')
plt.plot( [ ((P.Lambda*t)**k)*exp(-P.Lambda*t)/factorial(k) \
    for k in range(len(Bins1)) ], 'go')
plt.show()








if True:
    
    sm = SuperMarket( Lambda = 1.0, Queue_arguements = 0.1, n_Queues=3)    
    sm.sample()
    
    T = numpy.linspace(0,max([max(Q.cumulative_service_times) for Q in sm.Queues]),1000)
    #plt.ylim(-0.5,4)
    
    #plt.plot(sm.arrival_times.cumulative_times, [0.5 for t in sm.arrival_times.cumulative_times], 'mo')
    for q,Q in enumerate(sm.Queues):
        color = ['r', 'g', 'b' , 'y'][q]
        plt.plot(T, [Q.length(t) for t in T ], color )
        plt.plot(Q.arrival_times, [0.1 for t in Q.arrival_times], color+ 'o')
        plt.plot(Q.cumulative_service_times, [0.3 for t in Q.cumulative_service_times], color + 'o')
    
    plt.show()

    


if False:

    pp = PoissonProcess(1.0)
    T = numpy.linspace(0,5,1000)
    plt.ylim(-0.5,10)
    plt.plot(T, [pp.sample_path(t) for t in T ], 'g')
    print pp.cumulative_times
    plt.plot(pp.cumulative_times, [0.5 for t in pp.cumulative_times], 'bo')
    plt.show()

if False:
    
    sm = SuperMarket( Lambda = 1.0, Queue_arguements = 3.0 )
    sm.sample()    
    
    T = numpy.linspace(0,30,1000)
    plt.ylim(-0.5,4)
    plt.plot(T, [sm.Queues[0].length(t) for t in T ], 'y')
    plt.plot(sm.Queues[0].arrival_times, [0.1 for t in sm.Queues[0].arrival_times], 'ro')
    plt.plot(sm.Queues[0].cumulative_service_times, [0.3 for t in sm.Queues[0].cumulative_service_times], 'bo')
    #plt.plot(sm.arrival_times.cumulative_times, [0.5 for t in sm.arrival_times.cumulative_times], 'go')
    plt.show()

if False:

    Q = Queue(0.5)

    s = 0
    for k in range(6):
        s += random.uniform(0,0.7)
        Q.arrival(s)

        s += 2.0
        
        for k in range(6):
            s += random.uniform(0,0.7)
            Q.arrival(s)

        print numpy.round(numpy.array(Q.arrival_times), 3)
        print numpy.round(numpy.array(Q.service_times), 3)
        print numpy.round(numpy.array(Q.cumulative_service_times), 3)
        
        T = numpy.linspace(0,10,1000)
        plt.ylim(-0.5,4)
        plt.plot(T, [Q.length(t) for t in T ], 'g')
        plt.plot(Q.arrival_times, [0.5 for t in Q.arrival_times], 'bo')
        plt.plot(Q.cumulative_service_times, [0.5 for t in Q.cumulative_service_times], 'ro')
        plt.show()









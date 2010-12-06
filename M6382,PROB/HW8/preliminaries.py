
# includes:
import numpy
import random
import matplotlib
matplotlib.use('macosx')
import matplotlib.pyplot as plt
from math import *


# classes:

class PoissonProcess:
    
    def __init__(self, Lambda):
        self.Lambda = Lambda
        self.reset()
    
    def time(self):
        return random.expovariate(self.Lambda)
    
    def reset(self):
        self.cumulative_times = [0.0, self.time() ]
    
    def sample_path(self, t):
                
        while t >= self.cumulative_times[-1]:
            self.cumulative_times.append(self.time() + self.cumulative_times[-1])
        
        k = len(self.cumulative_times)-1
        while t < self.cumulative_times[k]:
            k -= 1
        return k
    
    def fixed_time_sample(self, t):
        k=0
        s = self.time()
        if t < s:
            return 0
        while s <= t:
            s += self.time()
            k += 1
        return k

class Queue:
    
    def __init__(self, service_parameters ):
        self.service_parameters = service_parameters
        self.reset()
    
    def reset(self):
        self.cumulative_service_times = []
        self.arrival_times = []
        self.service_times = []
    
    def arrival(self, time):
        
        if len(self.arrival_times) > 0:
            assert( time >= self.arrival_times[-1] )
        self.arrival_times.append(time)
        
        self.service_times.append(self.service_time())
        
        if len(self.cumulative_service_times) == 0:
            self.cumulative_service_times = [ self.service_times[-1]+time ]
        else:
            self.cumulative_service_times.append( \
                max( self.service_times[-1] + self.cumulative_service_times[-1],  \
                    self.service_times[-1] + time) )
    
    def length(self, time):
        return sum([1 for t in self.arrival_times if t <= time ]) \
            - sum([1 for t in self.cumulative_service_times if t <= time ])
    
    def service_time(self):
        return random.uniform(0.0, self.service_parameters)

class SuperMarket:
    
    def __init__(self, Lambda, Queue_arguements, n_Queues=3):
        
        self.n_Queues = n_Queues
        self.Queues = [Queue(Queue_arguements ) for k in range(self.n_Queues)]
        self.arrival_times = PoissonProcess(Lambda = Lambda)
    
    def choose_queue(self, ):
        return random.randint(0,self.n_Queues-1)
    
    def reset(self, ):
        for q in self.Queues:
            q.reset()
        
        self.arrival_times.reset()
    
    def sample(self, ):
        self.reset()
        
        max_customers = 20
        n_customers = 0
        
        time_step = 0.1
        time_index = 0
        time = 0.0
        while n_customers < max_customers:
            
            N_time = self.arrival_times.sample_path(time)
            while n_customers < N_time and n_customers < max_customers:
                
                self.Queues[self.choose_queue()].arrival( \
                    self.arrival_times.cumulative_times[-(N_time - n_customers) -1])
                n_customers += 1
            
            time_index += 1
            time = time_step*time_index




















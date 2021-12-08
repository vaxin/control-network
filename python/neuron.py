import time
import numpy as np

N_DELAY = 10 # s

class Neuron():
    neurons = set()
    connections = {}
    cache = {}

    @staticmethod
    def get_neuron(id):
        return Neuron.cache.get(id)

    @staticmethod
    def refresh_all():
        for n in Neuron.neurons:
            n.refresh()

    @staticmethod
    def print_network():
        for key in Neuron.connections:
            print(key)
        
    def __init__(self, id):
        self.id = id
        self.a = 0.0
        self.time_queue = [0.0] * N_DELAY
        self.extra = 0.0 # 可人工干预的输入
        # self.ts = time.time()
        self.ups = set()
        self.downs = set()
        Neuron.neurons.add(self)
        Neuron.cache[id] = self
        

    def connect(self, neuron):
        neuron.ups.add(self)
        self.downs.add(neuron)
        Neuron.connections['->'.join([ str(self.id), str(neuron.id)])] = (self, neuron)

    def active(self, a = 1.0):
        self.extra = max(-1.0, min(1.0, a))

    def deactive(self):
        self.extra = 0.0

    def refresh(self):
        x = [ up.output() for up in self.ups ] + [ self.extra ]
        i = self.activation(x)
        self.time_queue.append(i)
        self.a = self.time_queue.pop(0)
        
    def output(self):
        return self.a

    def activation(self, x):
        return min(max(-1.0, np.sum(x)), 1.0)

    

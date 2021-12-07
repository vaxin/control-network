import time
import numpy as np

N_DELAY = 10 # s

class Neuron():
    neurons = set()

    @staticmethod
    def refresh_all():
        for n in Neuron.neurons:
            n.refresh()
        
    def __init__(self, id):
        self.id = id
        self.a = 0.0
        self.time_queue = [0.0] * N_DELAY
        self.extra = 0.0 # 可人工干预的输入
        # self.ts = time.time()
        self.ups = set()
        self.downs = set()
        Neuron.neurons.add(self)

    def connect(self, neuron):
        neuron.ups.add(self)
        self.downs.add(neuron)

    def active(self):
        self.extra = 1.0

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

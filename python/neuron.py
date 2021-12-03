import time
import numpy as np

DELAY = 1 # ms

class Neuron():
    def __init__(self):
        self.a = 0.0
        self.input = 0.0 # direct input
        self.ts = time.time()
        self.ups = set()
        self.downs = set()

    def connect(self, neuron):
        neuron.ups.add(neuron)
        self.downs.add(neuron)

    def active(self):
        self.input = 1.0

    def refresh(self):
        if self.input > 0:
            i = self.input
            self.input = 0.0
        else:
            i = self.activation([ up.output() for up in self.ups ])

        #print('refresh', i, self.a, self.ts, time.time(), time.time() - self.ts)
        if self.a - 0.0 < 0.0001 and i > 0 or time.time() - self.ts > DELAY:
            print('set a=', i)
            self.a = i
            self.ts = time.time()
        
    def output(self):
        return self.a

    def activation(self, x):
        return min(max(-1.0, np.sum(x)), 1.0)

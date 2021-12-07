import time
from neuron import Neuron

class World():
    def __init__(self):
        self.build_network()        

    def build_network(self):
        self.neurons = []
        last_neuron = None
        self.motion_neuron = Neuron(100)
        for i in range(40):
            n = Neuron(i)
            self.neurons.append(n)
            #n.connect(self.motion_neuron) # all neurons active motion neuron
            if last_neuron is not None:
                last_neuron.connect(n)
            last_neuron = n
        last_neuron.connect(self.motion_neuron)

    def refresh(self):
        Neuron.refresh_all()
    
    def show(self):
        print("".join([ str(int(neuron.output())) for neuron in self.neurons ]) + ",motion=" + str(self.motion_neuron.output()), end="\r")

    def get_motion_neuron_value(self):
        return self.motion_neuron.output()

import _thread
world = World()
def loop():
    while True:
        world.refresh()
        world.show()
        time.sleep(0.001)

def start_world():
    _thread.start_new_thread(loop, ())

def start_act():
    _thread.start_new_thread(rand_act, ())

def start():
    start_world()
    start_act()

import random
def rand_act():
   count = 0
   while count < 100:
      time.sleep(2)
      world.neurons[0].active()
      time.sleep(0.5)
      world.neurons[0].deactive()
      count += 1

if __name__ == '__main__':
    start_act()
    loop()

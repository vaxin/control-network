import time
from neuron import Neuron

class World():
    def __init__(self):
        self.build_network()        

    def build_network(self):
        self.neurons = []
        last_neuron = None
        for i in range(40):
            n = Neuron(i)
            self.neurons.append(n)
            if last_neuron is not None:
                last_neuron.connect(n)
            last_neuron = n

    def refresh(self):
        for neuron in self.neurons:
            neuron.refresh()
    
    def show(self):
        print("".join([ str(int(neuron.output())) for neuron in self.neurons ]), end="\r")


world = World()
def main():
    while True:
        world.refresh()
        world.show()
        time.sleep(0.001)

import random
def rand_act():
   count = 0
   while count < 50:
      time.sleep(2)
      world.neurons[0].active()
      time.sleep(0.5)
      world.neurons[0].deactive()
      count += 1

if __name__ == '__main__':
    import _thread
    _thread.start_new_thread(rand_act, ())
    main()
    
import time
from neuron import Neuron

class World():
    def __init__(self):
        neuron1 = Neuron()
        neuron2 = Neuron()
        self.neurons = [ neuron1, neuron2 ]
        neuron1.connect(neuron2)

    def refresh(self):
        for neuron in self.neurons:
            neuron.refresh()
    
    def show(self):
        print([ neuron.output() for neuron in self.neurons ], end="\r")
    
    def active(self):
        self.neurons[0].active()
        
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
      time.sleep(random.random() * 10)
      world.active()
      print('active neuron 1')
      count += 1

if __name__ == '__main__':
    import _thread
    _thread.start_new_thread(rand_act, ())
    main()
    
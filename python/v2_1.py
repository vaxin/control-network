import time
from neuron import Neuron

class World():
    def __init__(self):
        self.neurons = []
        self.build_network()

    def build_link(self, prefix, length):
        last_neuron = None
        motion_neuron = Neuron(prefix + length)
        
        for i in range(length):
            n = Neuron(prefix + i)
            n.connect(motion_neuron)
            self.neurons.append(n)
            if last_neuron is not None:
                last_neuron.connect(n)
            last_neuron = n

    def build_network(self):
        self.build_link(100, 20)
        self.build_link(200, 20)
        self.build_link(300, 20)

    def refresh(self):
        Neuron.refresh_all()
    
    def show(self):
        print("".join([ str(int(neuron.output())) for neuron in self.neurons ]), end="\r")

    def get_neuron_value(self, id):
        n = Neuron.get_neuron(id)
        if n is not None:
            return n.output()
        return 0


import _thread
world = World()
def loop():
    while True:
        world.refresh()
        world.show()
        time.sleep(0.001)

def start_world():
    _thread.start_new_thread(loop, ())

def start():
    start_world()

cache = {}
def __active(index, a, delay):
    if abs(a) < 0.001:
        return
    
    n = Neuron.get_neuron(index)
    if n is None:
        return

    cache[index] = True
    n.active(a)
    time.sleep(delay)
    n.deactive()
    cache[index] = False

def active(index, a, delay):
     # 暂时避免重复刺激，否则会不停地创建线程
    if cache.get(index, False) is True:
        return

    _thread.start_new_thread(__active, (index, a, delay))

if __name__ == '__main__':
    start()
    Neuron.print_network()

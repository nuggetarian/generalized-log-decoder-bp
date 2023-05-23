from config import BATCH_SIZE
from modules.array_queue import ArrayQueue
from concurrent.futures import ThreadPoolExecutor
import copy
from modules.neural_network import NeuralNetwork

queue = ArrayQueue()
ai = NeuralNetwork()

class BatchMode():
    
    def __init__(self):
            self.logArray = []
            
    def process(self,data): 
        self.logArray.append(data)
        
        def if_batch_larger():
            if len(self.logArray) >= BATCH_SIZE:
                queue.append(copy.deepcopy(self.logArray))
                self.logArray.clear()
             
        def if_queue_not_empty():
            if queue.size() > 0:
                # ai.predict(queue.get())
                print(queue.get())
            
        executor = ThreadPoolExecutor(max_workers=2)
        
        executor.submit(if_batch_larger)
        executor.submit(if_queue_not_empty) 
        
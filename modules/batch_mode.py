from config import BATCH_SIZE
from modules.array_queue import ArrayQueue
from concurrent.futures import ThreadPoolExecutor
import copy
from modules.neural_network import NeuralNetwork

queue = ArrayQueue()
ai = NeuralNetwork()

class BatchMode():
    
    def __init__(self): # Konstruktor docasnych arrayov
            self.logArray = []
            
    def process(self,data): 
        self.logArray.append(data) # Pridanie do docasneho array
        
        def if_batch_larger():
            if len(self.logArray) >= BATCH_SIZE: # Ak je docasny array vacsi alebo rovny batch_size, je jeho kopia pridana do queue
                queue.append(copy.deepcopy(self.logArray))
                self.logArray.clear() # Docasny array je vycisteny a pripraveny aby bol z neho dalsi batch
             
        def if_queue_not_empty(): # Ak queue nieco obsahuje, tak postupne posiela svoj obsah batchov do neuronovej siete
            if queue.size() > 0:
                # ai.predict(queue.get()) # <==== Zakomentovana funkcia, v ktorej by ai predikovalo na zaklade array
                print(queue.get()) # <==== Odkomentovana funkcia, ktora demonstruje fungovanie queue
            
        executor = ThreadPoolExecutor(max_workers=2) # <==== Vlakna na jednotlive funkcie
        
        executor.submit(if_batch_larger)
        executor.submit(if_queue_not_empty) 
        
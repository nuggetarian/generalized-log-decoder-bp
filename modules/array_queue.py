class ArrayQueue:
    # Konstruktor obsahujuci array pouzity na queue
    def __init__(self):
        self.queue = []
    
    # Pridanie polozky do queue
    def append(self, item):
        self.queue.append(item)
    
    # Ziskanie polozky z queue + vymazanie prvej polozky
    def get(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    # Overenie prazdnosti queue
    def is_empty(self):
        return len(self.queue) == 0
    
    # Velkost queue
    def size(self):
        return len(self.queue)
    
    # Vypis queue
    def display(self):
        return self.queue
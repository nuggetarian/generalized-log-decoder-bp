from datetime import datetime

class Logger:
    
    # Urovne logu
    levels = {
        1: '[DEBUG]',
        2: '[INFO]',
        3: '[WARNING]',
        4: '[ERROR]',
        5: '[CRITICAL]'
    }
    
    # Funkcia na vytvorenie logu na zaklade vstupnych parametrov
    def makeLog(self, level, usedClass, message):
        time = datetime.now()
        current = time.strftime("%H:%M:%S")
        # Log obsahuje sucasny cas, zadanu uroven, triedu kde sa dana udalost vykonala a spravu
        log = f"[{current}] {self.levels.get(level)} [{usedClass}] {message}\n"
        print(log)
        with open('activity.log', 'a') as f: # Zapis logu do suboru
            f.write(log)



    
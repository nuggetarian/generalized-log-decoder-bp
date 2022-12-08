from datetime import datetime

class Logger:
        
    levels = {
        1: '[DEBUG]',
        2: '[INFO]',
        3: '[WARNING]',
        4: '[ERROR]',
        5: '[CRITICAL]'
    }

    def makeLog(self, level, usedClass, message):
        time = datetime.now()
        current = time.strftime("%H:%M:%S")
        log = f"[{current}] {self.levels.get(level)} [{usedClass}] {message}\n"
        print(log)
        with open('activity.log', 'a') as f:
            f.write(log)



    
class Logger:
        
    levels = {
        1: '[DEBUG]',
        2: '[INFO]',
        3: '[WARNING]',
        4: '[ERROR]',
        5: '[CRITICAL]'
    }

    def makeLog(self, level, message):
        log = f"{self.levels.get(level)}: {message}"
        print(log)
        with open('activity.log', 'a') as f:
            f.write(log)



    
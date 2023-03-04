import json
from config import BATCH_SIZE
from modules.logger import Logger
from os.path import exists

class Linux:
    syslogArray = []
    logger = Logger()
    
    #Funkcia na pridanie syslog logu do pola
    def arraySyslogAppend(self, data):
        self.syslogArray.append(data)
    
    #Getter na syslog pole
    def getSyslogArray(self):
        return self.syslogArray
    
    def dumpSyslogLogs(self, system, code):
        try:
            with open(f'exported\\{system}\\syslogbatch{code}.json', 'w') as f:
                json.dump(self.getSyslogArray(), f)
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")  
            
    def saveLinuxLog(self, system, data, code):
        if len(self.syslogArray) < BATCH_SIZE and not exists(f'exported\\{system}\\syslogbatch{code}.json'): #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
            
            self.arraySyslogAppend(data) #Pridanie logu do pola
        elif exists(f'exported\\{system}\\syslog_{code}-batch_{BATCH_SIZE}.json'):
            print("File already exists")
        else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
            self.arraySyslogAppend(data)
            self.dumpSyslogLogs(system, code)
            self.syslogArray.clear() #Vycisti sa pole   
            self.logger.makeLog(2, "log_array" , f"Syslog log file created with a batch size of {BATCH_SIZE}")
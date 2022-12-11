import json
from config import BATCH_SIZE
from modules.logger import Logger

WINDOWSNAMENUMBER = 1 #Globalna premenna na pocitanie cisla suboru
SYSLOGNAMENUMBER = 1

class LogArray:
    #Deklaracie
    logger = Logger()
    winlogArray = []
    syslogArray = []
    
    
    #Funkcia na pridanie windows logu do pola
    def arrayWinAppend(self, data):
        self.winlogArray.append(json.loads(data))

    #Funkcia na pridanie syslog logu do pola
    def arraySyslogAppend(self, data):
        self.syslogArray.append(json.loads(data))
    
    #Getter na windows pole
    def getWinArray(self):
        return self.winlogArray

    #Getter na syslog pole
    def getSyslogArray(self):
        return self.syslogArray
    
    #Ulozenie pola logov do suboru s cislom globalnej premennej   
    def dumpWinLogs(self, system, number):
        with open(f'exported\\{system}\\winlogbatch{number}.json', 'w') as f:
            json.dump(self.getWinArray(), f)
            # Pridat try catch

    #Ulozenie pola logov do suboru s cislom globalnej premennej   
    def dumpSyslogLogs(self, system, number):
        with open(f'exported\\{system}\\syslogbatch{number}.json', 'w') as f:
            json.dump(self.getSyslogArray(), f)
            # Pridat try catch        
    
    #Funkcia ktora na zaklade batch size zapise pocet logov do .json suboru
    def saveLogs(self, system, data):
        global WINDOWSNAMENUMBER
        global SYSLOGNAMENUMBER
        # Typ Systemu
        if system == "windows":
            if len(self.winlogArray) < BATCH_SIZE: #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
                self.arrayWinAppend(data) #Pridanie logu do pola
            else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
                self.arrayWinAppend(data)
                self.dumpWinLogs(system, WINDOWSNAMENUMBER)
                WINDOWSNAMENUMBER = WINDOWSNAMENUMBER + 1
                self.winlogArray.clear() #Vycisti sa pole
                self.logger.makeLog(2, "log_array" , f"Windows log file created with a batch size of {BATCH_SIZE}")
        elif system == "linux":
            if len(self.syslogArray) < BATCH_SIZE: #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
                self.arraySyslogAppend(data) #Pridanie logu do pola
            else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
                self.arraySyslogAppend(data)
                self.dumpSyslogLogs(system, SYSLOGNAMENUMBER)
                SYSLOGNAMENUMBER = SYSLOGNAMENUMBER + 1
                self.syslogArray.clear() #Vycisti sa pole
                self.logger.makeLog(2, "log_array" , f"Syslog log file created with a batch size of {BATCH_SIZE}")

    
            








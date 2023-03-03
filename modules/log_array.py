import json
from config import BATCH_SIZE
from modules.logger import Logger
from os.path import exists

WINDOWSNAMENUMBER = 1 #Globalna premenna na pocitanie cisla suboru
SYSLOGNAMENUMBER = 1
OTHERNAMENUMBER = 1

class LogArray:
    #Deklaracie
    logger = Logger()
    winlogArray = []
    syslogArray = []
    
    
    #Funkcia na pridanie windows logu do pola
    def arrayWinAppend(self, data):
        self.winlogArray.append(data)

    #Funkcia na pridanie syslog logu do pola
    def arraySyslogAppend(self, data):
        self.syslogArray.append(data)
    
    #Getter na windows pole
    def getWinArray(self):
        return self.winlogArray

    #Getter na syslog pole
    def getSyslogArray(self):
        return self.syslogArray
    
    #Ulozenie pola logov do suboru s cislom globalnej premennej   
    def dumpWinLogs(self, system, code):
        try:
            with open(f'exported\\{system}\\winlog_{code}_batch_{BATCH_SIZE}.json', 'w') as f:
                json.dump(self.getWinArray(), f)
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")
            # Pridat try catch

    #Ulozenie pola logov do suboru s cislom globalnej premennej   
    def dumpSyslogLogs(self, system, code):
        try:
            with open(f'exported\\{system}\\syslogbatch{code}.json', 'w') as f:
                json.dump(self.getSyslogArray(), f)
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")
            # Pridat try catch        
    
    #Funkcia ktora na zaklade batch size zapise pocet logov do .json suboru
    def saveLogs(self, system, data, code):
        global OTHERNAMENUMBER
        # Typ Systemu
        if system == "windows": # Ak ide o log z windows stanice
            if len(self.winlogArray) < BATCH_SIZE and not exists(f'exported\\{system}\\winlog_{code}-batch_{BATCH_SIZE}.json'): #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
                self.arrayWinAppend(data) #Pridanie logu do pola
            elif exists(f'exported\\{system}\\winlog_{code}-batch_{BATCH_SIZE}.json'):
                print("File already exists")
            else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
                self.arrayWinAppend(data)
                self.dumpWinLogs(system, code)
                self.winlogArray.clear() #Vycisti sa pole
                self.logger.makeLog(2, "log_array" , f"Windows log file created with a batch size of {BATCH_SIZE}")
        elif system == "linux": # Ak ide o log z linux stanice
            if len(self.syslogArray) < BATCH_SIZE and not exists(f'exported\\{system}\\syslogbatch{code}.json'): #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
                self.arraySyslogAppend(data) #Pridanie logu do pola
            else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
                self.arraySyslogAppend(data)
                self.dumpSyslogLogs(system, code)
                self.syslogArray.clear() #Vycisti sa pole   
                self.logger.makeLog(2, "log_array" , f"Syslog log file created with a batch size of {BATCH_SIZE}")
        elif system == "other":
            try:
                with open(f'exported\\{system}\\other{OTHERNAMENUMBER}_batch_1.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))
                self.logger.makeLog(2, "log_array" , f"Other log file created with a batch size of 1")
                OTHERNAMENUMBER = OTHERNAMENUMBER + 1
            except:
                self.logger.makeLog(4, "log_array", "File Creation Failed")
            

    
            








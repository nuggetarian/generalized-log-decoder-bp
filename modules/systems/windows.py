import json
from config import BATCH_SIZE
from modules.logger import Logger
from os.path import exists

class Windows:
    winlogArray = []
    logger = Logger()
    
    #Funkcia na pridanie windows logu do pola
    def arrayWinAppend(self, data):
        self.winlogArray.append(data)
        
    #Getter na windows pole
    def getWinArray(self):
        return self.winlogArray
    
    #Ulozenie pola logov do suboru s cislom globalnej premennej   
    def dumpWinLogs(self, system, code):
        try:
            with open(f'exported\\{system}\\winlog_{code}_batch_{BATCH_SIZE}.json', 'w') as f:
                json.dump(self.getWinArray(), f)
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")
            # Pridat try catch
        
    def saveWinLog(self, system, data, code):
        if len(self.winlogArray) < BATCH_SIZE and not exists(f'exported\\{system}\\winlog_{code}-batch_{BATCH_SIZE}.json'): #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
            self.arrayWinAppend(data) #Pridanie logu do pola
        elif exists(f'exported\\{system}\\winlog_{code}-batch_{BATCH_SIZE}.json'):
            print("File already exists")
        else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
            self.arrayWinAppend(data)
            self.dumpWinLogs(system, code)
            self.winlogArray.clear() #Vycisti sa pole
            self.logger.makeLog(2, "log_array" , f"Windows log file created with a batch size of {BATCH_SIZE}")
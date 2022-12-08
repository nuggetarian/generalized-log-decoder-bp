import json
from config import BATCH_SIZE
from modules.logger import Logger

NAMENUMBER = 1 #Globalna premenna na pocitanie cisla suboru

class LogArray:
    #Deklaracie
    logger = Logger()
    logArray = []
    
    #Funkcia na pridanie logu do pola
    def arrayAppend(self, data):
        self.logArray.append(json.loads(data))
    
    #Getter na pole
    def getArray(self):
        return self.logArray
    
    #Ulozenie pola logov do suboru s cislom globalnej premennej   
    def dumpLogs(self, number):
        with open(f'exported\\data{number}.json', 'w') as f:
            json.dump(self.getArray(), f)
            # Pridat try catch
    
    #Funkcia ktora na zaklade batch size zapise pocet logov do .json suboru
    def saveLogs(self, data):
        global NAMENUMBER
        if len(self.logArray) < BATCH_SIZE: #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
            self.arrayAppend(data) #Pridanie logu do pola
        else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
            self.arrayAppend(data)
            self.dumpLogs(NAMENUMBER)
            NAMENUMBER = NAMENUMBER + 1
            self.logArray.clear() #Vycisti sa pole
            self.logger.makeLog(2, "log_array" , f"File created with a batch size of {BATCH_SIZE}")
            








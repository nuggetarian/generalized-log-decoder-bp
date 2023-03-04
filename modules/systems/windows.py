import json
from config import BATCH_SIZE
from modules.logger import Logger
from os.path import exists

class Windows:
    winlogArray = []
    logger = Logger()
    dictionary = {}
    
    #Funkcia na pridanie windows logu do pola
    # def arrayWinAppend(self, data):
    #     self.winlogArray.append(data)
        
    # #Getter na windows pole
    # def getWinArray(self):
    #     return self.winlogArray
    
    #Ulozenie pola logov do suboru s cislom globalnej premennej
    def createArray(self, code):
        var_name = 'array_' + code
        self.dictionary[var_name] = [] 
        
    def getArray(self, code):
        return self.dictionary.get(f"array_{code}")

    def dumpWinLogs(self, system, code):
        try:
            with open(f'exported\\{system}\\winlog_{code}_batch_{BATCH_SIZE}.json', 'w') as f:
                json.dump(self.dictionary[f'array_{code}'], f)
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")
            # Pridat try catch
        
    def saveWinLog(self, system, data, code):
        if self.getArray(code) is None:
            self.createArray(code)
            self.dictionary[f'array_{code}'].append(data)
            print(f"Code of incoming log: {code}, Length of Array: {len(self.dictionary[f'array_{code}'])}")
            # print(self.dictionary[f'array_{code}'])
        else:
            
        # new_array = [code]
        # var_name = 'array_' + code
        # self.new_arrays[var_name] = new_array
        
        # print(self.new_arrays[f'array_{code}'])
            
            # self.new_arrays[f'array_{code}'] = new_array
            if len(self.dictionary[f'array_{code}']) < BATCH_SIZE and not exists(f'exported\\{system}\\winlog_{code}-batch_{BATCH_SIZE}.json'): #Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola
                # self.arrayWinAppend(data) #Pridanie logu do pola
                self.dictionary[f'array_{code}'].append(data)
                print(f"Code of incoming log: {code}, Length of Array: {len(self.dictionary[f'array_{code}'])}")
                print(self.dictionary.keys())
                # print(self.new_arrays[f'array_{code}'])
            elif exists(f'exported\\{system}\\winlog_{code}-batch_{BATCH_SIZE}.json'):
                print("File already exists")
            else: #Inak sa logy ulozia do suboru a inkrementuje sa cislo ktore pojde do nazvu buduceho suboru
                # self.arrayWinAppend(data)
                self.dumpWinLogs(system, code)
                self.dictionary[f'array_{code}'].clear() #Vycisti sa pole
                self.logger.makeLog(2, "log_array" , f"Windows log file created with a batch size of {BATCH_SIZE}")
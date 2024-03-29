import json
from config import BATCH_SIZE
from modules.logger import Logger
from os.path import exists

class Linux:
    logger = Logger() # Instancia loggeru
    dictionary = {} # Dictionary pre custom polia podla kodu logu
    
    # Funkcia na tvorbu custom pola podla kodu z logu
    def _createArray(self, code:int) -> None:
        var_name = 'array_' + str(code)
        self.dictionary[var_name] = [] 
    
    # Getter na pole
    def _getArray(self, code:int):
        return self.dictionary.get(f"array_{code}")
    
    # Funkcia na ulozenie pola do suboru
    def _dumpLinuxLogs(self, system:str, code:int) -> None:
        try:
            with open(f'exported\\{system}\\syslog_{code}-batch_{BATCH_SIZE}.json', 'w') as f:
                json.dump(self.dictionary[f'array_{code}'], f)
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")
    
    # Funkcia ua sprostredkovanie vsetkeho
    def saveLinuxLog(self, system:str, data:str, code:int) -> None:
        # Overenie existencie pola, ak neexistuje vytvori sa nove a prida sa donho prvy log
        if self._getArray(code) is None:
            self._createArray(code)
            self.dictionary[f'array_{code}'].append(data)
            print(f"Code of incoming log: {code}, Length of Array: {len(self.dictionary[f'array_{code}'])}")
        # Ak existuje vykona sa pridavanie logov alebo ukladanie
        else:
            # Porovnanie velkosti pola a batch size, ak je mensie pole tak sa log prida do pola, zaroven nesmie uz existovat dany subor
            if len(self.dictionary[f'array_{code}']) < BATCH_SIZE and not exists(f'exported\\{system}\\syslog_{code}-batch_{BATCH_SIZE}.json'): 
                self.dictionary[f'array_{code}'].append(data)
                print(f"Code of incoming log: {code}, Length of Array: {len(self.dictionary[f'array_{code}'])}")
            # Ak subor uz existuje tak sa nic nerobi
            elif exists(f'exported\\{system}\\syslog_{code}-batch_{BATCH_SIZE}.json'):
                print("File already exists")
            # Inak sa logy ulozia do suboru a vycisti sa pole (hoci nemusi kedze sa vytvori custom na kazdy kod)
            else: 
                self._dumpLinuxLogs(system, code)
                self.dictionary[f'array_{code}'].clear() # Vycisti sa pole
                self.logger.makeLog(2, "log_array" , f"Linux log file created with a batch size of {BATCH_SIZE}")
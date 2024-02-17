import json
from modules.logger import Logger
import os

SIMILAR = 0 # Globalna premenna na test ci log s takymi klucmi uz existuje
OTHERNAMENUMBER = 1 # Globalna premenna na pocitanie cisla suboru

class Other:
    logger = Logger()
    
    def _compare(self, json1, json2) -> bool: # Funkcia porovnania JSON klucov
        if set(json1.keys()) == set(json2.keys()):
            return True
        else:
            return False
            
    def _cycleFiles(self, data:str) -> None: # Cyklovanie suborov
        global SIMILAR
        count = 0
        dir_path = f'exported\\other'
        for path in os.scandir(dir_path):
            if path.is_file():
                count += 1
    
        for i in range(count): # For loop na porovnanie suborov a ich klucov
            with open(f'exported\\other\\other{i+1}_batch_1.json') as json_file:
                json1 = json.load(json_file)
                if self._compare(json1, data) == True: # Premenna udrziavajuca to, ze su kluce podobne
                            SIMILAR = SIMILAR + 1
                           
    def saveOtherLog(self, system:str, data:str) -> None:
        self._cycleFiles(data) 
        global SIMILAR
        global OTHERNAMENUMBER        
        if SIMILAR == 0: # Ak nie su kluce podobne, tak sa ulozi subor o batch size 1
            try:
                with open(f'exported\\{system}\\other{OTHERNAMENUMBER}_batch_1.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))
                self.logger.makeLog(2, "log_array" , f"Other log file created with a batch size of 1")
                OTHERNAMENUMBER = OTHERNAMENUMBER + 1
            except:
                self.logger.makeLog(4, "log_array", "File Creation Failed")
        elif SIMILAR >= 1:
            SIMILAR = 0   
        
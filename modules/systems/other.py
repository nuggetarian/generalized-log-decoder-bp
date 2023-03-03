import json
from config import BATCH_SIZE
from modules.logger import Logger
from os.path import exists
import os

class Other:
    logger = Logger()
    
    def compare(self, json1, json2):
        if set(json1.keys()) == set(json2.keys()):
            return True
        else:
            return False
            
    
    def cycleFiles(self):
        count = 0
        dir_path = f'exported\\other'
        for path in os.scandir(dir_path):
            if path.is_file():
                count += 1
        
        for i in count:
            with open(f'exported\\other\\other{i}_batch_1.json') as json_file:
                json1 = json.load(json_file)
                for f in count:
                    with open(f'exported\\other\\other{f}_batch_1.json') as json_file:
                        json2 = json.load(json_file)
                    if self.compare(json1, json2) == True:
                        print("Same file")
                    
                    
    def saveOtherLog(self, system, data):
        try:
            with open(f'exported\\{system}\\other{OTHERNAMENUMBER}_batch_1.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))
            self.logger.makeLog(2, "log_array" , f"Other log file created with a batch size of 1")
            OTHERNAMENUMBER = OTHERNAMENUMBER + 1
        except:
            self.logger.makeLog(4, "log_array", "File Creation Failed")
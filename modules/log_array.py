import json
from modules.logger import Logger
from modules.systems.windows import Windows
from modules.systems.linux import Linux

OTHERNAMENUMBER = 1 #Globalna premenna na pocitanie cisla suboru

class LogArray:
    #Deklaracie
    logger = Logger()
    windowsLog = Windows()
    linuxLog = Linux()
     
    #Funkcia ktora na zaklade batch size zapise pocet logov do .json suboru
    def saveLogs(self, system, data, code):
        global OTHERNAMENUMBER
        # Typ Systemu
        if system == "windows": # Ak ide o log z windows stanice
            self.windowsLog.saveWinLog(system, data, code)
            
        elif system == "linux": # Ak ide o log z linux stanice
            self.linuxLog.saveLinuxLog(system, data, code)
            
        elif system == "other":
            try:
                with open(f'exported\\{system}\\other{OTHERNAMENUMBER}_batch_1.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))
                self.logger.makeLog(2, "log_array" , f"Other log file created with a batch size of 1")
                OTHERNAMENUMBER = OTHERNAMENUMBER + 1
            except:
                self.logger.makeLog(4, "log_array", "File Creation Failed")
            

    
            








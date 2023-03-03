import json
from modules.logger import Logger
from modules.systems.windows import Windows
from modules.systems.linux import Linux
from modules.systems.other import Other

OTHERNAMENUMBER = 1 #Globalna premenna na pocitanie cisla suboru

class LogArray:
    #Deklaracie
    logger = Logger()
    windowsLog = Windows()
    linuxLog = Linux()
    otherLog = Other()
    
    #Funkcia ktora na zaklade batch size zapise pocet logov do .json suboru
    def saveLogs(self, system, data, code):
        
        # Typ Systemu
        if system == "windows": # Ak ide o log z windows stanice
            self.windowsLog.saveWinLog(system, data, code)
            
        elif system == "linux": # Ak ide o log z linux stanice
            self.linuxLog.saveLinuxLog(system, data, code)
            
        elif system == "other": # Ak ide o log ktory je neznamy
            self.otherLog.saveOtherLog(system, data)
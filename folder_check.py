import os

class FolderCheck():
    current_working_directory = os.getcwd()
    
    def check(self):       
        if os.path.exists("exported"): 
            pass
        elif not os.path.exists("exported"):
            os.mkdir("exported")
            print("directory 'exported' created")
        
        if os.path.exists("exported\\linux"): 
            pass
        elif not os.path.exists("exported\\linux"):
            os.mkdir("exported\\linux")
            print("directory 'exported\linux' created")
            
        if os.path.exists("exported\\windows"): 
            pass
        elif not os.path.exists("exported\\windows"):
            os.mkdir("exported\\windows")
            print("directory 'exported\windows' created")
            
        if os.path.exists("exported\\other"): 
            pass
        elif not os.path.exists("exported\\other"):
            os.mkdir("exported\\other")
            print("directory 'exported\other' created")
            
        if os.path.exists("modules\\model"): 
            pass
        elif not os.path.exists("modules\\model"):
            os.mkdir("modules\\model")
            print("directory 'modules\model' created")
            
    def checkAnonymized(self):
        if os.path.exists("anonymized"): 
            pass
        elif not os.path.exists("anonymized"):
            os.mkdir("anonymized")
            print("directory 'anonymized' created")
        
        if os.path.exists("anonymized\\exported"): 
            pass
        elif not os.path.exists("anonymized\\exported"):
            os.mkdir("anonymized\\exported")
            print("directory 'anonymized\exported' created")
            
        if os.path.exists("anonymized\\exported\\windows"): 
            pass
        elif not os.path.exists("anonymized\\exported\\windows"):
            os.mkdir("anonymized\\exported\\windows")
            print("directory 'anonymized\exported\windows' created")
            
        if os.path.exists("anonymized\\exported\\linux"): 
            pass
        elif not os.path.exists("anonymized\\exported\\linux"):
            os.mkdir("anonymized\\exported\\linux")
            print("directory 'anonymized\exported\linux' created")
            
        if os.path.exists("anonymized\\exported\\other"): 
            pass
        elif not os.path.exists("anonymized\\exported\\other"):
            os.mkdir("anonymized\\exported\\other")
            print("directory 'anonymized\exported\other' created")
            
        
        
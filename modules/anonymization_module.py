import os

directory = f'exported'
class AnonymizeForward:

    def anonymize(self): # For loop prechadzajuci vsetky subory v danom priecinku a ziskavanie ich cesty
        r = []
        for root, dirs, files in os.walk(directory):
            for name in files:
                r.append(os.path.join(root, name))
        return r
    

import json

class Beautify:
    
    def beautify(self, data): # Funkcia na zarovnanie JSON logu
        s = json.dumps(data, indent=4, sort_keys=True) # Konverzia do JSON, s odsadenim 4 medzery a zoradenim klucov
        return s
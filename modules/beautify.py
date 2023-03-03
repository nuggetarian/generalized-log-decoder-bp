import json

class Beautify:
    
    # Funkcia na zarovnanie JSON logu
    def beautify(self, data):
        # Nastavit timer zaciatok sem
        normalized = data.decode('utf-8') #Dekodovanie na zaklade utf-8 kodovania
        data = json.loads(normalized) #Nacitanie dekodovanych dat do premennej
        s = json.dumps(data, indent=4, sort_keys=True) #Konverzia do JSON, s odsadenim 4 medzery a zoradenim klucov
        return s
        # Nastavit time koniec sem, mozno zalogovat
import json

class Beautify:
    
    # Funkcia na zarovnanie JSON logu
    def beautify(self, data):
        normalized = data.decode('utf-8')
        data = json.loads(normalized)
        s = json.dumps(data, indent=4, sort_keys=True)
        return s


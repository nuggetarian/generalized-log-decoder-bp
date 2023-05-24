from modules.log_array import LogArray

arraylog = LogArray()

class Comparator:
        
    def compare(self, data): # Zistovanie ci logy obsahuju urcite kluce, na zaklade ktorych su posunute do ich vlastnych modulov
        if ('host' in data and 'os' in data['host'] and 'family' in data['host']['os'] and data['host']['os']['family'] == "windows"):
            print("windows Log Received.")
            wincode = data['winlog']['event_id']
            arraylog.saveLogs("windows", data, wincode)
        elif ('log' in data and data['log']['syslog']):
            print("Syslog Log Received.")
            syscode = data['log']['syslog']['severity']['code']
            arraylog.saveLogs("linux", data, syscode)
        else:
            arraylog.saveLogs("other", data, 1)

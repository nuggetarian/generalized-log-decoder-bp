from modules.log_array import LogArray

arraylog = LogArray()

class Comparator:
    
    def compare(self, data):
        # try:
            if ('host' in data and 'os' in data['host'] and 'family' in data['host']['os'] and data['host']['os']['family'] == "windows"):
                # print(data)
                print("windows Log Received.")
                wincode = data['winlog']['event_id']
                print(wincode)
                arraylog.saveLogs("windows", data, wincode)
            elif ('log' in data and data['log']['syslog']):
                # print(data)
                print("Syslog Log Received.")
                syscode = data['log']['syslog']['severity']['code']
                arraylog.saveLogs("linux", data, syscode)
            else:
                # print(data)
                arraylog.saveLogs("other", data, 1)
        # except:
        #      print("Possibly not a JSON.")
            
            
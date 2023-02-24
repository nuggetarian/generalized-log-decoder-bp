from modules.log_array import LogArray

arraylog = LogArray()

class Comparator:
    
    def compare(self, resp, s):
        try:
            if ('host' in resp and 'os' in resp['host'] and 'family' in resp['host']['os'] and resp['host']['os']['family'] == "windows"):
                print(s)
                print("windows Log Received.")
                wincode = resp['winlog']['event_id']
                print(wincode)
                arraylog.saveLogs("windows", s, wincode)
            elif ('log' in resp and resp['log']['syslog']):
                print(s)
                print("Syslog Log Received.")
                syscode = resp['log']['syslog']['severity']['code']
                arraylog.saveLogs("linux", s, syscode)
            else:
                print("It works!!")
                arraylog.saveLogs("other", s, 1)
        except:
            print("Possibly not a JSON.")
            
            
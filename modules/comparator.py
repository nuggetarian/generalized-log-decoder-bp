from modules.log_array import LogArray

arraylog = LogArray()

class Comparator:
    
    def compare(self, resp, s):
        if ('host' in resp and 'os' in resp['host'] and 'family' in resp['host']['os'] and resp['host']['os']['family'] == "windows"):
            print(s)
            print("windows Log Received.")
            arraylog.saveLogs("windows", s)
        elif ('log' in resp and resp['log']['syslog']):
            print(s)
            print("Syslog Log Received.")
            arraylog.saveLogs("linux", s)
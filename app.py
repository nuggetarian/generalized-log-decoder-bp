from flask import Flask, request
from modules.beautify import Beautify
from modules.log_array import LogArray
import json
from modules.logger import Logger

app = Flask(__name__)
# Vytvaranie instancii objektov
logger = Logger()
beautifier = Beautify()
arraylog = LogArray()

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():   
    data = request.data # Ziskava raw data
    s = beautifier.beautify(data) # Funkcia na odsadenie JSON
    resp = json.loads(s)
    # Filter na zaklade operacneho systemu
    if ('host' in resp and 'os' in resp['host'] and 'family' in resp['host']['os'] and resp['host']['os']['family'] == "windows"):
        print(s)
        print("windows Log Received.")
        print(resp['host']['os']['family'])
        arraylog.saveLogs("windows", s)
    elif ('log' in resp and resp['log']['syslog']):
        print(s)
        print("Syslog Log Received.")
        arraylog.saveLogs("linux", s)
    return s
    

if __name__ == '__main__':
	app.run()
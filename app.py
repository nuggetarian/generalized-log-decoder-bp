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
    #Filter na zaklade stanice
    if resp['host']['hostname'] == "miri":
        print(s)
        print("Miri Log Received.")
        arraylog.saveLogs("linux", s)
    if resp['host']['hostname'] == "radka":
        print(s)
        print("Radka Log Received.")
        arraylog.saveLogs("windows", s)
    if resp['host']['hostname'] == "regina":
        print(s)
        print("Regina Log Received.")
        arraylog.saveLogs("windows", s)
    return s
    

if __name__ == '__main__':
	app.run()
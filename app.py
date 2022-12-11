from flask import Flask, request
from modules.beautify import Beautify
from modules.log_array import LogArray
import json

app = Flask(__name__)

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():
    beautifier = Beautify()
    arraylog = LogArray()
    syslogarray = LogArray()
    data = request.data # Ziskava raw data
    s = beautifier.beautify(data) # Funkcia na odsadenie JSON
    #print(s) # Print odsadeneho logu
    #arraylog.saveLogs(s)
    resp = json.loads(s)
    #Filter na zaklade stanice
    if resp['host']['hostname'] == "miri":
        print(s)
        print("Miri Log Received.")
        syslogarray.saveLogs("linux", s)
    if resp['host']['hostname'] == "radka":
        print(s)
        print("Radka Log Received.")
        arraylog.saveLogs("windows", s)
    if resp['host']['hostname'] == "regina":
        print(s)
        print("Regina Log Received.")
        arraylog.saveLogs("windows", s)
    
    # Kod na pouzitie neskor
    # resp = json.loads(s)
    # print(resp['event']['original']) 
    return s
    

if __name__ == '__main__':
	app.run()
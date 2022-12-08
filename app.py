from flask import Flask, request
from modules.beautify import Beautify
from modules.log_array import LogArray
import json

app = Flask(__name__)

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():
    beautifier = Beautify()
    arraylog = LogArray()
    data = request.data # Ziskava raw data
    s = beautifier.beautify(data) # Funkcia na odsadenie JSON
    print(s) # Print odsadeneho logu
    arraylog.saveLogs(s)
    # Kod na pouzitie neskor
    # resp = json.loads(s)
    # print(resp['event']['original']) 
    return s
    

if __name__ == '__main__':
	app.run()
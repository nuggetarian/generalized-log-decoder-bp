from flask import Flask, request
from modules.beautify import Beautify
from modules.log_array import LogArray
import json

app = Flask(__name__)

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():
    beautifier = Beautify()
    arraylog = LogArray()
    # Ziskava raw data
    data = request.data
    s = beautifier.beautify(data)
    # print(s)
    arraylog.saveLogs(s)
    print("===============================================================")
    resp = json.loads(s)
    print(resp['event']['original'])
    return s
    

if __name__ == '__main__':
	app.run()
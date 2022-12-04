from flask import Flask, request, jsonify
from flask_restful import Api
from modules.beautify import Beautify
from modules.log_array import LogArray

app = Flask(__name__)
api = Api(app)



@app.route('/processmsg', methods=['GET','POST'])
def processmsg():
    # Get random raw data
    beautifier = Beautify()
    arraylog = LogArray()
    data = request.data
    s = beautifier.beautify(data)
    print(s)
    arraylog.saveLogs(s)
    return s
    

if __name__ == '__main__':
	app.run()
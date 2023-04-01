from flask import Flask, request
from modules.logger import Logger
from modules.comparator import Comparator
from config import MODE
import requests

app = Flask(__name__)
logger = Logger()
comparator = Comparator()

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():   
    data = request.json # Ziskava json data
    if MODE == 1:
        comparator.compare(data)
    elif MODE == 2:  
        print(data)
    return data

@app.route('/v1/forward-anonymize', methods=['GET', 'POST'])
def fwdAnonymize():
    # url = 'http://localhost:5000/upload'
    # with open(f'exported\\linux\\syslog_6-batch_3.json', 'rb') as f:
    #     res = requests.post(url, files = f)

    # return "bruh"

    # data = request.json
    # res =  requests.post('http://localhost:6000/v1/processmsg', json=data)
    # return data

    data = request.json
    res =  requests.post('http://localhost:5000/acceptjson', json=data)
    return data

    # url = 'http://localhost:29170/v1/upload'
    # with open(f'exported\\linux\\syslog_6-batch_3.json', 'rb') as f:
    #     res = requests.post(url, files = f)

    return "bruh"

@app.route('/v1/upload', methods=['GET', 'POST'])

def upload_file():
    # Get the uploaded file from the request
    file = request.files.get('file', str(False))
    print(file)

    return "bruh"
    
if __name__ == '__main__':
	app.run(threaded=True, port=29170)
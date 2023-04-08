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
    # with open('D:\\bakalarska-praca\\generalized-log-decoder-bp\\syslog-log-miri.json', 'rb') as f:
    #     res = requests.post(url, files = f)

    # return "bruh"

    # data = request.json
    # res =  requests.post('http://localhost:6000/v1/processmsg', json=data)
    # return data

    # data = request.json
    # res =  requests.post('http://localhost:5000/acceptjson', json=data)
    # return data

    # url = 'http://localhost:29170/v1/upload'
    # with open(f'exported\\linux\\syslog_6-batch_3.json', 'rb') as f:
    #     res = requests.post(url, files = f)
        
    # url = 'http://localhost:29170/v1/upload'
    # with open(f'D:\\bakalarska-praca\\generalized-log-decoder-bp\\syslog-log-miri.json', 'rb') as f:
    #     res = requests.post(url, files = f)

    # define the URL to send the request to
    url = "http://localhost:5000/upload"

    # define the path to the file to upload
    file_path = "D:\\bakalarska-praca\\generalized-log-decoder-bp\\syslog-log-miri.json"
    # file_path = "D:\\bakalarska-praca\\generalized-log-decoder-bp\\exported\\linux\\syslog_6-batch_3.json"

    # open and read the contents of the file
    with open(file_path, "rb") as f:
        file_data = f.read()
        
    print(file_data)

    # define the data payload for the request
    payload = {"file": file_data}

    # send the POST request with the file as an attachment
    response = requests.post(url, files=payload)

    # print the response
    print(response.text)
    
    
    return "bruh"

@app.route('/v1/upload', methods=['GET', 'POST'])

def upload_file():
    # Get the uploaded file from the request
    file = request.files.get('file', str(False))
    print(file)

    return "bruh"
    
if __name__ == '__main__':
	app.run(threaded=True, port=29170)
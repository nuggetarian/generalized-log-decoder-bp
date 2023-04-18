from flask import Flask, request
from modules.logger import Logger
from modules.comparator import Comparator
from modules.anonymization_module import AnonymizeForward
from config import MODE
import requests
import re

app = Flask(__name__)
logger = Logger()
comparator = Comparator()
anonymization = AnonymizeForward()

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
    r = anonymization.anonymize()
    # print(r[1])

    # file_path = f'exported\\linux\\syslog_6-batch_3.json'
    # file_path = f'{r[1]}'

    # with open(file_path, "rb") as f:
    #     file_data = f.read()

    # url = "http://localhost:5000/anonymize/json"
    # payload = {'jsonfile': file_data}

    # response = requests.post(url, files=payload)

    results = []

    for i in range(1, len(r)):
        print(r[i])
        # file_path = f'exported\\linux\\syslog_6-batch_3.json'
        file_path = f'{r[i]}'

        with open(file_path, "rb") as f:
            file_data = f.read()

        url = "http://localhost:5000/anonymize/json"
        payload = {'jsonfile': file_data}

        response = requests.post(url, files=payload)

        results.append(response.text)

        i = i + 1
        # print(response.text)

    # i = 1
    # for result in results:
    #     print(r[i])
    #     i = i + 1
    #     print("=========================================================================================")
    #     print(result)
    # print(results[0])

    # # For cyklus na ukladanie
    # i = 1
    # for result in results:
    #     try:
    #         with open(f'anonymized\\{r[i]}', 'w') as f:
    #             json.dump(result, f)
    #         i = i + 1
    #     except:
    #         print("Saving failed")

    # PROBLEM BOLO ZE NEVZNIKLI FOLDERY TREBA VYMYSLET
    try:
        with open(f'anonymized\\{r[1]}', 'w') as f:
            f.write(results[0])
    except Exception as e:
        print(e)
    

    return results[7]

    # file_path = f'exported\\linux\\syslog_6-batch_3.json'
    # file_path = f'{r[1]}'

    # with open(file_path, "rb") as f:
    #     file_data = f.read()

    # url = "http://localhost:5000/anonymize/json"
    # payload = {'jsonfile': file_data}

    # response = requests.post(url, files=payload)

    # print(response.text)

    # return "bruh"
    return response.text

@app.route('/v1/upload', methods=['GET', 'POST'])

def upload_file():
    # Get the uploaded file from the request
    file = request.files.get('file', str(False))
    print(file)

    return "bruh"
    
if __name__ == '__main__':
	app.run(threaded=True, port=29170)
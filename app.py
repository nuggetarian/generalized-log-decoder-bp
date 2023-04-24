from flask import Flask, request
from modules.logger import Logger
from modules.comparator import Comparator
from modules.anonymization_module import AnonymizeForward
from config import MODE
import requests

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
    results = []

    for i in range(1, len(r)):
        print(r[i])
        file_path = f'{r[i]}'

        with open(file_path, "rb") as f:
            file_data = f.read()

        url = "http://localhost:5000/anonymize/json"
        payload = {'jsonfile': file_data}

        response = requests.post(url, files=payload)

        results.append(response.text)

        i = i + 1

    i = 1
    for result in results:
        try:
            with open(f'anonymized\\{r[i]}', 'w') as f:
                f.write(result)
            i = i + 1
        except Exception as e:
            print(e)

    # PROBLEM BOLO ZE NEVZNIKLI FOLDERY TREBA VYMYSLET
    # try:
    #     with open(f'anonymized\\{r[1]}', 'w') as f:
    #         f.write(results[0])
    # except Exception as e:
    #     print(e)

    return response.text


    
if __name__ == '__main__':
	app.run(threaded=True, port=29170)
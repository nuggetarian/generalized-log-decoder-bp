from flask import Flask, request
from modules.logger import Logger
from modules.comparator import Comparator
from modules.anonymization_module import AnonymizeForward
from time import perf_counter
from modules.neural_network import NeuralNetwork
from config import MODE, BATCH_SIZE
import requests
import json
import queue
import threading
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
logger = Logger()
comparator = Comparator()
anonymization = AnonymizeForward()
ai = NeuralNetwork()
q = queue.Queue()
logArray = []

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():   
    data = request.json # Ziskava json data
    if MODE == 1:
        comparator.compare(data)
    elif MODE == 2: # Logy po jednom
        def prediction():
            ai.predict(log)
        executor = ThreadPoolExecutor(max_workers=2)
        log = json.dumps(data)
        start = perf_counter()
        executor.submit(prediction)
        end = perf_counter()
        time = format(round((end - start)*1000))
        print(time)

    elif MODE == 3: #Queue Batchov
            
        def if_batch_smaller():
            if len(logArray) < BATCH_SIZE:
                logArray.append(data)
                print("Log appended")
                print(len(logArray))
            
        def if_batch_larger():
            if len(logArray) >= BATCH_SIZE:
                arrayToString = ' '.join(map(str, logArray))
                q.put(arrayToString)
                print("Batch added to queue")
                logArray.clear()
                print("Array cleared")

        def if_queue_not_empty():
            if not q.empty():
                start = perf_counter()
                ai.predict(q.get())
                end = perf_counter()
                time = format(round((end - start)*1000))
                print(time)

        executor = ThreadPoolExecutor(max_workers=3)
        
        executor.submit(if_batch_smaller)
        executor.submit(if_batch_larger)
        executor.submit(if_queue_not_empty)
          
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

    return response.text

    
if __name__ == '__main__':
	app.run(threaded=True, port=29170)
from flask import Flask, request
from modules.beautify import Beautify
from modules.logger import Logger
from modules.comparator import Comparator
from modules.anonymization_module import AnonymizeForward
from modules.batch_mode import BatchMode
from time import perf_counter
from modules.neural_network import NeuralNetwork
from config import MODE
from folder_check import FolderCheck
import requests
import json
import queue

app = Flask(__name__)
logger = Logger()
comparator = Comparator()
anonymization = AnonymizeForward()
ai = NeuralNetwork()
q = queue.Queue()
logArray = []
batchMode = BatchMode()
folderCheck = FolderCheck()
beautify = Beautify()


def initialize_app(): # Inicializacna funkcia -- overenie spravnosti priecinkov, ak nejake chybaju, vytvoria sa
    try:
        folderCheck.check() 
        folderCheck.checkAnonymized()
    except Exception as e:
        print(e)

with app.app_context(): # Inicializacna funkcia prebieha len pri spusteni
    initialize_app()


@app.route('/v1/processmsg', methods=['GET','POST']) # Endpoint hlavnych troch modov rozhrania
def processmsg():   
    data = request.json # Ziskava json data
    print(beautify.beautify(data)) # Vypis s odsadenim
    if MODE == 1: # Mod ukladania logov po batchoch
        comparator.compare(data)
    elif MODE == 2: # Mod odosielania logov do neuronovej siete po jednom
        log = json.dumps(data)
        start = perf_counter()
        ai.predict(log) # Predikcna funkcia AI
        end = perf_counter()
        time = format(round((end - start)*1000)) # Vypocet casu na vykonanie jednej predikcie
        print(time)
    elif MODE == 3: # Mod odosielania logov do neuronovej siete po batchoch
        batchMode.process(data)
          
    return data 

@app.route('/v1/forward-anonymize', methods=['GET', 'POST']) # Endpoint odosielania batchov do externej anonymizacnej aplikacie
def fwdAnonymize(): 
       
    r = anonymization.anonymize()
    results = []

    for i in range(1, len(r)): # For loop na ziskavanie ciest suborov
        print(r[i])
        file_path = f'{r[i]}'

        with open(file_path, "rb") as f: # Otvaranie suboru zo ziskanej cesty
            file_data = f.read()

        url = "http://localhost:5000/anonymize/json" # Odosielanie suborov na endpoint anonymizacnej aplikacie
        payload = {'jsonfile': file_data}

        response = requests.post(url, files=payload) # Ziskana odpoved

        results.append(response.text) # Zapis odpovede do pola odpovedi

        i = i + 1

    i = 1
    for result in results: # For loop prechadzajuci pole odpovedi
        try:
            with open(f'anonymized\\{r[i]}', 'w') as f: # Nazov suboru zvoleny na zaklade ziskanej cesty
                f.write(result) # Zapis odpovedi do suboru, z pola odpovedi
            i = i + 1
        except Exception as e:
            print(e)

    return response.text

    
if __name__ == '__main__':
	app.run(threaded=True, port=29170)
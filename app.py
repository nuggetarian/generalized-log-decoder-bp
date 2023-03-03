from flask import Flask, request
from modules.beautify import Beautify
from modules.log_array import LogArray
import json
from modules.logger import Logger
from modules.comparator import Comparator

app = Flask(__name__)
# Vytvaranie instancii objektov
logger = Logger()
# beautifier = Beautify()
#arraylog = LogArray()
comparator = Comparator()

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():   
    data = request.json # Ziskava raw data
    # s = beautifier.beautify(data) # Funkcia na odsadenie JSON
    # resp = json.loads(s) 
    # comparator.compare(resp, s) # Filter na zaklade operacneho systemu
    comparator.compare(data)

    print(data)
    return data
    

if __name__ == '__main__':
	app.run()
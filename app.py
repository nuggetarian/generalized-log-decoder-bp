from flask import Flask, request
import json
from modules.logger import Logger
from modules.comparator import Comparator

app = Flask(__name__)
logger = Logger()
comparator = Comparator()

@app.route('/v1/processmsg', methods=['GET','POST'])
def processmsg():   
    data = request.json # Ziskava json data
    comparator.compare(data)
    print(data)
    return data
    
if __name__ == '__main__':
	app.run()
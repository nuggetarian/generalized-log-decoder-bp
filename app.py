from flask import Flask, request
from modules.logger import Logger
from modules.comparator import Comparator
from config import MODE

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
    
if __name__ == '__main__':
	app.run()
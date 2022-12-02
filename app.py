from flask import Flask, request, jsonify
from flask_restful import Api
from modules.beautify import Beautify

app = Flask(__name__)
api = Api(app)

beautifier = Beautify()

@app.route('/processmsg', methods=['GET','POST'])
def processmsg():
    # Get random raw data
	data = request.data
	beautifier.beautify(data)
	return data

    # Get JSON
    # data = request.get_json()
    # timestamp = data['@timestamp']
    # version = data['@version']
    # agent = data['agent']
    # ecs = data['ecs']
    # event = data['event']
    # host = data['host']
    # log = data['log']
    # message = data['message']
    # tags = data['tags']
    # winlog = data['winlog']

    # return jsonify({'@timestamp' : timestamp, '@version' : version, 'agent' : agent, 'ecs': ecs, 'event': event,
    #                 'host' : host, 'log' : log, 'message' : message, 'tags' : tags, 'winlog' : winlog})

if __name__ == '__main__':
	app.run()
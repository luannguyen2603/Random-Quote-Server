import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
quotes = [
    {'author': 'Vernor Vinge',
     'content': 'An Act of God was defined as something which no reasonable man could have expected.'},
    {'author': 'Ralph Waldo Emerson',
     'content': 'The imagination and the senses cannot be gratified at the same time.'},
    {'author': 'Richard L. Evans',
     'content': 'The tragedy of life is not that it ends so soon, but that we wait so long to begin it.'},
    {'author': 'John Henry Newman',
     'content': 'To live is to change, and to be perfect is to have changed often.'},
    {'author': 'Jack DuVall',
     'content': 'Those for whom peace is no more than a dream are asleep to the future.'},
    {'author': 'William H. Sheldon',
     'content': 'Happiness is essentially a state of going somewhere, wholeheartedly, one-directionally, without regret or reservation.'},
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Random Quote Generator</h1>'''


@app.route('/quotes', methods=['GET'])
def api_all():
    return jsonify(quotes)

@app.route('/quotes/random', methods=['GET'])
def api_random():

    results = []
    randNum = random.randrange(0, len(quotes), 1)
    results.append(quotes[randNum])
    return jsonify(results)

app.run()
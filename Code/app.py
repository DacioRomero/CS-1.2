import sys
import flask
import random
import markov

def create_app():
    app = flask.Flask(__name__)

    with open('./texts/metro.txt') as file:
        my_text = file.read()

    words = markov.get_words(my_text)
    app.markov = markov.MarkovChain(words, order=3)

    @app.route("/")
    def root():
        return flask.render_template('app.html')

    @app.route("/api")
    def api():
        seed = flask.request.args.get('seed') or random.randrange(sys.maxsize)
        seed = int(seed)

        random.seed(seed)

        return flask.jsonify({
            "seed": str(seed),
            "paragraph": app.markov.walk(5)
        })

    return app

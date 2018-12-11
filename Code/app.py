import sys
from flask import Flask, render_template
import markov

def create_app():
    app = Flask(__name__)

    with open('./texts/metro.txt') as file:
        my_text = file.read()

    words = markov.get_words(my_text)
    app.markov = markov.MarkovChain(words, order=2)

    @app.route("/")
    def root():
        return render_template('app.html')

    @app.route("/api")
    def api():
        return app.markov.walk(5)

    return app

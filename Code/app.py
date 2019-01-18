import os
import sys
import flask
import random
import markov
import boto3
import dotenv


def create_app():
    app = flask.Flask(__name__)
    dotenv.load_dotenv()

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = os.getenv('S3_BUCKET')

    if ((AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET) is not (None, None, None)):
        print('Reading from AWS')
        s3 = boto3.resource('s3')
        obj = s3.Object(S3_BUCKET, 'metro.txt')
        my_text = obj.get()['Body'].read().decode('utf-8')
    else:
        with open('./texts/metro.txt') as file:
            my_text = file.read()

    words = markov.get_words(my_text)
    app.markov = markov.MarkovChain(words, order=3)
    app.rng = random.Random()

    @app.route("/")
    def root():
        return flask.render_template('app.html')

    @app.route("/api")
    def api():
        seed = flask.request.args.get('seed') or app.rng.randrange(sys.maxsize)
        seed = int(seed)

        random.seed(seed)

        return flask.jsonify({
            "seed": str(seed),
            "paragraph": app.markov.walk(5)
        })

    return app

from flask import Flask
import time

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    # Flask automatically Jsonify dict for you
    return {'time': time.time()}

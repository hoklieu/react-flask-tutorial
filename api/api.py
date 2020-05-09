from flask import Flask
import time

app = Flask(__name__, static_folder="../build", static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    # Flask automatically Jsonify dict for you
    return {'time': time.time()}

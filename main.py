import pickle
from flask import Flask, request, jsonify
import numpy as np

from flask import Flask

app = Flask(__name__)


@app.route("/predict")
def index():
    vol_moving_avg = request.args.get('vol_moving_avg')
    adj_close_rolling_med = request.args.get('adj_close_rolling_med')
    y_pred = vol_moving_avg + adj_close_rolling_med
    test1=str(y_pred)
    print(y_pred)
    return test1


if __name__ == '__main__':
    app.run()



#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pandas as pd
from sklearn.externals import joblib
import zipfile
from flask import Flask, abort, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_input():
    app.logger.info("{} request received from: {}".format(
        request.method, request.remote_addr))
    if not request.get_json():
       app.logger.error("Request has no data or request is not json, aborting")
       abort(400)
#    zip_ref = zipfile.ZipFile('pipeline.zip', 'r')
#    zip_ref.extractall('model')
#    zip_ref.close()
    model = joblib.load('activity__ma__dtree.pkl')
    data = request.json
    data = pd.DataFrame(data=data, index=[0])
    #prediction = model.predict(data).tolist()
    probs = model.predict_proba(data)
    max_prob = max(max(probs.tolist()))
    max_index = max(probs.tolist()).index(max_prob)
    pred = model.classes_[max_index]
    return jsonify({'prediction': pred, 'probability': max_prob})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import pandas as pd
import flask
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
import io
import imutils
from werkzeug.utils import secure_filename
import keras
from keras.models import load_model
from datetime import datetime, timedelta
import requests
from tensorflow.python.keras.backend import set_session


# initialize flask application and the keras model
app = flask.Flask(__name__)
modelAlameda = None
modelContraCosta = None
modelFresno = None
modelLosAngeles = None
modelOrange = None
modelRiverside = None
modelSacramento = None
modelSanBernardino = None
modelSanDiego = None
modelSantaClara = None
graph = None
sess = None

series = None

def load_trained_models():
    global modelAlamedaCO
    global modelAlamedaPM25
    global modelAlamedaAQI
    global modelContraCostaCO
    global modelContraCostaPM25
    global modelContraCostaAQI
    global modelFresnoCO
    global modelFresnoPM25
    global modelFresnoAQI
    global modelLosAngelesCO
    global modelLosAngelesPM25
    global modelLosAngelesAQI
    global modelOrangeCO
    global modelOrangePM25
    global modelOrangeAQI
    global modelRiversideCO
    global modelRiversidePM25
    global modelRiversideAQI
    global modelSacramentoCO
    global modelSacramentoPM25
    global modelSacramentoAQI
    global modelSanBernardinoCO
    global modelSanBernardinoPM25
    global modelSanBernardinoAQI
    global modelSanDiegoCO
    global modelSanDiegoPM25
    global modelSanDiegoAQI
    global modelSantaClaraCO
    global modelSantaClaraPM25
    global modelSantaClaraAQI
    global graph
    global sess

    sess = tf.compat.v1.Session()
    graph = tf.compat.v1.get_default_graph()
    # load the air pollution models
    modelAlamedaCO = load_model('models/alameda/Alameda-CO.keras')
    modelAlamedaPM25 = load_model('models/alameda/Alameda-PM2.5.keras')
    modelAlamedaAQI = load_model('models/alameda/Alameda-AQI.keras')
    modelContraCostaCO = load_model('models/contra-costa/Contra-Costa-CO.keras')
    modelContraCostaPM25 = load_model('models/contra-costa/Contra-Costa-PM2.5.keras')
    modelContraCostaAQI = load_model('models/contra-costa/Contra-Costa-AQI.keras')
    modelFresnoCO = load_model('models/fresno/Fresno-CO.keras')
    modelFresnoPM25 = load_model('models/fresno/Fresno-PM2.5.keras')
    modelFresnoAQI = load_model('models/fresno/Fresno-AQI.keras')
    modelLosAngelesCO = load_model('models/los-angeles/Los-Angeles-CO.keras')
    modelLosAngelesPM25 = load_model('models/los-angeles/Los-Angeles-PM2.5.keras')
    modelLosAngelesAQI = load_model('models/los-angeles/Los-Angeles-AQI.keras')
    modelOrangeCO = load_model('models/orange/Orange-CO.keras')
    modelOrangePM25 = load_model('models/orange/Orange-PM2.5.keras')
    modelOrangeAQI = load_model('models/orange/Orange-AQI.keras')
    modelRiversideCO = load_model('models/riverside/Riverside-CO.keras')
    modelRiversidePM25 = load_model('models/riverside/Riverside-PM2.5.keras')
    modelRiversideAQI = load_model('models/riverside/Riverside-AQI.keras')
    modelSacramentoCO = load_model('models/sacramento/Sacramento-CO.keras')
    modelSacramentoPM25 = load_model('models/sacramento/Sacramento-PM2.5.keras')
    modelSacramentoAQI = load_model('models/sacramento/Sacramento-AQI.keras')
    modelSanBernardinoCO = load_model('models/san-bernardino/San-Bernardino-CO.keras')
    modelSanBernardinoPM25 = load_model('models/san-bernardino/San-Bernardino-PM2.5.keras')
    modelSanBernardinoAQI = load_model('models/san-bernardino/San-Bernardino-AQI.keras')
    modelSanDiegoCO = load_model('models/san-diego/San-Deigo-CO.keras')
    modelSanDiegoPM25 = load_model('models/san-diego/San-Deigo-PM2.5.keras')
    modelSanDiegoAQI = load_model('models/san-diego/San-Deigo-AQI.keras')
    modelSantaClaraCO = load_model('models/santa-clara/Santa-Clara-CO.keras')
    modelSantaClaraPM25 = load_model('models/santa-clara/Santa-Clara-PM2.5.keras')
    modelSantaClaraAQI = load_model('models/santa-clara/Santa-Clara-AQI.keras')

def getHistory(startDate, endDate, parameters, county):
    options = {}
    options["url"] = "https://www.airnowapi.org/aq/data/"
    options["start_date"] = startDate
    options["end_date"] = endDate
    options["parameters"] = parameters
    options["bbox"] = ""
    options["data_type"] = "C"
    options["format"] = "text/csv"
    options["verbose"] = "0"
    options["monitor_type"] = "0"
    options["include_raw_concentrations"] = "0"
    options["api_key"] = "8F7089D2-5912-49EE-8EEA-918600DADD1C"

    if county == 'alameda':
        options["bbox"] = "-122.373782,37.454186,-121.469214,37.905824"
    elif county == 'contra-costa':
        options["bbox"] = "-122.441584,37.718531,-121.534102,38.099878"
    elif county == 'fresno':
        options["bbox"] = "-120.918731,35.906914,-118.360586,37.585837"
    elif county == 'los-angeles':
        options["bbox"] = "-118.951721,32.75004,-117.646374,34.823302"
    elif county == 'orange':
        options["bbox"] = "-118.147806,33.333992,-117.412987,33.947636"
    elif county == 'riverside':
        options["bbox"] = "-117.676684,33.425888,-114.434949,34.079884"
    elif county == 'sacramento':
        options["bbox"] = "-121.862622,38.018421,-121.027084,38.736405"
    elif county == 'san-bernardino':
        options["bbox"] = "-117.802539,33.87089,-114.131211,35.809236"
    elif county == 'san-diego':
        options["bbox"] = "-117.611081,32.528832,-116.08094,33.505025"
    elif county == 'santa-clara':
        options["bbox"] = "-122.202653,36.892976,-121.208178,37.484637"

    if(parameters == "aqi"):
        options["data_type"] = "A"
        options["parameters"] = "pm25"


    #API request URL
    REQUEST_URL = options["url"] \
                    + "?startDate=" + options["start_date"] \
                    + "T13"  + "&endDate=" + options["end_date"] \
                    + "T14" + "&parameters=" + options["parameters"] \
                    + "&BBOX=" + options["bbox"] \
                    + "&dataType=" + options["data_type"] \
                    + "&format=" + options["format"] \
                    + "&verbose=" + options["verbose"] \
                    + "&monitorType=" + options["monitor_type"] \
                    + "&includerawconcentrations=" + options["include_raw_concentrations"] \
                    + "&API_KEY=" + options["api_key"]
    print(REQUEST_URL)
    
    try:
        # Request AirNowAPI data
        print("Requesting AirNowAPI data...")

        # Perform the AirNow API data request
        s = requests.get(REQUEST_URL).content
        column_name = ['latitude', 'longitude', 'utc', 'parameter', 'value', 'unit']
        series = pd.read_csv(io.StringIO(s.decode('utf-8')), names=column_name, usecols=column_name)

        # Download complete
        print("Download URL: %s" % REQUEST_URL)
        print("downloaded successfully")

        # Data Preprocessing
        series['utc'] = pd.to_datetime(series['utc'])
        df_daily = series.groupby(series['utc'].dt.date).mean()
        df_daily.reset_index(inplace=True)
        df_daily = df_daily.dropna()
        df_daily['value'] = df_daily['value'].astype(float)
        data = df_daily['value']
    
        data = data.values
        history_original = [data[-30:]]
        history = normalize_windows(history_original)
        history = np.array(history)
        history = np.reshape(history, (history.shape[0], history.shape[1],1))
        return history_original, history
    except Exception as e:
        print("Unable to perform AirNowAPI request. %s" %e)
        sys.exit(1)


def normalize_windows(window_data):

    """Normalize data"""
    normalized_data = []
    for window in window_data:
        normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data.append(normalized_window)
    return normalized_data

def predict_next_timestamp(history,county, parameter):
    """Predict the next time stamp given a sequence of history data"""
    if county == 'alameda' and parameter == 'co':
        prediction = modelAlamedaCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'alameda' and parameter == 'pm25':
        prediction = modelAlamedaPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'alameda' and parameter == 'aqi':
        prediction = modelAlamedaAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'contra-costa' and parameter == 'co':
        prediction = modelContraCostaCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'contra-costa' and parameter == 'pm25':
        prediction = modelContraCostaPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'contra-costa' and parameter == 'aqi':
        prediction = modelContraCostaAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'fresno' and parameter == 'co':
        prediction = modelFresnoCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'fresno' and parameter == 'pm25':
        prediction = modelFresnoPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'fresno' and parameter == 'aqi':
        prediction = modelFresnoAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'los-angeles' and parameter == 'co':
        prediction = modelLosAngelesCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'los-angeles' and parameter == 'pm25':
        prediction = modelLosAngelesPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'los-angeles' and parameter == 'aqi':
        prediction = modelLosAngelesAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'orange' and parameter == 'co':
        prediction = modelOrangeCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'orange' and parameter == 'pm25':
        prediction = modelOrangePM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'orange' and parameter == 'aqi':
        prediction = modelOrangeAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'riverside' and parameter == 'co':
        prediction = modelRiversideCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'riverside' and parameter == 'pm25':
        prediction = modelRiversidePM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'riverside' and parameter == 'aqi':
        prediction = modelRiversideAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'sacramento' and parameter == 'co':
        prediction = modelSacramentoCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'sacramento' and parameter == 'pm25':
        prediction = modelSacramentoPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'sacramento' and parameter == 'aqi':
        prediction = modelSacramentoAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'san-bernardino' and parameter == 'co':
        prediction = modelSanBernardinoCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'san-bernardino' and parameter == 'pm25':
        prediction = modelSanBernardinoPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'san-bernardino' and parameter == 'aqi':
        prediction = modelSanBernardinoAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'san-diego' and parameter == 'co':
        prediction = modelSanDiegoCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'san-diego' and parameter == 'pm25':
        prediction = modelSanDiegoPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'san-diego' and parameter == 'aqi':
        prediction = modelSanDiegoAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'santa-clara' and parameter == 'co':
        prediction = modelSantaClaraCO.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'santa-clara' and parameter == 'pm25':
        prediction = modelSantaClaraPM25.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction
    elif county == 'santa-clara' and parameter == 'aqi':
        prediction = modelSantaClaraAQI.predict(history)
        prediction = np.reshape(prediction,(prediction.size,))
        return prediction


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('rtpredictor.html')

# GET method used in web app
# POST can be used to test the endpoint
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        history_original, history = getHistory(file_path)
        with graph.as_default():
            prediction = predict_next_timestamp(history)
            pollution = (prediction[0] + 1) * history_original[0][0]
            data = {}
            data["predicted"] = pollution.tolist()
            data["history"] = np.array(history_original[0]).tolist()
            return flask.jsonify(data)

    if request.method == 'GET':
        county = request.args['county']
        parameter = request.args['parameter']
        endDate = datetime.today()
        startDate = endDate - timedelta(days=35)
        endDate = endDate.strftime("%Y-%m-%d")
        startDate = startDate.strftime("%Y-%m-%d")

        history_original, history = getHistory(startDate, endDate, parameter, county)
        
        #with graph.as_default():
            #set_session(sess)
        prediction = predict_next_timestamp(history,county, parameter)
        pollution = (prediction[0] + 1) * history_original[0][0]
        data = {}
        data["predicted"] = pollution.tolist()
        data["history"] = np.array(history_original[0]).tolist()
        data["parameter"] = parameter
        return flask.jsonify(data)




# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading LSTM models for air prediction and Flask starting server..."
    "please wait until server has fully started"))
    load_trained_models()
    app.run(host='0.0.0.0')
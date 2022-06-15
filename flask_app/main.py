from flask import Flask
from flask import Flask, render_template
from flask import request
import pandas as pd
from xgboost import XGBRegressor
import xgboost as xgb
import pickle


model = pickle.load(open('C:/Users/KDB/Desktop/flask_app/section3_project/model/xgb_model.model', 'rb'))

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
        
def Train():
    if request.method == 'POST':
 
        data1 = float(request.form['SO2'])
        data2 = float(request.form['CO'])
        data3 = float(request.form['NO2'])
        arr = pd.DataFrame({'SO2': [data1], 'CO': [data2], 'NO2' : [data3]})
        output = model.predict(arr)
        #predition

        pred = round(output[0], 2)
    return render_template('result.html', pre=pred)

if __name__ == '__main__': 
    app.run(debug=True)

import json
import pickle as pk
import processed_data

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model
model = pk.load(open('model_BNB.pk','rb'))
tfidf_vector = pk.load(open('Tfidf_Vectorizer.pk','rb'))
label_fit = pk.load(open('label_fit.pk','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json
    print(data)
    processed_text = processed_data.preprocessing(data)
    print(processed_text)
    output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
    
    
    print(output)

    return jsonify(output)
    

@app.route('/predict',methods=['POST'])
def predict():
    data="abc"
    # data=request.form['article']
    #model_name = request.form['ml_model']
    processed_text = processed_data.preprocessing(data)
    output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
    print(data)
    return render_template("index.html",prediction_text="Predicted category with model for article  is:{}".format(data))
    
    
if __name__=="__main__":
    app.run(debug=True)
    #app.run(host = '0.0.0.0', port=8080)
   
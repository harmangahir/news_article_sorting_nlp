import json
import pickle as pk
import processed_data

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model
model = pk.load(open('model_BNB.pkl','rb'))
tfidf_vector = pk.load(open('Tfidf_Vectorizer.pkl','rb'))
label_fit = pk.load(open('Tfidf_Vectorizer.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json
    print(data)
    processed_data = processed_data(data)
    output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_data])))[0]
    
    
    print(output)

    return jsonify(output)

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))



if __name__=="__main__":
    app.run(debug=True)
   
import pickle as pk
import processed_data
from flask import Flask,request,app,jsonify,url_for,render_template
from keras.models import load_model

app=Flask(__name__)

## Load the model

tfidf_vector = pk.load(open('Tfidf_Vectorizer.pk','rb'))
label_fit = pk.load(open('label_fit.pk','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])

# def predict_api():
#     data=request.json
#     print(data)
#     processed_text = processed_data.preprocessing(data)
#     print(processed_text)
#     output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
    
    
#     print(output)

#     return jsonify(output)
    

@app.route('/predict',methods=['POST'])
def predict():
    data= request.form['article']
    model_name = request.form['ml_model']
    if(model_name == 'BNB'):
        model = pk.load(open('model_BNB.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(model_name,output))
    elif(model_name == 'CNB'):
        model = pk.load(open('model_CNB.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(model_name,output))
    elif(model_name == 'GNB'):
        model = pk.load(open('model_GNB.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(model_name,output))
    elif(model_name == 'GRU'):
        model = pk.load(open('model_GRU.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(model_name,output))
    elif(model_name == 'SGD'):
        model = pk.load(open('model_SGD.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(model_name,output))
    elif(model_name == 'RFC'):
        model = pk.load(open('model_RFC.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        
        p_tfidf = tfidf_vector.transform(processed_text)
        result1 = model.predict(p_tfidf)[0]

        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform(processed_text)))[0]

        
        
        score = model.predict_proba(tfidf_vector.transform(processed_text))[result1]


        return render_template("index.html", models_name=model_name, probability_score=score,predicted_category=output)

        # return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(output), probability_score=score)

    elif(model_name == 'MNB'):
        model = pk.load(open('model_MNB.pk','rb'))
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text="Predicted category with model {} for article  is:{}".format(model_name,output))
    elif(model_name == 'LSTM'):
        model = load_model('model_LSTM.h5')
        processed_text = processed_data.preprocessing(data)
        output = label_fit.inverse_transform(model.predict(tfidf_vector.transform([processed_text])))[0]
        return render_template("index.html", models_name=model_name, prediction_text=output)
    
if __name__=="__main__":
    app.run(debug=True)
    #app.run(host = '0.0.0.0', port=8080)
   
import pickle as pk
import processed_data
from flask import Flask,request,app,jsonify,url_for,render_template
from keras.models import load_model
import tensorflow
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

app=Flask(__name__)

## Load the model

tfidf_vector = pk.load(open(r'TF-IDF\Tfidf_Vectorizer.pk','rb'))
label_fit = pk.load(open(r'Labels\label_fit.pk','rb'))
tokenizer = pk.load(open(r'Tokenizer\tokenizer.pk','rb'))
label_encoder_pk = pk.load(open(r'Labels\label_encoder.pk','rb'))




@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict_api',methods=['POST'])
    
        
    

@app.route('/predict',methods=['POST'])


def predict():
    data= request.form['article']

    model_name  = request.form['ml_model']

    processed_text = processed_data.preprocessing(data)
    if(model_name == 'MNB'):
        model = pk.load(open('models/model_MNB.pk','rb'))
        p_tfidf = tfidf_vector.transform(processed_text)
        result1 = model.predict(p_tfidf)[0]
        score = model.predict_proba(tfidf_vector.transform(processed_text))[result1]
        business_percentage=round(score[0]*100,2)
        tech_percentage=round(score[1]*100,2)
        politics_percentage=round(score[2]*100,2)
        sport_percentage=round(score[3]*100,2)
        entertainment_percentage=round(score[4]*100,2)
        model_prediction = label_fit.inverse_transform(model.predict(tfidf_vector.transform(processed_text)))[0]
        
        return render_template("index.html", model_name = 'Multinomial NB',sport_prob = sport_percentage,business_prob = business_percentage,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = model_prediction)
    elif(model_name == 'BNB'):
        model = pk.load(open('models/model_BNB.pk','rb'))
        p_tfidf = tfidf_vector.transform(processed_text)
        result1 = model.predict(p_tfidf)[0]
        score = model.predict_proba(tfidf_vector.transform(processed_text))[result1]
        business_percentage=round(score[0]*100,2)
        tech_percentage=round(score[1]*100,2)
        politics_percentage=round(score[2]*100,2)
        sport_percentage=round(score[3]*100,2)
        entertainment_percentage=round(score[4]*100,2)
        model_prediction = label_fit.inverse_transform(model.predict(tfidf_vector.transform(processed_text)))[0]
        
        return render_template("index.html", model_name = 'Bernoulli NB',sport_prob = sport_percentage,business_prob = business_percentage,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = model_prediction)
        
    elif(model_name == 'CNB'):
        model = pk.load(open('models/model_CNB.pk','rb'))
        p_tfidf = tfidf_vector.transform(processed_text)
        result1 = model.predict(p_tfidf)[0]
        score = model.predict_proba(tfidf_vector.transform(processed_text))[result1]
        business_percentage=round(score[0]*100,2)
        tech_percentage=round(score[1]*100,2)
        politics_percentage=round(score[2]*100,2)
        sport_percentage=round(score[3]*100,2)
        entertainment_percentage=round(score[4]*100,2)
        model_prediction = label_fit.inverse_transform(model.predict(tfidf_vector.transform(processed_text)))[0]
        
        return render_template("index.html", model_name = 'Complement NB',sport_prob = sport_percentage,business_prob = business_percentage,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = model_prediction)
    
    elif(model_name == 'RFC'):
        model = pk.load(open('models/model_RFC.pk','rb'))
        p_tfidf = tfidf_vector.transform(processed_text)
        result1 = model.predict(p_tfidf)[0]
        score = model.predict_proba(tfidf_vector.transform(processed_text))[result1]
        business_percentage=round(score[0]*100,2)
        tech_percentage=round(score[1]*100,2)
        politics_percentage=round(score[2]*100,2)
        sport_percentage=round(score[3]*100,2)
        entertainment_percentage=round(score[4]*100,2)
        model_prediction = label_fit.inverse_transform(model.predict(tfidf_vector.transform(processed_text)))[0]

        return render_template("index.html", model_name = 'Random Forest',sport_prob = sport_percentage,business_prob = business_percentage,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = model_prediction)

    elif(model_name == 'LSTM'):
        load_model_LSTM =tensorflow.keras.models.load_model('models/model_LSTM.h5')
        input_sequences = tokenizer.texts_to_sequences(processed_text)
        input_pad = pad_sequences(input_sequences, maxlen=500)
        predicted_result = load_model_LSTM.predict(input_pad)
        preds = tensorflow.argmax(predicted_result, axis=1)
        business_percentage=round(predicted_result[0][0]*100,2)
        tech_percentage=round(predicted_result[0][4]*100,2)
        politics_percentage=round(predicted_result[0][2]*100,2)
        sport_percentage=round(predicted_result[0][3]*100,2)
        entertainment_percentage=round(predicted_result[0][1]*100,2)
        output = label_encoder_pk.inverse_transform(preds)[0]
        
        return render_template("index.html", model_name = 'LSTM',sport_prob = sport_percentage,business_prob =business_percentage ,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = output)
    
    elif(model_name == 'BiLSTM'):
        load_model_Bi_LSTM =tensorflow.keras.models.load_model('models/model_Bi_LSTM.h5')
        input_sequences = tokenizer.texts_to_sequences(processed_text)
        input_pad = pad_sequences(input_sequences, maxlen=500)
        predicted_result = load_model_Bi_LSTM.predict(input_pad)
        preds = tensorflow.argmax(predicted_result, axis=1)
        business_percentage=round(predicted_result[0][0]*100,2)
        tech_percentage=round(predicted_result[0][4]*100,2)
        politics_percentage=round(predicted_result[0][2]*100,2)
        sport_percentage=round(predicted_result[0][3]*100,2)
        entertainment_percentage=round(predicted_result[0][1]*100,2)
        output = label_encoder_pk.inverse_transform(preds)[0]
        
        return render_template("index.html", model_name = 'Bi Directional LSTM',sport_prob = sport_percentage,business_prob =business_percentage ,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = output)
    
    elif(model_name == 'GRU'):
        load_model_GRU =tensorflow.keras.models.load_model('models/model_GRU.h5')
        input_sequences = tokenizer.texts_to_sequences(processed_text)
        input_pad = pad_sequences(input_sequences, maxlen=500)
        predicted_result = load_model_GRU.predict(input_pad)
        preds = tensorflow.argmax(predicted_result, axis=1)
        business_percentage=round(predicted_result[0][0]*100,2)
        tech_percentage=round(predicted_result[0][4]*100,2)
        politics_percentage=round(predicted_result[0][2]*100,2)
        sport_percentage=round(predicted_result[0][3]*100,2)
        entertainment_percentage=round(predicted_result[0][1]*100,2)
        output = label_encoder_pk.inverse_transform(preds)[0]
        
        return render_template("index.html", model_name = 'GRU',sport_prob = sport_percentage,business_prob =business_percentage ,politics_prob = politics_percentage,entertainment_prob = entertainment_percentage, tech_prob=tech_percentage,predicted_category = output)



@app.route('/predict_all',methods=['POST'])
def predict_all():
    data= request.form['article']

    BNB_model = pk.load(open('models/model_BNB.pk','rb'))
    MNB_model = pk.load(open('models/model_MNB.pk','rb'))
    CNB_model = pk.load(open('models/model_CNB.pk','rb'))
    RFC_model = pk.load(open('models/model_RFC.pk','rb'))
    load_model_LSTM =tensorflow.keras.models.load_model('models/model_LSTM.h5')
    load_model_Bi_LSTM =tensorflow.keras.models.load_model('models/model_Bi_LSTM.h5')
    load_model_GRU =tensorflow.keras.models.load_model('models/model_GRU.h5')
    processed_text = processed_data.preprocessing(data)
    p_tfidf = tfidf_vector.transform(processed_text)
    input_sequences = tokenizer.texts_to_sequences(processed_text)
    input_pad = pad_sequences(input_sequences, maxlen=500)
    
    
    BNB_result = BNB_model.predict(p_tfidf)[0]
    BNB_output = label_fit.inverse_transform(BNB_model.predict(tfidf_vector.transform(processed_text)))[0]
    BNB_score = BNB_model.predict_proba(tfidf_vector.transform(processed_text))[BNB_result]
    BNB_business_percentage=round(BNB_score[0]*100,2)
    BNB_tech_percentage=round(BNB_score[1]*100,2)
    BNB_politics_percentage=round(BNB_score[2]*100,2)
    BNB_sport_percentage=round(BNB_score[3]*100,2)
    BNB_entertainment_percentage=round(BNB_score[4]*100,2)

    MNB_result = BNB_model.predict(p_tfidf)[0]
    MNB_output = label_fit.inverse_transform(MNB_model.predict(tfidf_vector.transform(processed_text)))[0]
    MNB_score = MNB_model.predict_proba(tfidf_vector.transform(processed_text))[MNB_result]
    MNB_business_percentage=round(MNB_score[0]*100,2)
    MNB_tech_percentage=round(MNB_score[1]*100,2)
    MNB_politics_percentage=round(MNB_score[2]*100,2)
    MNB_sport_percentage=round(MNB_score[3]*100,2)
    MNB_entertainment_percentage=round(MNB_score[4]*100,2)

    CNB_result = CNB_model.predict(p_tfidf)[0]
    CNB_output = label_fit.inverse_transform(CNB_model.predict(tfidf_vector.transform(processed_text)))[0]
    CNB_score = MNB_model.predict_proba(tfidf_vector.transform(processed_text))[CNB_result]
    CNB_business_percentage=round(CNB_score[0]*100,2)
    CNB_tech_percentage=round(CNB_score[1]*100,2)
    CNB_politics_percentage=round(CNB_score[2]*100,2)
    CNB_sport_percentage=round(CNB_score[3]*100,2)
    CNB_entertainment_percentage=round(CNB_score[4]*100,2)

    RFC_result = RFC_model.predict(p_tfidf)[0]
    RFC_output = label_fit.inverse_transform(RFC_model.predict(tfidf_vector.transform(processed_text)))[0]
    RFC_score = MNB_model.predict_proba(tfidf_vector.transform(processed_text))[RFC_result]
    RFC_business_percentage=round(RFC_score[0]*100,2)
    RFC_tech_percentage=round(RFC_score[1]*100,2)
    RFC_politics_percentage=round(RFC_score[2]*100,2)
    RFC_sport_percentage=round(RFC_score[3]*100,2)
    RFC_entertainment_percentage=round(RFC_score[4]*100,2)
    
    
    
    predicted_result = load_model_LSTM.predict(input_pad)
    preds = tensorflow.argmax(predicted_result, axis=1)
    LSTM_business_percentage=round(predicted_result[0][0]*100,2)
    LSTM_tech_percentage=round(predicted_result[0][4]*100,2)
    LSTM_politics_percentage=round(predicted_result[0][2]*100,2)
    LSTM_sport_percentage=round(predicted_result[0][3]*100,2)
    LSTM_entertainment_percentage=round(predicted_result[0][1]*100,2)
    LSTM_output = label_encoder_pk.inverse_transform(preds)[0]

    
    predicted_result = load_model_Bi_LSTM.predict(input_pad)
    preds = tensorflow.argmax(predicted_result, axis=1)
    Bi_LSTM_business_percentage=round(predicted_result[0][0]*100,2)
    Bi_LSTM_tech_percentage=round(predicted_result[0][4]*100,2)
    Bi_LSTM_politics_percentage=round(predicted_result[0][2]*100,2)
    Bi_LSTM_sport_percentage=round(predicted_result[0][3]*100,2)
    Bi_LSTM_entertainment_percentage=round(predicted_result[0][1]*100,2)
    Bi_LSTM_output = label_encoder_pk.inverse_transform(preds)[0]

    
    predicted_result = load_model_GRU.predict(input_pad)
    preds = tensorflow.argmax(predicted_result, axis=1)
    GRU_business_percentage=round(predicted_result[0][0]*100,2)
    GRU_tech_percentage=round(predicted_result[0][4]*100,2)
    GRU_politics_percentage=round(predicted_result[0][2]*100,2)
    GRU_sport_percentage=round(predicted_result[0][3]*100,2)
    GRU_entertainment_percentage=round(predicted_result[0][1]*100,2)
    GRU_output = label_encoder_pk.inverse_transform(preds)[0]
    
    
    
    
    return render_template("index.html",MNB_model_name='Multinomial NB',MNB_business_prob=MNB_business_percentage, MNB_tech_prob=MNB_tech_percentage,MNB_politics_prob=MNB_politics_percentage,MNB_sport_prob=MNB_sport_percentage,MNB_entertainment_prob=MNB_entertainment_percentage ,MNB_predicted_category=MNB_output,BNB_model_name='Bernoulli NB',BNB_business_prob=BNB_business_percentage, BNB_tech_prob=BNB_tech_percentage,BNB_politics_prob=BNB_politics_percentage,BNB_sport_prob=BNB_sport_percentage,BNB_entertainment_prob=BNB_entertainment_percentage ,BNB_predicted_category=BNB_output,CNB_model_name='Complement NB',CNB_business_prob=CNB_business_percentage, CNB_tech_prob=CNB_tech_percentage,CNB_politics_prob=CNB_politics_percentage,CNB_sport_prob=CNB_sport_percentage,CNB_entertainment_prob=CNB_entertainment_percentage ,CNB_predicted_category=CNB_output,RFC_model_name='Random Forest',RFC_business_prob=RFC_business_percentage, RFC_tech_prob=RFC_tech_percentage,RFC_politics_prob=RFC_politics_percentage,RFC_sport_prob=RFC_sport_percentage,RFC_entertainment_prob=RFC_entertainment_percentage ,RFC_predicted_category=RFC_output,LSTM_model_name='LSTM',LSTM_business_prob=LSTM_business_percentage, LSTM_tech_prob=LSTM_tech_percentage,LSTM_politics_prob=LSTM_politics_percentage,LSTM_sport_prob=LSTM_sport_percentage,LSTM_entertainment_prob=LSTM_entertainment_percentage ,LSTM_predicted_category=LSTM_output,Bi_LSTM_model_name='Bi_LSTM',Bi_LSTM_business_prob=Bi_LSTM_business_percentage, Bi_LSTM_tech_prob=Bi_LSTM_tech_percentage,Bi_LSTM_politics_prob=Bi_LSTM_politics_percentage,Bi_LSTM_sport_prob=Bi_LSTM_sport_percentage,Bi_LSTM_entertainment_prob=Bi_LSTM_entertainment_percentage ,Bi_LSTM_predicted_category=Bi_LSTM_output,GRU_model_name='GRU',GRU_business_prob=GRU_business_percentage, GRU_tech_prob=GRU_tech_percentage,GRU_politics_prob=GRU_politics_percentage,GRU_sport_prob=GRU_sport_percentage,GRU_entertainment_prob=GRU_entertainment_percentage ,GRU_predicted_category=GRU_output)





if __name__=="__main__":
    app.run(debug=True)
    #app.run(host = '0.0.0.0', port=8080)
   
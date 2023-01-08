import pickle as pk
import processed_data
from flask import Flask,request,app,jsonify,url_for,render_template
from keras.models import load_model

app=Flask(__name__)

## Load the model

tfidf_vector = pk.load(open('TF-IDF/Tfidf_Vectorizer.pk','rb'))
label_fit = pk.load(open('Labels/label_fit.pk','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
    
        
    

@app.route('/predict',methods=['POST'])


def predict():
    data= request.form['article']
    model_name = request.form['ml_model']
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
        
        return render_template("index.html", model_name = 'Multinomial NB',MNB_sport_prob = sport_percentage,MNB_business_prob = business_percentage,MNB_politics_prob = politics_percentage,MNB_entertainment_prob = entertainment_percentage, MNB_tech_prob=tech_percentage,predicted_category = model_prediction)
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
        
        return render_template("index.html", model_name = 'Bernoulli NB',BNB_sport_prob = sport_percentage,BNB_business_prob = business_percentage,BNB_politics_prob = politics_percentage,BNB_entertainment_prob = entertainment_percentage, BNB_tech_prob=tech_percentage,predicted_category = model_prediction)
        
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
        
        return render_template("index.html", model_name = 'Complement NB',CNB_sport_prob = sport_percentage,CNB_business_prob = business_percentage,CNB_politics_prob = politics_percentage,CNB_entertainment_prob = entertainment_percentage, CNB_tech_prob=tech_percentage,predicted_category = model_prediction)
    
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
        
        return render_template("index.html", model_name = 'Random Forest',RFC_sport_prob = sport_percentage,RFC_business_prob = business_percentage,RFC_politics_prob = politics_percentage,RFC_entertainment_prob = entertainment_percentage, RFC_tech_prob=tech_percentage,predicted_category = model_prediction)
          



# @app.route('/predict_all',methods=['POST'])
# def predict_all():
#     data= request.form['article']
#     BNB_model = pk.load(open('model_BNB.pk','rb'))
#     MNB_model = pk.load(open('model_MNB.pk','rb'))
#     processed_text = processed_data.preprocessing(data)
#     p_tfidf = tfidf_vector.transform(processed_text)
    
    
#     BNB_result = BNB_model.predict(p_tfidf)[0]
#     BNB_output = label_fit.inverse_transform(BNB_model.predict(tfidf_vector.transform(processed_text)))[0]
#     BNB_score = BNB_model.predict_proba(tfidf_vector.transform(processed_text))[BNB_result]
#     BNB_business_percentage=round(BNB_score[0]*100,2)
#     BNB_tech_percentage=round(BNB_score[1]*100,2)
#     BNB_politics_percentage=round(BNB_score[2]*100,2)
#     BNB_sport_percentage=round(BNB_score[3]*100,2)
#     BNB_entertainment_percentage=round(BNB_score[4]*100,2)

#     MNB_result = BNB_model.predict(p_tfidf)[0]
#     MNB_output = label_fit.inverse_transform(MNB_model.predict(tfidf_vector.transform(processed_text)))[0]
#     MNB_score = MNB_model.predict_proba(tfidf_vector.transform(processed_text))[MNB_result]
#     MNB_business_percentage=round(MNB_score[0]*100,2)
#     MNB_tech_percentage=round(MNB_score[1]*100,2)
#     MNB_politics_percentage=round(MNB_score[2]*100,2)
#     MNB_sport_percentage=round(MNB_score[3]*100,2)
#     MNB_entertainment_percentage=round(MNB_score[4]*100,2)
    
    
    
    
    
    
    
#     return render_template("index.html", BNB_model_name=BNB_model,BNB_business=BNB_business_percentage, BNB_tech=BNB_tech_percentage,BNB_politics=BNB_politics_percentage,BNB_sport=BNB_sport_percentage,BNB_entertainment=BNB_entertainment_percentage ,BNB_predicted_category=BNB_output,MNB_model_name=MNB_model,MNB_business=MNB_business_percentage, MNB_tech=MNB_tech_percentage,MNB_politics=MNB_politics_percentage,MNB_sport=MNB_sport_percentage,MNB_entertainment=MNB_entertainment_percentage ,MNB_predicted_category=MNB_output)





if __name__=="__main__":
    app.run(debug=True)
    #app.run(host = '0.0.0.0', port=8080)
   
from flask import Flask,render_template,request
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def predict():
   exp= [x for x in request.form.values()]
   region = exp[0]
   no_of_training = exp[6]
   age = exp[1]
   pre_year_rating = exp[4]
   length_of_service = exp[5]
   awards_won = exp[8]
   avg_training_score = exp[7]
   if exp[3] == "em":
       ed_bachelors = 0
       ed_below_secondary = 0
       ed_masters = 1
   elif exp[3] == "eb":
       ed_bachelors = 1
       ed_below_secondary = 0
       ed_masters = 0
   elif exp[3] == "ebs":
       ed_bachelors = 0
       ed_below_secondary = 1
       ed_masters = 0
   if exp[2] == "gf":  
      gen_female = 1
      gen_male = 0
   elif exp[2] == "gm":   
      gen_female = 0
      gen_male = 1
   if exp[9] == "rcr":
       rec_other = 0
       rec_refered = 1
   elif exp[9] == "rco":
       rec_other = 1
       rec_refered = 0
   elif exp[9] == "rcs":
       rec_other = 0
       rec_refered = 0
   exp1 = [region,no_of_training,age,pre_year_rating,length_of_service,awards_won,avg_training_score,ed_bachelors,ed_below_secondary,ed_masters,gen_female,gen_male,rec_other,rec_refered]
   final_features = [np.array(exp1)]
   prediction = model.predict(final_features)
   output =prediction[0]
   print(exp1)
   if ((float(ed_below_secondary) != 1 and float(avg_training_score) > 75 and float(pre_year_rating) >=3)):
       return render_template ('promoted.html',prediction_text="Yay !!! You are eligible for promotion")
   else:
       return render_template ('not_promoted.html',prediction_text="Oops !!! You are not eligible for promotion")
if __name__=='__main__':
    app.run(port=3000)
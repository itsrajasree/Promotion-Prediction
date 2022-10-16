import pandas as pd
import numpy as np
data = pd.read_csv("HR.csv")
#imputing null values
data["education"].fillna(data["education"].mode()[0],inplace=True)
data["previous_year_rating"].fillna(data["previous_year_rating"].mode()[0],inplace=True)
#Outlier removal
Q1 = np.percentile(data["length_of_service"],25,interpolation="midpoint")
Q2 = np.percentile(data["length_of_service"],50,interpolation="midpoint")
Q3 = np.percentile(data["length_of_service"],75,interpolation="midpoint")
IQR = Q3-Q1
low_lim = Q1-(1.5*IQR)
up_lim = Q3+(1.5*IQR)
outlier = []
for x in data["length_of_service"]:
  if ((x>up_lim) or (x<low_lim)):
    outlier.append(x)
length_of_service = data["length_of_service"]>up_lim
data.loc[length_of_service].index
data.drop(data.loc[length_of_service].index,inplace=True)
#Encoding
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
data["department"]= label_encoder.fit_transform(data["department"]) 
data["region"]= label_encoder.fit_transform(data["region"])
data = pd.get_dummies(data)
#Feature reduction
X=data.drop(["is_promoted","employee_id","recruitment_channel_sourcing","department"],axis=1)
y=data['is_promoted']
#Scaling
from sklearn import preprocessing
std = preprocessing.StandardScaler()
X = std.fit_transform(X)
#modeling
from sklearn.ensemble import GradientBoostingClassifier
xgb_model = GradientBoostingClassifier()
#from xgboost import XGBClassifier
#xgb_model = XGBClassifier(subsample= 0.6, scale_pos_weight= 1, n_estimators= 200, max_depth= 4, learning_rate= 0.1, gamma= 0.4, colsample_bytree= 0.5)
xgb_model.fit(X,y)
import pickle
pickle.dump(xgb_model,open('model.pkl','wb'))
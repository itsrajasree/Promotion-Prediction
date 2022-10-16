# Promotion-Prediction

Based on various parameters, using Gradient Boost Classifier, it is predicted whether an employee is eligible for promotion or not. 

Details can be inputted in the webpage and the result can be obtained.

1. Outlier Removal :
Using percentile() function, otliers are detected and are removed from the dataset.

2. Encoding :
Label encoder is used to encode the data.

3. Feature Reduction :
Least relevent columns are removed from the dataset.

4. Scaling :
With Standard scaling, the data is scaled.

5. Modelling :
Gradient Boost Classifier is used to model the data. 

6. Website :
Using Python Flask, the model is connected to the designed web pages and output is obtained.

import numpy as np 
from flask import Flask, request, jsonify, render_template
import pickle

def predictor(AppInc, CoappInc, LoanAmt, LoanAmtTerm, CreditHist, Gender, Married, Dependents, Graduated, SelfEmp, PropertyLocationSU, PropertyLocationU):
    array = []
    #Applicant Income 
    array.append(int(AppInc))
    #Coapplicant Income
    array.append(float(CoappInc))
    #Loan Amount
    array.append(float(LoanAmt))
    #Term of Loan Amount
    array.append(LoanAmtTerm)
    #Credit History
    if CreditHist == 'Y':
        array.append(1.0)
    else:
        array.append(0.0)
    #Gender 
    if Gender == 'M':
        array.append(1.0)
    else:
        array.append(0.0)
    #Marriage Status
    if Married == 'Y':
        array.append(1)
    else:
        array.append(0)
    #Dependents
    if int(Dependents) == 1:
        array.extend([1, 0, 0])
    elif int(Dependents) == 2:
        array.extend([0, 1, 0])
    elif str(Dependents) == '3+':
        array.extend([0, 0, 1])
    #Education
    if Graduated == 'Y':
        array.append(1)
    else:
        array.append(0)
    #Self Employed
    if SelfEmp == 'Y':
        array.append(1)
    else:
        array.append(0)
    #Property Location Semi-Urban
    if PropertyLocationSU == 'Y':
        array.append(1)
    else:
        array.append(0)
    #Property Location Urban
    if PropertyLocationU == 'Y':
        array.append(1)
    else:
        array.append(0)
    return array


#create flask app 
app = Flask(__name__)
#load pickle model
model = pickle.load(open('LRModel.pkl', 'rb'))

#index template
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    features = [x for x in request.form.values()]
    list = predictor(*features)
    prediction = model.predict([list])
    if (prediction == 0):
        prediction = 'Not Approved'
    if (prediction == 1):
        prediction = 'Approved'
    return render_template('index.html', prediction_text = 'Your Loan was {}!'.format(prediction))
    

if __name__ == '__main__':
    app.run(debug= True)



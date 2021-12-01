import pandas as pd 
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split
import pickle

#load csv file 
df = pd.read_csv('./Data/Loan_Approval.csv')

df_cleaned = df.dropna()
df_encoded = pd.get_dummies(df_cleaned, drop_first= True)

X = df_encoded.drop(columns='Loan_Status_Y')
y = df_encoded['Loan_Status_Y']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

lr = LogisticRegression(solver= 'liblinear', multi_class= 'auto').fit(X_train, y_train)

pickle.dump(lr, open('LRModel.pkl', 'wb'))


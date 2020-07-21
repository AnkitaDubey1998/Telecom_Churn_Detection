from flask import *
import pickle
import misc_functions as mf

# filename = 'GB_Churn_model.pkl'
# classifier = pickle.load(open(filename, 'rb'))

import pandas as pd
train = pd.read_csv(r'datasets/final_data.csv', na_values=[' ','??'])
train.drop(train.columns[[0]], axis=1, inplace=True)

X_train=train.drop(columns=['Churn'])
Y_train=train[['Churn']]

from sklearn.ensemble import GradientBoostingClassifier
classifier = GradientBoostingClassifier(n_estimators=30, learning_rate=0.01, max_depth=7)
classifier.fit(X_train, Y_train)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if(request.method=='POST'):
        tenure = int(request.form['tenure'])
        monthly_charges = int(request.form['monthly_charges'])
        tech_support = request.form['tech_support']
        online_security = request.form['online_security']
        contract = request.form['contract']
        payment_method = request.form['payment_method']
        data = mf.get_processed_data(monthly_charges, tenure, online_security, tech_support, contract, payment_method)
        prediction = classifier.predict(data)[0]
        return render_template("result.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
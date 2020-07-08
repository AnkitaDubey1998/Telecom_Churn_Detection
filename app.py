from flask import *
import pickle

filename = 'GB_Churn_model.pkl'
classifier = pickle.load(open(filename, 'rb'))

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
        print(tenure)
        print(tech_support)
        print(online_security)
        print(contract)
        print(payment_method)
        print(monthly_charges)
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
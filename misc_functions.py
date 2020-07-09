import numpy as np

def get_processed_data(monthly_charges, tenure, online_security, tech_support, contract, payment_method):
    # MonthlyCharges
    mn=18.25
    mx=118.6
    monthly_charges = (monthly_charges-mn)/(mx-mn)

    # OnlineSecurity
    if(online_security=='No'):
        online_security = 0
    elif(online_security=='No internet service'):
        online_security = 1
    else:
        online_security = 2
    
    # TechSupport
    if(tech_support=='No'):
        tech_support = 0
    elif(tech_support=='No internet service'):
        tech_support = 1
    else:
        tech_support = 2

    # Contract
    if(contract=='Month-to-month'):
        contract = 0
    elif(contract=='One year'):
        contract = 1
    else:
        contract = 2

    # PaymentMethod
    if(payment_method=='Bank transfer (automatic)'):
        payment_method = 0
    elif(payment_method=='Credit card (automatic)'):
        payment_method = 1
    elif(payment_method=='Electronic check'):
        payment_method = 2
    else:
        payment_method = 3

    result = [monthly_charges, tenure, online_security, tech_support, contract, payment_method]
    
    return np.array([result])
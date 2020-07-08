import pandas as pd

pd.options.mode.chained_assignment = None

train = pd.read_csv(r'datasets/train_cleaned.csv', na_values=[' ','??'])
train.drop(train.columns[[0]], axis=1, inplace=True)

test = pd.read_csv(r'datasets/test_cleaned.csv', na_values=[' ','??'])
test.drop(test.columns[[0]], axis=1, inplace=True)

X_train=train.drop(columns=['Churn'])
Y_train=train['Churn']
X_test=test.drop(columns=['Churn'])
Y_test=test[['Churn']]

selected_feat=['MonthlyCharges', 'tenure', 'OnlineSecurity', 'TechSupport', 'Contract', 'PaymentMethod']
X_train=X_train[selected_feat]
X_test=X_test[selected_feat]

from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(n_estimators=30, learning_rate=0.01, max_depth=7, random_state=42)
gb.fit(X_train, Y_train)

import pickle
filename = 'GB_Churn_model.pkl'
pickle.dump(gb, open(filename, 'wb'))
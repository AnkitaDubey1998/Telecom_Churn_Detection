import pandas as pd

pd.options.mode.chained_assignment = None
df = pd.read_csv(r'datasets/original/telco_customer_churn.csv', na_values=[' ','??'])
df.drop(columns='customerID', inplace=True)

X=df.drop(columns=['Churn'])
Y=df.loc[:,['Churn']]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

df_train=X_train.copy()
df_train['Churn']=Y_train['Churn']
df_train.to_csv(r'datasets/uncleaned/train_uncleaned.csv')

df_test=X_test.copy()
df_test['Churn']=Y_test['Churn']
df_test.to_csv(r'datasets/uncleaned/test_uncleaned.csv')

median = X_train['TotalCharges'].median()
X_train['TotalCharges'].fillna(median, inplace=True)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in X_train.select_dtypes(include=[object]).columns:
    X_train[i] = encoder.fit_transform(X_train[i])
Y_train['Churn']=encoder.fit_transform(Y_train['Churn'])

from imblearn.over_sampling import SMOTE
sampler=SMOTE(sampling_strategy=0.8, random_state=1)
X_train,Y_train=sampler.fit_resample(X_train,Y_train)

from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler = MinMaxScaler()
X_train[['MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(X_train[['MonthlyCharges', 'TotalCharges']])
X_train[['MonthlyCharges', 'TotalCharges']].head()

df_train=X_train.copy()
df_train['Churn']=Y_train['Churn']
df_train.to_csv(r'datasets/train_cleaned.csv')
import pandas as pd

pd.options.mode.chained_assignment = None

df = pd.read_csv(r'datasets/uncleaned/test_uncleaned.csv', na_values=[' ','??'])
df.drop(df.columns[[0]], axis=1, inplace=True)

X=df.drop(columns=['Churn'])
Y=df.loc[:,['Churn']]

median = X['TotalCharges'].median()
X['TotalCharges'].fillna(median, inplace=True)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in X.select_dtypes(include=[object]).columns:
    X[i] = encoder.fit_transform(X[i])
Y['Churn']=encoder.fit_transform(Y['Churn'])

mn=18.25
mx=118.6
X['MonthlyCharges']=(X['MonthlyCharges']-mn)/(mx-mn)
mn=18.8
mx=8684.8
X['TotalCharges']=(X['TotalCharges']-mn)/(mx-mn)

df_test=X.copy()
df_test['Churn']=Y['Churn']
df_test.to_csv(r'datasets/test_cleaned.csv')
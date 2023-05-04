import statsmodels.api as sm
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('diamonds_with_log_price_2.csv')

data.head()

y = data.price
y_log = data.log_price
X = data.drop('price',axis=1)
X = X.drop('log_price',axis=1)

X_log_train, X_log_test, y_log_train, y_log_test = train_test_split(X, y_log, train_size=0.7)

X_log_train = sm.add_constant(X_log_train)

model_log = sm.OLS(y_log_train, X_log_train).fit()
print(model_log.summary())
print("Standard Error: " + str(model_log.scale**.5))
model_log.save("diamonds_model_log.pickle")
X_log_test = sm.add_constant(X_log_test)

X_log_test.to_csv('x_log_test.csv',index=False)
y_log_test.to_csv('y_log_true.csv',index=False)
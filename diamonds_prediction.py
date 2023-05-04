import statsmodels.api as sm
import pandas as pd
import os.path

to_test = pd.read_csv('x_log_test.csv')
to_test.head()

if os.path.isfile('y_log_true.csv'):
    true_price = pd.read_csv('y_log_true.csv')
    true_price.head()
    true_price.rename(columns = {'log_price':'true_price'}, inplace = True)

model = sm.load("diamonds_model_log.pickle")
print(model.summary())
print("Standard Error: " + str(model.scale**.5))

prediction = model.predict(to_test)
prediction_df = pd.DataFrame(data=prediction)
prediction_df.rename(columns = {'0':'prediction'}, inplace = True)

if os.path.isfile('y_log_true.csv'):
    results = pd.concat([to_test, prediction_df, true_price], axis=1, join='inner')
else:
    results = pd.concat([to_test, prediction_df], axis=1, join='inner')
    
results.to_csv('diamonds_prediction.csv',index=False)
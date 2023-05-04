#Python 3 OLS (Ordinary Least Square) Regression Instruction

---
###1. Installing Necessary Packages
---
Assuming the Python 3 has been installed, the following commands will install packages necessary to run the python program:
`pip3 install -U statsmodels`
`pip3 install -U pandas`

---
###2. Using the Program
---
There are two important files, `diamonds_regression.py` and `diamonds_prediction.py`.
To create the model, run the `python3 diamonds_regression.py` command. This will generate the regression model that will be shown in the terminal and these three files:
-  `x_log_test.csv` contains the variables selected for test that will be used to predict the price
-  `y_log_true.csv` contains the real price for the corresponding selected test variables
-  `diamonds_model_log.pickle` is the regression model that can be used for the prediction
  
After we have successfully run the program, we can run the `python3 diamonds_prediction.py` command to obtain `diamonds_prediction.csv` file that contains the test variables, predicted price, and the true prices. We can then manually import the csv file to excel to calculate the overfitting test.

---
###3. Using Regression Samples
---
There are two folders named `Best Result` and `Overfitting Example`. To see the result of each case, copy `x_log_test.csv`, `y_log_true.csv`, and `diamonds_model_log.pickle` to the same folder where the `diamonds_prediction.py` is located. Then run `python3 diamonds_prediction.py` to obtain `diamonds_prediction.csv` file.
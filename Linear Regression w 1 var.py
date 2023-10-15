Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #linear Regression with one variable
>>> import numpy as np
... import matplotlib.pyplot as plt
... plt.style.use('./deeplearning.mplstyle')
SyntaxError: multiple statements found while compiling a single statement
>>> # x_train is the input variable (size in 1000 square feet)
... # y_train is the target (price in 1000s of dollars)
... x_train = np.array([1.0, 2.0])
... y_train = np.array([300.0, 500.0])
... print(f"x_train = {x_train}")

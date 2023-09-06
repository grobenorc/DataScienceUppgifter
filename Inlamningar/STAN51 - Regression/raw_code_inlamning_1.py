# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:48:56 2023
@author: claes
"""
import statsmodels.api as sm
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.getcwd()
os.chdir('C:/Users/claes/OneDrive/Universitet/DataScience Magisterprogram/STAN51 - Maskininlärning ur ett regressionperspektiv/Inlamningar/Inlamning_1')
os.getcwd()

Guns = pd.read_stata('Guns.dta')

def log_transform(input_variable):
    return np.log(input_variable)

Guns['log_violent_crime'] = Guns['vio'].apply(log_transform)
Guns['log_pop'] = Guns['pop'].apply(log_transform)
Guns['log_murder'] = Guns['mur'].apply(log_transform)
Guns['log_robbery'] = Guns['rob'].apply(log_transform)


y_1a = np.array(Guns['log_violent_crime'])

X_1a = Guns[['log_pop', 'avginc', 'shall', 'log_murder', 'log_robbery']]
X_1a = sm.add_constant(X_1a)
# 2.
lm_spec_1a = sm.OLS(y_1a, X_1a)

# 3.
lm_fit_1a  = lm_spec_1a.fit()

lm_fit_1a.summary()
print(lm_fit_1a.summary())

lm_coef_1b = lm_fit_1a.params
print(lm_coef_1b)


# 1C
## Predict 
lm_fit_1a.predict()


# 1D
## Residuals vs fitted

lm_res_1d = lm_fit_1a.resid

lm_objnames = dir(lm_fit_1a)

diff_res = sum(lm_res_1d**2)
print(diff_res)


# 1E
plotdata_1e = pd.DataFrame({'predicted': lm_fit_1a.predict(), 'residuals': lm_fit_1a.resid})

from matplotlib.pyplot import subplots
fig_1e, ax_1e = subplots(figsize = (8,8))
ax_1e.scatter(x='predicted', y='residuals', marker='x', data=plotdata_1e)
ax_1e.set_xlabel("Predicted output value")
ax_1e.set_ylabel("Residuals")
plt.title('Residuals vs. predicted')


# rem_patterns1e



# 1F

# 1.
plotdata_1f = pd.DataFrame({'predicted': lm_fit_1a.predict(), 'residuals': lm_fit_1a.resid, 'stateid':Guns['stateid'].astype(float)})

# 2.
fig_1f, ax_1f = subplots(figsize = (8,8))
ax_1f.scatter(x = 'residuals', y ='stateid', c = "residuals", marker = 'x', data = plotdata_1f)
plt.title('Residuals vs. StateId')
ax_1f.set_xlabel('Residuals')
ax_1f.set_ylabel('StateId')

# 3.
whatIsee1f = "??"




# 1G
summary_1g     = Guns.describe(include = 'all')
print(summary_1g)

typeofvarb_1g  = "int"
in_regmodel_1g = "??"



# 1H

Guns['stateid'] = Guns['stateid'].astype(str)
summary_1h      = Guns.describe()
print(summary_1h)
whatchanged1h = "??"




# 1I

# 1.
X_1i = X_1a.assign(StateIdcat = Guns['stateid'])
X_1i['StateIdcat'] = pd.to_numeric(X_1i['StateIdcat'])

# 2.
lm_spec_1i = sm.OLS(y_1a, X_1i)
lm_fit_1i  = lm_spec_1i.fit()

# howincluded_1i = "??"



# 1J

## 1.
X_1j = pd.get_dummies(X_1i, columns=['StateIdcat'], drop_first=True)
X_1j = sm.add_constant(X_1j)

## 2.
lm_spec_1j = sm.OLS(y_1a, X_1j)
lm_fit_1j  = lm_spec_1j.fit()

print(lm_fit_1j.summary())

howoutputdiffers_1j = "??"

###############################################################################
# DEL 2 #
###############################################################################












def log_transform(input_variable):
    return np.log(input_variable)

Guns['log_violent_crime'] = Guns['vio'].apply(log_transform)
Guns['log_pop'] = Guns['pop'].apply(log_transform)
Guns['log_murder'] = Guns['mur'].apply(log_transform)
Guns['log_robbery'] = Guns['rob'].apply(log_transform)


y_1a = np.array(Guns['log_violent_crime'])

X_1a = Guns[['log_pop', 'avginc', 'shall', 'log_murder', 'log_robbery']]
X_1a = sm.add_constant(X_1a)

def get_betas(y, X):
    """
    Calculate the least squares estimate 𝛽̂ for simple linear regression.

    Parameters:
    X (numpy.ndarray): Two-dimensional array of feature values (independent variable).
    y (numpy.ndarray): One-dimensional array of target values (dependent variable).

    Returns:
    beta_hat (numpy.ndarray): Array of estimated slope coefficients.
    
    Estimering av koefficienter görs av: (X'X)^-1*X'Y
    """
    # Transpose av X
    X_trans = np.array(X).T
    
    # Beräkning X^TX
    XTX = np.matmul(X_trans, np.array(X))
    
    # Beräkning av inversen X^TX
    XTX_inv = np.linalg.inv(XTX)
    
    # Beräkna X^TY
    XTY = np.matmul(X_trans, y)
    
    # Estimate the coefficients
    coefficients = np.matmul(XTX_inv, XTY)

    return coefficients
    

def calculate_residuals(y,X):
    """
    Parameters
    ----------
    y : np.array()
        Observerade värden.
    X : np.array()
        Input-variabler av observerad data.
    coefficients : np.array()
        Estimering av koefficienter.

    Returns
    -------
    Residuals

    """
    predicted = np.dot(X, get_betas(y, X))
    observed = y
    res = observed - predicted
    return res



def calculate_r2(y,X):
    """
    Parameters
    ----------
    y : np.array()
        Observerade värden.
    X : np.array()
        Input-variabler av observerad data.

    Returns
    -------
    R^2 statistic.

    """
    residuals = calculate_residuals(y, X)
    residuals_squared = residuals**2
    y_observed = y
    y_mean = y.mean()
    y_mean_squared = (y_observed - y_mean)**2
    
    summa = 1 - ( sum(residuals_squared)/ sum((y_mean_squared)) )
    
    return summa



# 1.
y_2d = y_1a.reshape(-1, 1)
X_2d = X_1a.values
X_2e = X_1j.values

# 2.
R2_nostate_2e = calculate_r2(y_1a, X_2d)
R2_withstate_2e = calculate_r2(y_1a, X_2e)
print((R2_withstate_2e, R2_nostate_2e))

# 3.
effect_of_stateid2e = "??"


    
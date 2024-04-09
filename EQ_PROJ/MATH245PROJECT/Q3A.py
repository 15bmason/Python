import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore') # Removes the exp overflow warning
# Prob. of an aftershock func.
def p_aftershock(x, beta0, beta1): 
    z = beta0 + beta1 * x
    exp_neg_z = np.exp(-z)
    return 1 / (1 + exp_neg_z)

# Negative log-likelihood func.
def n_log_lik(X, Y, beta0, beta1):
    p = p_aftershock(X, beta0, beta1)
    return -(Y.dot(np.log(p)) - (1-Y).dot(np.log(1-p)))

# Returns the gradient of b0,b1
def gradient(X, Y, beta0, beta1): 
    p = p_aftershock(X, beta0, beta1)
    grad_beta0, grad_beta1 = np.sum(p - Y), np.sum((p - Y) * X)
    return grad_beta0, grad_beta1

#Returns values for b0,b1 after we reach stopping cond.
def fit(X, Y, gamma):
    beta0, beta1 = 0, 0 # Inital values b0 and b1 = 0
    for i in range(int(1/gamma)): # Stopping cond. 1/gamma
        grad_beta0, grad_beta1 = gradient(X, Y, beta0, beta1)
        beta0 -= gamma * grad_beta0
        beta1 -= gamma * grad_beta1
        nll = n_log_lik(X, Y, beta0, beta1)
        print(f"grad beta0: {grad_beta0}", f"grad beta1: {grad_beta1}")
    return beta0, beta1

# Calc. Euclidean distance between the stresses
def euclidDist(df, cols = ["s1", "s2", "s3", "s4", "s5", "s6"]):
    return np.linalg.norm(df[cols].values, axis=1)

# Assignment of variables
spe_d = pd.read_csv("aftershocks/2001BHUJIN01YAGI_grid.csv") # Specific data
dataAftershocks = spe_d["aftershock"].to_numpy() # Aftershocks column as vector
X = euclidDist(spe_d) # Euclidean norm of the stresses
Y = dataAftershocks  # Aftershock column

gamma = 0.001  # Step size for gradient descent
beta0, beta1 = fit(X, Y, gamma)
print(beta0, beta1)
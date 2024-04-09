import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def sigmoid(x, beta0, beta1):
    z = beta0 + beta1 * x
    return 1 / (1 + np.exp(-z))

def negative_log_likelihood(X, Y, beta0, beta1):
    nll = 0
    for x, y in zip(X, Y):
        p_x = sigmoid(x, beta0, beta1)
        nll += -y * np.log(p_x) - (1 - y) * np.log(1 - p_x)
    return nll

def gradient_descent(X, Y, gamma, max_iter=60000, tol=1e-10):
    beta0 = 0
    beta1 = 0
    n = len(X)
    prev_loss = np.inf
    for _ in range(max_iter):
        pred = sigmoid(X, beta0, beta1)
        gradient_beta0 = np.sum(pred - Y)
        gradient_beta1 = np.sum((pred - Y) * X)
        beta0 -= gamma * gradient_beta0 / n
        beta1 -= gamma * gradient_beta1 / n
        loss = negative_log_likelihood(X, Y, beta0, beta1)
        print(beta0, beta1)
        if abs(loss - prev_loss) < tol:
            break
        prev_loss = loss
    return beta0, beta1

def fit(X, Y, gamma):
    return gradient_descent(X, Y, gamma)


def euclidDist(df, cols = ["s1", "s2", "s3", "s4", "s5", "s6"]):
    return np.linalg.norm(df[cols].values, axis=1)

# Assignment of variables
spe_d = pd.read_csv("aftershocks/2001BHUJIN01YAGI_grid.csv") # Specific data
dataAftershocks = spe_d["aftershock"].to_numpy() # Aftershocks column as vector
X = euclidDist(spe_d) # Euclidean norm of the stresses
Y = dataAftershocks  # Aftershock column

gamma = 0.001  # Step size for gradient descent
beta0, beta1 = fit(X, Y, gamma)
print("Beta0:", beta0)
print("Beta1:", beta1)

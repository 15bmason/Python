import numpy as np
import pandas as pd
from scipy.optimize import minimize
import warnings
warnings.simplefilter("ignore")

def moment_distance(fi):
    specific_event = pd.read_csv(fi)
    all_events = pd.read_csv("all_events.csv")

    related_row = all_events[all_events['id'] == fi[12:-9]]
    log_moment = np.log(related_row.iloc[0]["moment"])
    dists_from_mainshock = np.sqrt(specific_event['x']**2 + specific_event['y']**2).to_numpy()
    
    df = pd.DataFrame({"moment": log_moment,
                    "distance": dists_from_mainshock,
                    "aftershock": specific_event["aftershock"].values})
    return df

def n_log_likelihood(beta, X1, X2, Y):
    beta0, beta1, beta2 = beta
    z = beta0 + beta1 * X1 + beta2 * X2
    p = 1 / (1 + np.exp(-z))
    return -(Y.dot(np.log(p)) + (1 - Y).dot(np.log(1 - p)))

def fit2(X1, X2, Y):
    beta_initial = np.zeros(3)
    result = minimize(n_log_likelihood, beta_initial, args=(X1, X2, Y))
    beta_optimal = result.x
    return beta_optimal

df = moment_distance("aftershocks/2001BHUJIN01YAGI_grid.csv")
X1 = df["moment"].values
X2 = df["distance"].values
Y = df["aftershock"].values

beta_values = fit2(X1, X2, Y)
print("Optimal beta values:", beta_values)
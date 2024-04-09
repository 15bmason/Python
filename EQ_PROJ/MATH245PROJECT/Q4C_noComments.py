import pandas as pd
import numpy as np
from scipy.optimize import minimize
from plotnine import ggplot, aes, geom_point, labs
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

def n_log_likelihood(params, X1, X2, Y):
    beta0, beta1, beta2 = params
    z = beta0 + beta1 * X1 + beta2 * X2
    p = 1 / (1 + np.exp(-z))
    return -np.sum(Y * np.log(p) + (1 - Y) * np.log(1 - p))

def fit2_file(fi):
    specific_data = moment_distance("aftershocks/" + fi)
    X1 = specific_data["moment"].values 
    X2 = specific_data["distance"].values 
    Y = specific_data["aftershock"].values
    beta_initial = np.zeros(3)
    result = minimize(n_log_likelihood, beta_initial, args=(X1, X2, Y))
    return result.x

selected_events = pd.read_csv("selectedEvents.csv")
beta_values = []
for file_path in selected_events["file"]:
    beta_values.append(fit2_file(file_path))

beta_df = pd.DataFrame(beta_values, columns=["beta0", "beta1", "beta2"])
p1 = (
    ggplot(beta_df, aes(x="beta0", y="beta1")) +
    geom_point() +
    labs(x="β0", y="β1", title="β1 vs β0")
)
print(p1)
p2 = (
    ggplot(beta_df, aes(x="beta0", y="beta2")) +
    geom_point() +
    labs(x="β0", y="β2", title="β2 vs β0")
)
print(p2)
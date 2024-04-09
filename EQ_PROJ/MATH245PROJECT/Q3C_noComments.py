import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_point, labs
import warnings
warnings.filterwarnings("ignore")

def p_aftershock(x, beta0, beta1): 
    z = beta0 + beta1 * x
    exp_neg_z = np.exp(-z)
    return 1 / (1 + exp_neg_z)
        
def n_log_lik(X, Y, beta0, beta1):
    p = p_aftershock(X, beta0, beta1)
    return -(Y.dot(np.log(p)) - (1-Y).dot(np.log(1-p)))
        
def gradient(X, Y, beta0, beta1): 
    p = p_aftershock(X, beta0, beta1)
    grad_beta0, grad_beta1 = np.sum(p - Y), np.sum((p - Y) * X)
    return grad_beta0, grad_beta1
        
def euclidDist(df, cols = ["s1", "s2", "s3", "s4", "s5", "s6"]):
    return np.linalg.norm(df[cols].values, axis=1)

def fit(X, Y, gamma):
    beta0, beta1 = 0, 0 # Inital values b0 and b1 = 0
    for _ in range(int(1/gamma)): # Stopping cond. 1/gamma
        grad_beta0, grad_beta1 = gradient(X, Y, beta0, beta1)
        beta0 -= gamma * grad_beta0
        beta1 -= gamma * grad_beta1
    return beta0, beta1

def fit_file(fi, fu, gamma):
        specific_data = pd.read_csv("aftershocks/" + fi) # Specific data
        data_aftershocks = specific_data["aftershock"].to_numpy() # Aftershocks column as vector
        X = specific_data.apply(lambda row: fu(row['s1'],
                row['s2'], row['s3'], row['s4'],
                row['s5'], row['s6']), axis=1).to_numpy()
        Y = data_aftershocks
        return fit(X, Y, gamma)

def fit_file_factory(fu, gamma):
    return lambda fi: fit_file(fi, fu, gamma)

def fu(s1, s2, s3, s4, s5, s6):
    return np.log(np.sum(np.abs([s1, s2, s3, s4, s5, s6])))

def plot_results(beta_df):
    p = (
        ggplot(beta_df, aes(x="beta0", y="beta1")) 
        + geom_point()
        + labs(x="β0", y="β1", title="β0 vs β1 for selected events")
    )
    p.show()

selected_events = pd.read_csv("selectedEvents.csv")
gamma = 10e-3
fit_file_fixed = fit_file_factory(fu, gamma)
beta_values = []
for file_path in selected_events["file"]:
    beta0, beta1 = fit_file_fixed(file_path)
    beta_values.append((beta0, beta1))

beta_df = pd.DataFrame(beta_values, columns=["beta0", "beta1"])
plot_results(beta_df)
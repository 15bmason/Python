import numpy as np
import pandas as pd

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
moment_distance("aftershocks/2001BHUJIN01YAGI_grid.csv")
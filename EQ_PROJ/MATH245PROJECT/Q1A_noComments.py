import pandas as pd
import numpy as np

# DataFrame transcripts of resp. files
all_events = pd.read_csv("all_events.csv", index_col="id")
selected_events = pd.read_csv("selectedEvents.csv", index_col="id")
"""
data = []
for event_id in selected_events.index:
    specific_event = all_events.loc[event_id] # Links the events from selected_events to all_events
    aftershock_data = pd.read_csv("aftershocks/" + event_id + "_grid.csv") # Reads the specific events' aftershock data

    # Dictionary of rows to go into the DataFrame
    data_temp = {
        "date": specific_event["date"],
        "file": selected_events.loc[selected_events.index == event_id, "file"].values[0],
        "lat": specific_event["lat"],
        "lon": specific_event["lon"],
        "mw": specific_event["mw"],
        "aftershocks": np.sum(aftershock_data["aftershock"])
    }
    data.append(data_temp)

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y") # Converts the date into a datetime type
df_sorted = df.sort_values("date") # Sorted by date
df_sorted.head()
"""

def extract_info(row_id):
    specific_event = all_events.loc[row_id] # Locates a selected event in all_events
    aftershock_data = pd.read_csv("aftershocks/" + specific_event.name + "_grid.csv")
    aftershocks_count = aftershock_data["aftershock"].sum() # Sums the aftershock column
    return {
        "date": specific_event["date"],
        "file": selected_events.loc[row_id, "file"],
        "lat": specific_event["lat"],
        "lon": specific_event["lon"],
        "mw": specific_event["mw"],
        "aftershocks": aftershocks_count
    }

# Applies extract_info to each row
data = list(map(extract_info, selected_events.index))

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y") # Converts the date into a datetime type
# Sort the DataFrame by date
sorted_df = df.sort_values("date")

sorted_df.head()
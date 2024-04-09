import pandas as pd

selected_events = pd.read_csv("selectedEvents.csv", index_col="id") # Sets id as the index column
all_events = pd.read_csv("all_events.csv", index_col="id") 

def extract_info(row_id):
    specific_event = all_events.loc[row_id] # Locates a selected event in all_events
    return {
        "file": selected_events.loc[row_id, "file"],
        "lat": specific_event["lat"],
        "lon": specific_event["lon"],
        "moment": specific_event["moment"],
    }

# Applies extract_info to each row
data = list(map(extract_info, selected_events.index))

df = pd.DataFrame(data)
sorted_df = df.sort_values("file") # Sorts by file
sorted_df.head()
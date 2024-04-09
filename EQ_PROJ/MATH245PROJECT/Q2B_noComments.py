import geopandas as gpd
import pandas as pd
import numpy as np
from plotnine import ggplot, geom_map, aes, geom_point, theme, labs

selected_events = pd.read_csv("selectedEvents.csv", index_col="id")
all_events = pd.read_csv("all_events.csv", index_col="id")
countries = gpd.read_file("worldMap.shp")

def extract_info(row_id):
    specific_event = all_events.loc[row_id] # Locates a selected event in all_events
    aftershock_data = pd.read_csv("aftershocks/" + specific_event.name + "_grid.csv")
    aftershocks_count = aftershock_data["aftershock"].sum() # Sums the aftershock column
    return {
        "lat": specific_event["lat"],
        "lon": specific_event["lon"],
        "mw": specific_event["mw"],
        "aftershocks": aftershocks_count
    }

# Applies extract_info to each row
data = list(map(extract_info, selected_events.index))

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)
# Sorted by aftershock quantity - descending so we have no big points plotted over small points
sorted_df = df.sort_values(by="aftershocks", ascending=False)

p = (
ggplot()
    + geom_map(data=countries, fill="lightgray", color="white")
    # Plots the points from sorted_df where size and fill colour correlate to number of aftershocks and the intensity - Given a black border to make more distinct
    + geom_point(data=sorted_df, mapping=aes(x="lon", y="lat", size="aftershocks",fill="mw"), color="black", stroke=0.25, alpha=0.7)
    + labs(x="Longitude", y="Latitude", title="Map of selected events")
    + theme(legend_position="right", figure_size=(6, 4))
)
p.show()
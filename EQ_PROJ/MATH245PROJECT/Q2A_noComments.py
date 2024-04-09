import geopandas as gpd
import pandas as pd
from plotnine import ggplot, geom_map, aes, geom_point

all_events = pd.read_csv("all_events.csv") # Turns all events into a DataFrame
countries = gpd.read_file("worldMap.shp") # Turns world map into a geo DataFrame

p = (
ggplot(countries) +
  geom_map(fill="lightgray", colour = "white")
  + geom_point(all_events, aes(x = "lon", y = "lat"), colour = "blue", size=1)
)
p.show()
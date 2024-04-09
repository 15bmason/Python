import pandas as pd
from plotnine import ggplot, geom_point, aes, scale_color_gradient
import numpy as np

def euclidDist(df, cols = ["s1", "s2", "s3", "s4", "s5", "s6"]):
    return np.linalg.norm(df[cols].values, axis=1)

spe_e = pd.read_csv("aftershocks/2001BHUJIN01YAGI_grid.csv")
spe_e['norm'] = euclidDist(spe_e)

p = (
    ggplot(spe_e)
    + geom_point(aes(x='x', y='y', color='norm'))
    + geom_point(aes(x='x', y='y'), data=spe_e[spe_e['aftershock'] > 0], color='black', size=2)
    + scale_color_gradient(low="blue", high="red")
)

p.show()

import pandas as pd
import numpy as np

def process_stress(fi, fu):
    df_file = pd.read_csv(fi)
    df_file['fu'] = df_file.apply(lambda row: fu(row['s1'],
                     row['s2'], row['s3'], row['s4'],
                       row['s5'], row['s6']), axis=1)
    return df_file[['x', 'y', 'fu', 'aftershock']].head()

def fu(s1, s2, s3, s4, s5, s6):
    return np.sum(np.abs([s1, s2, s3, s4, s5, s6]))

result = process_stress("aftershocks/2001BHUJIN01YAGI_grid.csv", fu)
print(result)
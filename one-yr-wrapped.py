# turning spotify data into a visualization project

import pandas as pd
from pandas import DataFrame

chars = pd.read_csv('characters.csv')
frame = DataFrame(chars)

print(frame)
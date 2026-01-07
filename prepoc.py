import pandas as pd
import numpy as np

data = pd.read_csv("housing_data.csv")



cols = ['Basement', 'Exterior', 'Heating', 'Flooring', 'Roof']

data[cols] = data[cols].fillna("NA")

data = data.drop(columns=['Latitude','Longitude'])



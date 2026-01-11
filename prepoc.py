import pandas as pd
import numpy as np

data = pd.read_csv("housing_data.csv")



cols = ['Basement', 'Exterior', 'Heating', 'Flooring', 'Roof']

data[cols] = data[cols].fillna("NA")

data = data.drop(columns=['Latitude','Longitude'])


def get_luxury_score(data):

    data['LUXURY_SCORE']=(
        (data['Pool'] == 'Yes').astype(int) * 2 +
        (data['Waterfront'] == 'Yes').astype(int) * 2 +
        (data['Fireplace'] == 'Yes').astype(int) * 1 +
        (data['Garden'] == 'Yes').astype(int) * 1 +
        (data['Balcony'] == 'Yes').astype(int) * 1
    )
    return data



def commodies_score(data):
    data['C_score']=(
        (np.where(data['Garage']=="No", 0, 1))+
        (np.where(data['Parking']=="No", 0, 1))+
        (np.where(data['Basement']=="No Basement", 0, 1))+
        (np.where(data['Exterior']=="NA", 0, 1))+
        (np.where(data['Flooring']=="NA", 0, 1))+
        (np.where(data['Sewer']=="none", 0, 1))

    )
    return data
data = get_luxury_score(data)
data = commodies_score(data)
print("Garage values:", data['Garage'].unique())
print("Parking values:", data['Parking'].unique())
print("Basement values:", data['Basement'].unique())
print("Exterior values:", data['Exterior'].unique())
print("Flooring values:", data['Flooring'].unique())
print("Sewer values:", data['Sewer'].unique())


print(data.head())
import pandas as pd
from prepoc import data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

X = data
y= data['Price']

num_cols=[

]

cat_cols=[
    
]
X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=42, shuffle=True)
import pandas as pd
from prepoc import data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

X = data.drop(columns=['Price','City','Province'])
y= data['Price']

num_cols=[
    'Bedrooms',
    "Bathrooms",
    "Acreage",
    'Square Footage'

]

cat_cols=[
    'Property Type',
    'Garage',
    'Parking',
    'Basement',
    'Exterior',
    'Fireplace',
    'Heating',
    'Flooring',
    'Roof',
    'Waterfront',
    'Sewer',
    'Pool',
    'Garden',
    'Balcony'
]

PRE_PROCESS = ColumnTransformer(
    transformers=[
        ("Scaler", StandardScaler(), num_cols),
        ("Encodeer", OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ]
)


X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2, random_state=42, shuffle=True)


lm = Pipeline(steps=[
    ("preporc", PRE_PROCESS),
    ("RFR", RandomForestRegressor(
        n_estimators=50,
        max_depth=15,
        min_samples_leaf=10,
        max_features="sqrt",
        n_jobs=-1,
        random_state=42
    ))
])

lm.fit(X_train, y_train)

preds = lm.predict(X_test)
print(preds)

print("MAE:", mean_absolute_error(y_test, preds))
print("R²:", r2_score(y_test, preds))
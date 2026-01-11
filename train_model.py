import numpy as np
import pandas as pd
from prepoc import*
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor

from sklearn.preprocessing import TargetEncoder
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score

X = data.drop(columns=['Price'])
y= data['Price']

num_cols=[
    'Bedrooms',
    "Bathrooms",
    "Acreage",
    'Square Footage',
    'LUXURY_SCORE',
    'C_score'

]

cat_cols=[
    'City',
    'Province',
    'Property Type',
    'Heating',
    'Roof'

]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

y_train_log = np.log1p(y_train)
y_test_log = np.log1p(y_test)

preproc = ColumnTransformer(
    transformers=[
         ("num", "passthrough", num_cols),
        ("Encoder", TargetEncoder(), cat_cols)
    ]
)

hgb = HistGradientBoostingRegressor(
    max_iter=100,
    max_depth=10,
    learning_rate=0.02,
    min_samples_leaf=10,
    l2_regularization=0.04,
   
    random_state=69
)

my_model = Pipeline(steps=[
    ("preproc", preproc),
    ("model", hgb)

])

my_model.fit(X_train, y_train_log)



pred = my_model.predict(X_test)
print(pred)


print(mean_absolute_error(y_test_log,pred))
print(r2_score(y_test_log, pred))


test_data = pd.read_csv("test_house.csv")

test_data = get_luxury_score(test_data)
test_data = commodies_score(test_data)

X_test = test_data[X.columns]

pred_log = my_model.predict(X_test)
pred_price = np.expm1(pred_log)

print(pred_price)

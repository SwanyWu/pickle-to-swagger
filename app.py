# 1. Library imports
from pyexpat import model
import uvicorn
from fastapi import FastAPI
from InputSchema import Schema
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_breast_cancer(data:Schema):
    data = data.dict()
    # print(model.predict([[variance,skewness,curtosis,entropy]]))
    prediction = model.predict([[
        data["radius_mean"],
        data["perimeter_mean"],
        data["area_mean"],
        data["compactness_mean" ],
        data["concavity_mean"],
        data["concave_points_mean"],
        data["radius_se"],
        data["perimeter_se"],
        data["area_se"],
        data["radius_worst"],
        data["perimeter_worst"], 
        data["area_worst"], 
        data["compactness_worst"], 
        data["concavity_worst"],
        data["concave_points_worst"],
    ]])
    if(prediction[0]>0.5):
        prediction="high risk"
    else:
        prediction="low risk"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
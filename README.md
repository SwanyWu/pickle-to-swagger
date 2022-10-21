# 🎓 pickle-to-swagger

(base) This project aims at exposing a machine learning model vis FastAPI
 
 ## step by step implementation
 
 1. create an empty repo in gitlab and clone to local machine
 
 2. train the model and wrap it up in a pickle file \\
 [model we used|https://www.kaggle.com/code/nobodymartin/lightgbm-explanation-practice-with-dataset/notebook]
 
 3. write main(app.py) function and data schema
 
 4. save and run `uvicorn app:app --reload` and go to port *http://127.0.0.1:8000*
 
 5. go to *http://127.0.0.1:8000/docs* is the swagger page.
 

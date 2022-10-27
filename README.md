# 🎓 pickle-to-swagger

(base) This project aims at exposing a machine learning model vis FastAPI
 
 ## step by step implementation
 
 1. create an empty repo in gitlab and clone to local machine
 
 2. train the model and wrap it up in a pickle file 
 [model we used](https://www.kaggle.com/code/nobodymartin/lightgbm-explanation-practice-with-dataset/notebook)
 
 3. write main(app.py) function and data schema
 
 4. save and run `uvicorn app:app --reload` and go to port *http://127.0.0.1:8000*
 
 5. go to *http://127.0.0.1:8000/docs* is the swagger page.

 ## containerization

the benefit of containerizing app into a docker image is that 1) independent environment and 2) resource (ram/CPU) efficient.
we don't need to run the app 24/7 to make it accessible, just trigger the container every time we want to access the app.

 6. run `pip install pipreqs` and `pipreqs .` to generate requirements.txt.

 7. create Dockerfile

 8. run `docker build -t dockapp:v1 .` to build your own image based on base python:3.9. can check current images in docker UI or `docker images`

 9. run `docker run -d --name mlcontainer -p 80:80 dockapp:v1` to build container, you might want to change `8000` if it's already in use. and then run `docker container ls` to check available containers.

 now go to docker hub and launch app in browser.

 ### notes
- ?swagger UI = streamlit UI
2 ways for users to provide input but streamlit is more customized


 

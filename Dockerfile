# base imagex
FROM python:3.9

# create our own image
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt
# lightgbm uses cmake, install outset requirements.txt
RUN pip3 install cmake
RUN pip3 install lightgbm

# CMD ["python", "app.py"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
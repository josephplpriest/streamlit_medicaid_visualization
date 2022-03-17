FROM python:3.8-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python", "./cleaning.py" ]
#CMD [ "streamlit", "run", "./app.py"]


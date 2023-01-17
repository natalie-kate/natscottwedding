FROM python:3.9.2

WORKDIR /wedding

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "./app.py", "runserver" , "0.0.0.0:8000"]

EXPOSE 8000
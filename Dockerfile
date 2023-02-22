FROM python:3.9.2

WORKDIR /wedding

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

RUN chmod +x /wedding/check_activity.sh

LABEL com.centurylinklabs.watchtower.lifecycle.pre-update="/check_activity.sh"

CMD [ "python3", "./app.py", "runserver" , "0.0.0.0:8000"]

EXPOSE 8000
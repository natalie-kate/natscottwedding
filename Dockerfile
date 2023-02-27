FROM python:3.9.2

WORKDIR /wedding

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

RUN apt-get update

RUN apt-get install nano

RUN chmod +x /wedding/check_activity.sh

RUN chmod +x /wedding/post_update.sh

LABEL com.centurylinklabs.watchtower.lifecycle.pre-update="/wedding/check_activity.sh"

LABEL com.centurylinklabs.watchtower.lifecycle.post-update="/wedding/post_update.sh"

CMD [ "python3", "./app.py", "runserver" , "0.0.0.0:8000"]

EXPOSE 8000
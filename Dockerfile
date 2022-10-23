FROM python:3.10


ENV APP /app


WORKDIR ${APP}


COPY . .


RUN pip install -r requirements.txt


#ENTRYPOINT ["assistant"]
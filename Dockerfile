FROM python:3.9
WORKDIR /api
COPY . /api

EXPOSE 5000
ENV FLASK_APP=main.py

RUN pip install -r requirements.txt

CMD python main.py
FROM python:3.6
WORKDIR /
COPY requirements.txt ./


RUN pip3 install -r requirements.txt
COPY . .

CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py"]


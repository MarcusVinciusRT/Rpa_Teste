FROM python

WORKDIR /rpa

COPY rpa.py /rpa

COPY requirements.txt /webpython/

RUN apt-get update

RUN apt-get install nano

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

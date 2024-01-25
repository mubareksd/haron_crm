FROM python

COPY . /haron_crm
WORKDIR /haron_crm

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
FROM python:3.10

WORKDIR /flak-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY page.py ./app
COPY csv_conveter.py ./app
COPY test.py ./app
COPY templates/ ./templates

CMD ["python", "./app/page.py"]


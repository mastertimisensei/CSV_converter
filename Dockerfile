FROM python:3.10

WORKDIR /flak-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/page.py"]


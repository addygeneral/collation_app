FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

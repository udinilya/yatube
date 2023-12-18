FROM python:3.9

RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
RUN python3 manage.py collectstatic --no-input
CMD gunicorn yatube.wsgi:application --bind 0.0.0.0:8000

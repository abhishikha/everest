FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /=
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8080
WORKDIR /code/mysite
CMD ["python", "manage.py", "runserver"]

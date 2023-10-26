FROM python:3
#dummy
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000
WORKDIR /code/mysite
CMD ["python", "manage.py", "runserver"]

FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install -r task_deepx/requirements.txt

EXPOSE 8000

CMD ["python", "task_deepx/manage.py", "runserver", "0.0.0.0:8000"]

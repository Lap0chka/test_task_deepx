FROM python:3.12

WORKDIR /task_deepx

COPY task_deepx /task_deepx

RUN pip install -r /task_deepx/requirements.txt

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

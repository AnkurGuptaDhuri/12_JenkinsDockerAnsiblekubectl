FROM python:3.8.2-alpine3.11

#ENV FLASK_ENV=development

WORKDIR /app-demo

COPY . /app-demo/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "./app_run.py", "run", "--host", "0.0.0.0"]









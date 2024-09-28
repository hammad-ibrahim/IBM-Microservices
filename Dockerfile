FORM python:3.8

COPY . /app

ENV LISTEN_PORT 8080

EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["python", "m", "flask", "run"
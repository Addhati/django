FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
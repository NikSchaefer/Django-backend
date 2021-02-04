FROM python:3.6

RUN pip install pipenv

ENV PYTHONUNBUFFERED=1

WORKDIR /

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy

ENV DEBUG=False

COPY . .

EXPOSE 8000

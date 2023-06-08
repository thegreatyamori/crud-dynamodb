FROM python:3.10.4

COPY pyproject.toml .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry config experimental.new-installer false
RUN poetry install --no-root --only main

COPY ./app app/

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]

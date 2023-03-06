FROM python:3.9

LABEL maintainer="development@planetly.org"

WORKDIR /app

ENV PYTHONPATH=/app
RUN useradd -m app
RUN chown -R app:app /app

COPY --chown=app:app requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt
USER app
COPY --chown=app:app . .
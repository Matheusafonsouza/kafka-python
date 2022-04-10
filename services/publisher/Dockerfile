FROM python:3.9-slim

ENV PYTHONBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

ADD common /code/common/
ADD services/publisher /code/services/publisher/

RUN pip install --no-cache-dir -r /code/services/publisher/requirements.txt

ENTRYPOINT ["python3", "/code/services/publisher/main.py"]
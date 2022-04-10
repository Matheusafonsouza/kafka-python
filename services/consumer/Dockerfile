FROM python:3.9-slim

ENV PYTHONBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/code/"

WORKDIR /code

ADD common /code/common/
ADD services/consumer /code/services/consumer/

RUN pip install --no-cache-dir -r /code/services/consumer/requirements.txt

ENTRYPOINT ["python3", "/code/services/consumer/main.py"]
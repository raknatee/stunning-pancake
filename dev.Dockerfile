FROM python:3.12.4-bullseye
WORKDIR /container
EXPOSE 80


RUN pip install pdm
# COPY ./src/Pipfile* .


COPY ./container .

ENV TZ=Asia/Bangkok

CMD tail -f /dev/null
# CMD pdm run uvicorn main:app --host 0.0.0.0 --port 80 --reload


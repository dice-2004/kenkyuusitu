FROM python:3.9-slim

WORKDIR /app/src/

COPY ./requirements.txt /app/src/
RUN pip install -r requirements.txt
# CMD [ "python","main.py" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]

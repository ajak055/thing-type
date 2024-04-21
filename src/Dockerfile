FROM python:3.11.6-slim

RUN mkdir -p /home

COPY ./ /home

WORKDIR /home

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "app.py"]
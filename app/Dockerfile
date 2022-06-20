FROM python:3.9

ENV http_proxy http://host.docker.internal:3128
ENV https_proxy http://host.docker.internal:3128
#ENV FLASK_ENV=development
EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY app.py /app
CMD python app.py
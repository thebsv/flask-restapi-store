FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "app.py"]

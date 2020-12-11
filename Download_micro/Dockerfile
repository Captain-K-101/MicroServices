FROM python:3.6
COPY . /app
WORKDIR /app
RUN mkdir ./app/uploads
RUN pip install -r requirements.txt
RUN chmod 777 ./app/uploads
ENTRYPOINT ["python"]
CMD ["app/app.py"]

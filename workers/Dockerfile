FROM python:3.6
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]

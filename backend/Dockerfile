FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8084

CMD ["python3", "main.py"]

# docker build --no-cache -t myimage2 .
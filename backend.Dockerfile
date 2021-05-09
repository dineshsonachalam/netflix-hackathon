FROM python:3.7

WORKDIR /app

COPY backend .

RUN pip install -r requirements.txt

EXPOSE 8001

RUN chmod +x /app/main.py

CMD ["python3", "main.py"]
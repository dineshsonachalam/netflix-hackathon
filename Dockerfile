# Here we are creating an image for python alphine image.(https://hub.docker.com/r/library/python/)
FROM python:3

CMD ["mkdir","/app/backend"]

# Copying the entire application to the docker container in the app directory.
COPY ./backend /app/backend


# WORKDIR is nothing but current directory (cd app)
WORKDIR /app/backend

# Install the requirements in the current directory.
RUN pip install -r requirements.txt


# It executes the command python app.py in the app directory.# start gunicorn
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8087", "main:app"]


EXPOSE 8087


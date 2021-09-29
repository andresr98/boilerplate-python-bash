# Create image based on the official Python 3.7 image from the dockerhub
FROM python:3.7-slim-buster

# Create a directory where our app will be placed
RUN mkdir -p /usr/src/app

# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/app

# Copy dependency definitions
COPY requirements.txt /usr/src/app/

# Install project dependecies
RUN python3 -m pip install -r requirements.txt

# Get all the code needed to run the app
COPY . /usr/src/app

# Serve the app
ENTRYPOINT [ "python3", "app/main.py" ]
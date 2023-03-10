FROM python:3.9-slim-buster

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN python3 -m venv venv && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

# Copy the app code
COPY . .

ENV DATABASE_URL ${DATABASE_URL}
ENV BOOTSTRAP_SERVERS ${DATABASE_URL}
ENV TOPIC ${TOPIC}
ENV STAGE ${STAGE}

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run the application using flask run
CMD . venv/bin/activate && python3 main.py


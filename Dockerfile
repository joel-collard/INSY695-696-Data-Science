FROM python:3.12.7-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents to /app
COPY . /app

# Install required build dependencies
RUN apt-get update && \
    apt-get install -y build-essential python3-dev libffi-dev gcc g++ && \
    apt-get clean

RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask default port
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]

# docker push joelcollard/my-flask-app:latest
# docker build -t joelcollard/my-flask-app:latest .
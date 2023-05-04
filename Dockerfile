# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8081
EXPOSE 8081

# Set the command to run the Flask app on port 8081 when the container starts
CMD ["python", "app.py", "--port=8081"]

# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app files to the container
COPY app.py /app/
COPY requirements.txt /app/
COPY init.sql /docker-entrypoint-initdb.d/

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 2500

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=users_db

# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Run the Flask application
CMD ["python", "app.py"]


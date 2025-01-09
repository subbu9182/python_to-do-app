# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py /app
COPY requirements.txt /app
COPY index.html /app
COPY style.css /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["python", "/app/app.py"]


# Use a lightweight official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code into the container
COPY service/ ./service/

# Create and switch to a non-root user
RUN useradd --uid 1000 theia && chown -R theia /app
USER theia

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:8080", "--log-level=info", "service:app"]

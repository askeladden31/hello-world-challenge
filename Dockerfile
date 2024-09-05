# Use a lightweight Python image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app/

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the Python web server
CMD ["python", "app.py"]


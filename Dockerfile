# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --verbose -r requirements.txt

# Expose the port that the client will run on
EXPOSE 80

# Run the command to start the client
CMD ["python", "app.py"]
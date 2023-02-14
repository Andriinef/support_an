# Use an official Python runtime as a parent image
FROM python:3.10.4-slim

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file to the container
COPY ./requirements.txt /tmp/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the project code to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Set the command to run when the container starts
CMD ["python", "app.py"]

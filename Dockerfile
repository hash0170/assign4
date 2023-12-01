# dockerfile, Image, Container


# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY main.py /app

# Run the Python script when the container launches
CMD ["python", "main.py"]

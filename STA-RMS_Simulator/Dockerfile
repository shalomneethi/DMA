# Use the official Python image from Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python requirements file into the container
COPY STA-RMS_Simulator/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask application code into the container
COPY STA-RMS_Simulator/sta-rms-app.py .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "sta-rms-app.py"]

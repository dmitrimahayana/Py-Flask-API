# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /FlaskAPI

# Copy the current directory contents into the container
COPY . /FlaskAPI

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make ports available to the world outside this container
EXPOSE 80 5000

# Define environment variable
ENV NAME FlaskAPI

# Run PeopleAPI.py when the container launches
CMD ["python", "PeopleAPI.py"]
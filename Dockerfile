# Use official Python image (with Python installed)
FROM python:3.13.9

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Command to run your Python script by default
CMD ["python", "data_bricks_python.py"]
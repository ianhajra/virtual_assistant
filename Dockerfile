# Use the slim Python image from the Docker Hub
FROM python:slim

# Set environment variables
# Writes to stdout and stdin unbuffered
ENV PYTHONUNBUFFERED=1
# Stops Python from saving .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Set the virtual environment path
ENV VENV_PATH=/opt/venv
# Ensure the virtual environment's bin directory is in the PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create the virtual environment
RUN python3 -m venv $VENV_PATH

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r nlp/requirements.txt \
    && pip install --no-cache-dir -r user_information/requirements.txt \
    && pip install --no-cache-dir -r core/requirements.txt

# run main file
CMD ["python", "main.py"]
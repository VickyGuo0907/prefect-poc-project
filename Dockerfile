# We're using the latest version of Prefect with Python 3.12
FROM python:3.12

RUN mkdir -p /home/prefect-poc-project/

WORKDIR /home/prefect-poc-project/

# Copy all the required files from host to container
COPY . ./

# Add our requirements.txt file to the image and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/prefect-poc-project/requirements.txt

# Set the environment variables for prefect server, change API URL to point your Prefect server
ENV PREFECT_API_URL=http://127.0.0.1:4200/api
ENV PREFECT_LOGGING_LEVEL="INFO"

# Run our flow script when the container starts
CMD ["python", "flows/health_check.py"]
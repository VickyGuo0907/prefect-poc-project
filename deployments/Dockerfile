# We're using the latest version of Prefect with Python 3.12
FROM python:3.12

# Install Git
RUN apt-get update && apt-get install -y git

RUN mkdir -p /home/prefect-poc-project/

WORKDIR /home/prefect-poc-project/

# Clone workflow repository into container (change to your own repository)
RUN git clone https://github.com/VickyGuo0907/prefect-poc-project.git ./

# List the contents in container directory
RUN ls -al /home/prefect-poc-project/

# Add our requirements.txt file to the image and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /home/prefect-poc-project/requirements.txt

# Set the environment variables for prefect server, change API URL to point your Prefect server
ENV PREFECT_API_URL=http://127.0.0.1:4200/api
ENV PREFECT_LOGGING_LEVEL="INFO"

ENTRYPOINT ["/home/prefect-poc-project/deployments/deployment_scheduled_pool.sh"]
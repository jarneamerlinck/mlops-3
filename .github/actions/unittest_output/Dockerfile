# Docker image that we're using. This will install a prebuilt environment of python and the base required packages.
FROM python:3.9

# Copy our requirements file into the docker container
COPY requirements.txt ./

# Install the additional requirements
RUN pip install -r requirements.txt

# Copy the root level of our github repository (so, all files) into the root level of our container
COPY . .

# Define which command we should run when starting the container
ENTRYPOINT ["sh","/entrypoint.sh"]

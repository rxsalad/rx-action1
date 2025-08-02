FROM docker.io/python

# Install essential utilities
RUN apt-get update && apt-get install -y curl  net-tools iputils-ping tree

# Upgrade pip and install additional packages
RUN pip install --upgrade pip
RUN pip install flask python-dotenv 

# copy hello.py, and Dockerfile to /app
WORKDIR /app
COPY hello.py Dockerfile /app/

# Declaration: the container listens on TCP port 8888.
EXPOSE 8888

# Set the default command 
#CMD ["sleep", "infinity"]
CMD ["python", "hello.py"]



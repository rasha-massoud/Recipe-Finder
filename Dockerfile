# Use official Python base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the working directory
COPY . /app

# Update and install necessary packages
RUN apt-get update -y && apt-get install -y python3-pip git \
    && pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install streamlit

# Expose the port on which the Streamlit app runs
EXPOSE 80

# Command to run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0"]

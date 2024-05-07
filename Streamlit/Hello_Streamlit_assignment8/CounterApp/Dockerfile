# Use Python 3.9 slim as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the Streamlit example repository
RUN git clone https://github.com/streamlit/streamlit-example.git .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Healthcheck to verify the application is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Entry point command to start the Streamlit application
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
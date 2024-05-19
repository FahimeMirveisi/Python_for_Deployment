
FROM python 

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . /app

EXPOSE 8501

# Healthcheck to verify the application is running
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Entry point command to start the Streamlit application
# ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
ENTRYPOINT ["streamlit", "run", "main.py"]
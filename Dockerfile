FROM python:3.12
LABEL authors="jeffrey"

# set the working directory for the data-server application
WORKDIR /app

# install the environment dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copy the required files to the container working directory
COPY data_server/main.py /app
COPY data_server/data_model.py /app
COPY data_server/connectors.py /app
COPY data_server/TransactionHistory.csv /app

# start the unicorn API server
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
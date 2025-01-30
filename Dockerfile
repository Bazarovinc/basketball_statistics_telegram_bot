FROM python:3.10-slim

# Set the working directory
WORKDIR /code

# Install poetry
RUN pip install poetry==1.3.1

# Copy only the pyproject.toml and poetry.lock files to install dependencies first
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with-credentials --without-urls
RUN pip install --no-cache-dir -r requirements.txt


COPY ./main.py /code

COPY ./src /code/src
COPY ./common /code/common
COPY ./images /code/images
#COPY ./test_main.py /code

CMD python main.py
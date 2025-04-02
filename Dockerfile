FROM python:3.11-slim

# Set the working directory
WORKDIR /code

# Install poetry
RUN pip install uv

# Copy only the pyproject.toml and poetry.lock files to install dependencies first
COPY pyproject.toml ./

# Install dependencies
RUN uv pip install -r pyproject.toml


COPY ./main.py /code

COPY ./src /code/src
COPY ./common /code/common
COPY ./images /code/images
#COPY ./test_main.py /code

CMD python main.py
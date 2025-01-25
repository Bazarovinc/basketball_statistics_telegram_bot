FROM python:3.10-slim


#RUN apt-get update && apt-get install -y \
#    libexpat1 \
#    libgomp1 \
#    libx11-6 \
#    libxext6 \
#    libxrender1 \
#    libglib2.0-0 \
#    libgl1-mesa-glx \
#    libxi6 \
#    libdbus-1-3 \
#    --no-install-recommends \
#    && rm -rf /var/lib/apt/lists/*

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
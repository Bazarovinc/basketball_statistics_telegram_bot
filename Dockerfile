FROM python:3.11-slim

# Set the working directory
WORKDIR /code
ENV UV_PROJECT_ENVIRONMENT=/usr/local
# Install poetry
RUN pip install uv

# Copy only the pyproject.toml and poetry.lock files to install dependencies first
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --locked --no-dev
#ENV PATH="/code/.venv/bin:$PATH"


COPY ./main.py /code

COPY ./src /code/src
COPY ./common /code/common
COPY ./images /code/images

CMD python main.py
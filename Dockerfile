FROM python:3.11-slim

# Set the working directory
WORKDIR /code

# Install uv
RUN pip install uv

COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project --no-dev
ENV PATH="/code/.venv/bin:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/usr/local

COPY ./main.py /code

COPY ./src /code/src
COPY ./common /code/common
COPY ./images /code/images

CMD python main.py
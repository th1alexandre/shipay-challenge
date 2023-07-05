### Base stage, load environment variables
FROM python:3.11-slim-bullseye as python-base

# Python envs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random

# Pip envs
ENV PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Poetry envs
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.3.0 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# Other envs
ENV APP_PATH=/app \
    PYSETUP_PATH=/opt/pysetup \
    VENV_PATH=/opt/pysetup/.venv \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


### Building stage, installs poetry and main dependencies
FROM python-base as poetry-builder

# Installs essential tools for building poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl build-essential

# Install Poetry, respects $POETRY_VERSION and $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python

# Cache requirements and installs only main dependencies
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --only main


### Pre-development stage, installs dev dependencies
FROM poetry-builder as pre-development

# Have cache for main dependencies
WORKDIR $PYSETUP_PATH

# Installs development dependencies
RUN poetry install --only dev


### Development final stage
FROM python-base as development

# Copy Poetry and pre-build development dependencies
COPY --from=pre-development $POETRY_HOME $POETRY_HOME
COPY --from=pre-development $PYSETUP_PATH $APP_PATH

# Required to bind docker-compose volumes
WORKDIR $APP_PATH

# Copy all files to container, .dockerignore
# should be used to avoid copying unnecessary files
COPY . .

# Flask app port
EXPOSE 5000

# Run flask in development mode, debug true
ENTRYPOINT poetry run python -u src/main.py


### Pre-production stage, installs prod dependencies
FROM poetry-builder as pre-production

# Installs essential tools for building psycopg[c]
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        libpq-dev gcc \
        python3-dev

# Have cache for main dependencies
WORKDIR $PYSETUP_PATH

# Installs production dependencies
RUN poetry install --only prod


### Production final stage
FROM python-base as production

# Copy Poetry and pre-build production dependencies
COPY --from=pre-production $POETRY_HOME $POETRY_HOME
COPY --from=pre-production $PYSETUP_PATH $APP_PATH

# Required to bind docker-compose volumes
WORKDIR $APP_PATH

# Copy only source code for production
COPY ./src /app/src

# Flask app port
EXPOSE 5000

# Run flask in production mode, debug false
ENTRYPOINT poetry run python -u src/main.py
